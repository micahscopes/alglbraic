from .base import GLSL, meta_glsl, GlslBundler
from sympy import symbols
from sympy.matrices import Matrix
from string import Template
from . import array_tools

class GlslStruct(GlslBundler, array_tools.Mixin):
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

