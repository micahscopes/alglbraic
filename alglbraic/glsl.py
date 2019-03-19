from sympy import symbols
from sympy import Matrix
from string import Template
from inspect import getmembers, ismethod, signature
from alglbraic.util import get_arguments
from alglbraic.util import MetaString


class GLSL(MetaString):
    depends_on: list = []
    pass

def get_glsl_meta(func):
    try:
        glsl_meta = signature(func).return_annotation
        if issubclass(glsl_meta, GLSL):
            return glsl_meta
    except Exception:
        return None


def is_glsl_method(func):
    return get_glsl_meta(func) is not None


def is_glsl_helper(func):
    return is_glsl_method(func) and len(get_arguments(func)) > 0


def is_glsl_snippet(func):
    return is_glsl_method(func) and len(get_arguments(func)) == 0


class GlslStruct:
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

    def _glsl_methods(self):
        return (func for name, func in getmembers(self) if is_glsl_method(func))

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


def sort_glsl_dependencies(glsl_node_graph, glsl_node):
    # from Blckknght @ https://stackoverflow.com/a/47234034
    result = []
    seen = set()
    unseen = set(glsl_node_graph.keys())

    def hop(node):
        nonlocal unseen
        for neighbor in get_glsl_meta(glsl_node_graph[node]).depends_on:
            if neighbor not in seen:
                seen.add(neighbor)
                unseen = seen - unseen
                hop(neighbor)
        result.insert(0, node)

    while len(unseen) > 0:
        hop(unseen.pop())
    return result



struct_template = Template(
    """\
struct $type_name {
    $members
}\
"""
)
