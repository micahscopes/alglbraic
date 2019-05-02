from .base import glsl_snippet, GLSL, GlslBundler
from sympy import symbols
from sympy.matrices import Matrix
from string import Template
from . import array_tools
from alglbraic.util import with_outfile

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

class GlslStruct(GlslBundler, array_tools.BuildFromArray):
    def __init__(self, type_name, *member_declarations):
        self.type_name = type_name
        self.member_declarations = member_declarations
        self.member_types, self.member_names = zip(
            *[mt.split() for mt in member_declarations]
        )

    def member_index_const(self, member):
        i = int(member) if RepresentsInt(member) else None
        i = self.member_names.index(member) if i is None else i
        member_name = self.member_names[i]
        return "I_%s_%s" % (self.type_name, member_name)

    def injections(self, members, inject_fn_name="inject"):
        if len(members) > len(self):
            raise ValueError(
                f"Tried to generate injections of size {len(members)} for a struct \
of size {len(self)}!"
            )
        return array_tools.struct_injections(self, members, inject_fn_name=inject_fn_name)

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

    @GLSL
    def definition(self, separator=";\n    "):
        template = Template(
            """\
$indices;

struct $type_name {
    $members
};\
"""
        )
        indices = ';\n'.join(
            "const int "+self.member_index_const(i)+" = "+str(i)
            for i in range(len(self))
        )
        members = separator.join(self.member_declarations) + separator.strip()
        return glsl_snippet(template.substitute(type_name=self.type_name, members=members, indices=indices))


import click


@click.group(chain=True)
def commands():
    pass

@commands.command()
@click.argument("name", type=str)
@click.argument("members", type=str)
@click.pass_context
def injections(ctx, **opts):
    struct = ctx.obj.get("latest_struct")
    name = opts.pop("name")
    members = opts.pop("members").split(" ")
    if all(RepresentsInt(m) for m in members):
        members = (int(m) for m in members)

    if not name:
        name = "inject_"+"_".join(str(m) for m in members)

    ctx.obj["results"][name] = struct.injections(members, inject_fn_name=name, **opts)
