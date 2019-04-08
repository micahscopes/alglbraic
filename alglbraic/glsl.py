from sympy import symbols
from sympy import Matrix
from string import Template
from inspect import getmembers, signature
from alglbraic.util import get_arguments, MetaString
from typing import List, Union
from types import FunctionType


class GLSL(MetaString):
    depends_on: list = []
    pass


def meta_glsl(*args, **kwargs):
    MetaGLSL_type = GLSL(*args, **kwargs)

    def meta_glsl_decorator(func):
        def wrapper(*gl_args, **gl_kwargs) -> MetaGLSL_type:
            return MetaGLSL_type(func(*gl_args, **gl_kwargs))

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


class GlslBundler:
    def _glsl_methods(self):
        members = sorted(getmembers(self))
        glsl_methods = [func for name, func in members if is_glsl_method(func)]
        return sort_glsl_dependencies(glsl_methods)

    def glsl_methods(self):
        return tuple(self._glsl_methods())

    def glsl_helpers(self):
        return tuple(
            func for func in self._glsl_methods() if len(get_arguments(func)) > 0
        )

    def glsl_snippets(self):
        return tuple(
            func for func in self._glsl_methods() if len(get_arguments(func)) == 0
        )

    def compile_snippet_bundle(self):
        return "\n\n".join(s() for s in self.glsl_snippets())


class GlslStruct(GlslBundler):
    def __init__(self, type_name, *member_declarations):
        self.type_name = type_name
        self.member_declarations = member_declarations
        self.member_types, self.member_names = zip(
            *[mt.split() for mt in member_declarations]
        )

    def symbols_for(self, instance_name="x"):
        members = self.member_names
        return symbols([str(instance_name) + "." + str(m) for m in members])

    def symbols_vector_for(self, instance_name="x"):
        return Matrix(self.symbols_for(instance_name))

    @meta_glsl(depends_on=[])
    def definition(self, separator="; "):
        members = separator.join(self.member_declarations) + separator.strip()
        return GLSL(
            struct_template.substitute(type_name=self.type_name, members=members)
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
        fn_name(node): set(fn_name(d) for d in get_meta_glsl(node).depends_on)
        for node in glsl_nodes
    }

    sorted_by_dependencies = toposort_flatten(graph)
    return [fn_lookup[k] for k in sorted_by_dependencies]


struct_template = Template(
    """\
struct $type_name {
    $members
}\
"""
)
