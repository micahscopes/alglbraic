import click
from alglbraic.util import with_outfile
from .clifford_algebra import CliffordAlgebra, ComplexNumbers, DualNumbers

class IntListParamType(click.ParamType):
    name = "IntList"

    def convert(self, value, param, ctx):
        try:
            return [int(i) for i in value.split(" ")]
        except ValueError:
            self.fail("%s is not a valid integer list" % value, param, ctx)


INTLIST = IntListParamType()


class StringListParamType(click.ParamType):
    name = "StringList"

    def convert(self, value, param, ctx):
        try:
            return [s for s in " ".split(value)]
        except ValueError:
            self.fail("%s is not a valid string list" % value, param, ctx)


STRLIST = StringListParamType()


@click.group(chain=True)
def commands():
    pass


def simple_cli_options(function):
    import click

    function = click.pass_context(function)
    function = click.option("--base", "base_ring")(function)
    function = click.option("--basis_names", "basis_names", type=STRLIST)(function)
    function = click.option("--name", "name")(function)
    return function

@commands.command()
@click.argument("name")
@click.argument("quadratic_form", type=INTLIST)
@simple_cli_options
def clifford_algebra(ctx, **kwargs):
    kwargs = {k: v for (k, v) in kwargs.items() if v is not None}
    alg = ctx.obj["latest_struct"] = CliffordAlgebra(**kwargs)
    ctx.obj["results"][alg.type_name] = alg
    return alg.bundle()


@commands.command()
@simple_cli_options
def complex_numbers(ctx, **opts):
    opts = {k: v for (k, v) in opts.items() if v is not None}
    alg = ctx.obj["latest_struct"] = ComplexNumbers(**opts)
    ctx.obj["results"][alg.type_name] = alg
    return alg.bundle()


@commands.command()
@simple_cli_options
@click.option("--size", "size", type=int)
def dual_numbers(ctx, **opts):
    opts = {k: v for (k, v) in opts.items() if v is not None}
    alg = ctx.obj["latest_struct"] = DualNumbers(**opts)
    ctx.obj["results"][alg.type_name] = alg
    return alg.bundle()
