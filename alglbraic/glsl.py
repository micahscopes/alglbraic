from sympy import symbols
from sympy import Matrix
from sympy.tensor import IndexedBase
from string import Template
from inspect import getmembers, signature
from alglbraic.util import get_arguments, MetaString
from typing import List, Union
from types import FunctionType
from rop import read_only_properties
from functools import total_ordering
from functools import wraps, update_wrapper
import types
from sortable_callable import sortable, SortableCallable
import functools


class GLSL(MetaString):
    depends_on: list = []
    pass


def less_than(self, other):
    return self.__name__ < other.__name__


def meta_glsl(*args, **kwargs):

    def meta_glsl_decorator(func):
        sig = inspect.signature(func)
        
        if issubclass(sig.return_annotation, GLSL):
            MetaGLSL_type = sig.return_annotation(*args, **kwargs)
        else:
            MetaGLSL_type = GLSL(*args, **kwargs)

        def wrapper(*gl_args, **gl_kwargs) -> MetaGLSL_type:
            return MetaGLSL_type(func(*gl_args, **gl_kwargs))

        wrapper.__signature__ = sig.replace(
            return_annotation=MetaGLSL_type
        )

        wrapper = sortable(less_than)(wrapper)
        wrapper.__name__ = func.__name__

        return wrapper

    return meta_glsl_decorator


def get_meta_glsl(func):
    try:
        meta_glsl = signature(func).return_annotation
        if issubclass(meta_glsl, GLSL):
            return meta_glsl
    except Exception:
        return None


def is_glsl_method(func):
    return get_meta_glsl(func) is not None


def is_glsl_helper(func):
    return is_glsl_method(func) and len(get_arguments(func)) > 0


def is_glsl_snippet(func):
    return is_glsl_method(func) and len(get_arguments(func)) == 0


import inspect


class GlslBase:
    # def __init_subclass__(cls):
    #     for name, func in cls.__dict__.items():
    #         if is_glsl_method(func):
    #             def __lt__(self, other):
    #                 return func.__name__ < other.__name__
    #             func.__lt__ = __lt__
    pass


# @decorate_class
class GlslBundler(GlslBase):
    # __metaclass__ = GlslMetaclass
    # __glsl_methods__ = []
    def _glsl_methods(self):
        members = getmembers(self)
        glsl_methods = [
            getattr(self, name) for name, func in members if is_glsl_method(func)
        ]
        # import ipdb; ipdb.set_trace()
        wrapped_glsl_methods = [meta_glsl()(gl) for gl in glsl_methods]
        # import ipdb; ipdb.set_trace()
        # return wrapped_glsl_methods
        return sort_glsl_dependencies(wrapped_glsl_methods)

    def glsl_methods(self):
        return tuple(self._glsl_methods())

    def glsl_helpers(self):
        return tuple(
            func for func in self._glsl_methods() if len(get_arguments(func)) > 0
        )

    def glsl_snippets(self):
        # import ipdb; ipdb.set_trace()
        return tuple(
            func for func in self._glsl_methods() if len(get_arguments(func)) == 0
        )

    def compile_snippet_bundle(self):
        return "\n\n".join(s() for s in self.glsl_snippets())


@read_only_properties("type_name", "member_declarations", "member_types")
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

    @meta_glsl(depends_on=[])
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
    from toposort import toposort_flatten

    def fn_name(str_or_fn) -> str:
        try:
            return str_or_fn.__name__
        except AttributeError:
            return str_or_fn

    fn_lookup = {fn_name(node): node for node in glsl_nodes}

    graph = {
        node: set(fn_lookup[fn_name(d)] for d in get_meta_glsl(node).depends_on)
        for node in glsl_nodes
    }

    # sorted_by_dependencies = toposort_flatten(graph)
    return toposort_flatten(graph)
    # return [fn_lookup[k] for k in sorted_by_dependencies]
