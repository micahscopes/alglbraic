from sympy import symbols
from sympy import Matrix
from sympy.tensor import IndexedBase
from string import Template
from inspect import getmembers, signature
from alglbraic.util import get_arguments, MetaString
from typing import List, Union
from types import FunctionType
import inspect


def meta_glsl(*args, **kwargs):
    from alglbraic.util import Callable

    def meta_glsl_decorator(func):
        sig = inspect.signature(func)
        MetaGLSL_type = GLSL(*args, **kwargs)
        MetaGLSL_type.special = False

        if issubclass(sig.return_annotation, GLSL):
            MetaGLSL_type = sig.return_annotation(*args, special=True, **kwargs)

        def wrapper(*gl_args, **gl_kwargs) -> MetaGLSL_type:
            return MetaGLSL_type(func(*gl_args, **gl_kwargs))

        from functools import partial, update_wrapper

        class MetaCallable(Callable):
            def __set_name__(self, cls, name):
                MetaGLSL_type.glsl_type = cls

        wrapper = update_wrapper(MetaCallable(wrapper), MetaGLSL_type)
        wrapper.__signature__ = sig.replace(return_annotation=MetaGLSL_type)
        wrapper.__name__ = func.__name__
        return wrapper

    return meta_glsl_decorator


def get_meta_glsl(func):
    try:
        meta_glsl = signature(func).return_annotation
        if issubclass(meta_glsl, GLSL):
            return meta_glsl
    except (TypeError, ValueError):
        return None


def is_glsl_method(func):
    return get_meta_glsl(func) is not None


def is_glsl_helper(func):
    return is_glsl_method(func) and len(get_arguments(func)) > 1


def is_glsl_snippet(func):
    return is_glsl_method(func) and len(get_arguments(func)) == 0



class GlslBaseType(object):
    pass

class GLSL(MetaString):
    depends_on: list = []
    glsl_type = GlslBaseType
    pass

class GlslBundler(GlslBaseType):
    def _glsl_methods(self):
        members = getmembers(self)
        glsl_methods = [
            getattr(self, name) for name, func in members if is_glsl_method(func)
        ]
        return sort_glsl_dependencies(glsl_methods)
        # wrapped_glsl_methods = [meta_glsl()(gl) for gl in glsl_methods]
        # return sort_glsl_dependencies(wrapped_glsl_methods)

    def glsl_methods(self):
        return tuple(self._glsl_methods())

    def glsl_helpers(self):
        return tuple(func for func in self._glsl_methods() if is_glsl_helper(func))

    def glsl_snippets(self):
        return tuple(func for func in self._glsl_methods() if is_glsl_snippet(func))

    def compile_snippet_bundle(self):
        return "\n\n".join(s() for s in self.glsl_snippets())


# @read_only_properties("type_name", "member_declarations", "member_types")
class GlslStruct(GlslBundler):
    def __init__(self, type_name, *member_declarations):
        self.type_name = type_name
        self.member_declarations = member_declarations
        self.member_types, self.member_names = zip(
            *[mt.split() for mt in member_declarations]
        )

    def __len__(self):
        return len(self.member_declarations)

    @property
    def uniform_member_type(self):
        member_type_set = set(self.member_types)
        return member_type_set.pop() if len(member_type_set) == 1 else None

    def symbols_for(self, instance_name="x"):
        members = self.member_names
        return symbols([str(instance_name) + "." + str(m) for m in members])

    def symbols_vector_for(self, instance_name="x"):
        return Matrix(self.symbols_for(instance_name))

    @meta_glsl()
    def definition(self, separator="; "):
        template = Template(
            """\
struct $type_name {
    $members
}\
"""
        )
        members = separator.join(self.member_declarations) + separator.strip()
        return GLSL(template.substitute(type_name=self.type_name, members=members))

    @meta_glsl(depends_on=["definition"])
    def build_from_array(self, separator=", "):
        if not self.uniform_member_type:
            raise TypeError(
                "To generate an array constructor, GlslStruct must have members of\
                uniform type"
            )

        template = Template(
            """\
$type_name fromArray($base_type x[$size]){
    return $type_name($array_members);
}"""
        )

        x = IndexedBase("x")
        array_members = separator.join([str(x[i]) for i in range(len(self))])
        return template.substitute(
            type_name=self.type_name,
            base_type=self.uniform_member_type,
            array_members=array_members,
            size=len(self),
        )


def sort_glsl_dependencies(glsl_nodes: List[Union[str, FunctionType]]):
    """
        Parameters
        ----------
        glsl_nodes :
            A set of functions, each of which has a `GLSL` return type containing
            a `depends_on` attribute defining its dependencies.
    """
    from toposort import toposort

    def get_deps(node):
        try:
            return get_meta_glsl(node).depends_on + [get_meta_glsl(node).glsl_type]
        except AttributeError:
            return node.mro()

    def key(node):
        try:
            return str(len(node.mro()))
        except AttributeError:
            return (
                str(len(get_meta_glsl(node).glsl_type.mro()))
                + "."
                + str.lower(node.__name__)
            )

    # glsl_nodes = [meta_glsl()(n) for n in glsl_nodes]
    glsl_types = set(sum([get_meta_glsl(n).glsl_type.mro() for n in glsl_nodes], []))
    # for glsl_type in glsl_types:
    #     print(glsl_type)

    def fn_name(str_or_fn) -> str:
        try:
            return str_or_fn.__name__
        except AttributeError:
            return str_or_fn

    nodes = list(glsl_types) + glsl_nodes

    fn_lookup = {fn_name(node): node for node in nodes}

    graph = {node: set(fn_lookup[fn_name(d)] for d in get_deps(node)) for node in nodes}

    graph_toposorted = toposort(graph)
    graph_sorted = (
        sorted(
            (n for n in layer if type(n) is not type),
            key=key,
        )
        for layer in graph_toposorted
    )
    graph_sorted_flattened = sum(graph_sorted, [])

    return graph_sorted_flattened
