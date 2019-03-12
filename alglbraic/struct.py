from sympy import glsl_code
from sympy import symbols
from sympy import Matrix

from string import Template


class GlslStruct:
    def __init__(self, name, *member_declarations):
        self.name = name
        self.member_declarations = member_declarations
        self.member_types, self.member_names = zip(
            *[mt.split() for mt in member_declarations]
        )

    def symbols_for(self, instance_name="x"):
        members = self.member_names
        return symbols([str(instance_name) + "." + str(m) for m in members])

    def element(self, instance_name="x"):
        return Matrix(self.symbols_for(instance_name))

    def definition(self, separator="; "):
        members = separator.join(self.member_declarations) + separator.strip()
        return struct_template.substitute(name=self.name, members=members)


struct_template = Template(
    """\
struct $name {
    $members
}\
"""
)
