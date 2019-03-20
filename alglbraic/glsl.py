from sympy import symbols
from sympy import Matrix
from string import Template
from inspect import getmembers, ismethod, signature
from alglbraic.util import get_arguments
from alglbraic.util import MetaString


class GLSL(MetaString):
    depends_on: list = []
    pass


def meta_glsl(*args, **kwargs):
    MetaGLSL_type = GLSL(*args, **kwargs)

    def meta_glsl_decorator(func):
        def wrapper(*gl_args, **gl_kwargs) -> MetaGLSL_type:
            return MetaGLSL_type(func(*gl_args, **gl_kwargs))

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

    def definition(self, separator="; ") -> GLSL:
        members = separator.join(self.member_declarations) + separator.strip()
        return GLSL(
            struct_template.substitute(type_name=self.type_name, members=members)
        )


def sort_glsl_dependencies(glsl_nodes):
    from toposort import toposort_flatten

    lookup = {node.__name__: node for node in glsl_nodes}
    graph = {
        node.__name__: set(d.__name__ for d in get_meta_glsl(node).depends_on)
        for node in glsl_nodes
    }
    return [lookup[k] for k in toposort_flatten(graph)]


struct_template = Template(
    """\
struct $type_name {
    $members
}\
"""
)
