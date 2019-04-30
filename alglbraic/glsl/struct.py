from .base import GLSL, meta_glsl, GlslBundler
from sympy import symbols
from sympy.matrices import Matrix
from string import Template
from . import array_tools
from alglbraic.util import with_outfile


class GlslStruct(GlslBundler, array_tools.BuildFromArray):
    def __init__(self, type_name, *member_declarations):
        self.type_name = type_name
        self.member_declarations = member_declarations
        self.member_types, self.member_names = zip(
            *[mt.split() for mt in member_declarations]
        )

    def injections(self, size, inject_fn_name="inject"):
        if size > len(self):
            raise ValueError(
                f"Tried to generate injections of size {size} for a struct \
of size {len(self)}!"
            )
        return array_tools.struct_injections(self, size, inject_fn_name=inject_fn_name)

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
    def definition(self, separator=";\n    "):
        template = Template(
            """\
struct $type_name {
    $members
};\
"""
        )
        members = separator.join(self.member_declarations) + separator.strip()
        return GLSL(template.substitute(type_name=self.type_name, members=members))


import click


@click.group(chain=True)
def commands():
    pass

@commands.command()
@click.argument("size", type=int)
@click.option("--name", type=str)
@click.pass_context
def injections(ctx, **opts):
    struct = ctx.obj.get("latest_struct")
    name = opts.pop("name")

    if not name:
        name = "inject%i" % opts["size"]

    ctx.obj['results'][name] = struct.injections(inject_fn_name=name, **opts)
