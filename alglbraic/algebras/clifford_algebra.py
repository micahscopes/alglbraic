from alglbraic.algebra import Algebra
from galgebra.ga import Ga
from alglbraic import GLSL
from alglbraic.glsl import meta_glsl
from functools import reduce
import click

import contextlib
import io


def build_basis_names(clifford_algebra, prefix="e", separator=""):
    Cl = clifford_algebra
    base = (
        lambda indexes: prefix + separator + separator.join(str(i + 1) for i in indexes)
    )
    return [base(indexes) for indexes in Cl.indexes_lst]


class CliffordAlgebra(Algebra):
    def __init__(
        self,
        name,
        signature,
        base_ring="float",
        unit="scalar",
        basis_names=None,
        **kwargs
    ):
        from sympy import symbols

        gens = "e*" + "|".join("%i" % (i + 1) for i in range(len(signature)))

        the_void = io.StringIO()
        with contextlib.redirect_stdout(the_void):
            ga = Ga.build(gens, g=signature)

        self.Cl, *self._grade_1_basis = ga
        basis_names = (
            [unit] + build_basis_names(self.Cl)
            if basis_names is None or len(basis_names) == 0
            else basis_names
        )
        Algebra.__init__(self, name, base_ring, *basis_names, unit=unit, **kwargs)

    def _algebraic_element_from_coefficients(self, coefficients):
        return self.Cl.mv(
            reduce(
                lambda u, v: u + v,
                [a * x for a, x in zip(coefficients, self.Cl.blades_lst0)],
                0,
            )
        )

    def _coefficients_from_algebraic_element(self, element):
        return element.blade_coefs()

    @meta_glsl()
    def reverse(self, **kwargs) -> GLSL:
        result = self.algebraic_arguments(1).rev()
        return self.algebraic_operation("reverse", result, n=1, **kwargs)

    @meta_glsl()
    def grade_involution(self, **kwargs) -> GLSL:
        x = self.algebraic_arguments(1)
        result = x.even() - x.odd()
        return self.algebraic_operation("involve", result, n=1, **kwargs)

    @meta_glsl(depends_on=[reverse, grade_involution])
    def conjugation(self, **kwargs) -> GLSL:
        result = "reverse(involve(u))"
        return self.algebraic_operation("conjugate", result, n=1, **kwargs)


class ComplexNumbers(CliffordAlgebra):
    def __init__(self, name="C", base_ring="float", unit="real", **kwargs):
        basis_names = ["real", "imag"]
        opts = {
            "name": name,
            "signature": [-1],
            "basis_names": basis_names,
            "unit": unit,
            "base_ring": base_ring,
        }
        opts.update(kwargs)
        CliffordAlgebra.__init__(self, **opts)


class DualNumbers(CliffordAlgebra):
    def __init__(self, name="Dual", base_ring="float", unit="real", **kwargs):
        basis_names = ["real", "nilpotent"]
        opts = {
            "name": name,
            "signature": [0],
            "basis_names": basis_names,
            "unit": unit,
            "base_ring": base_ring,
        }
        opts.update(kwargs)
        CliffordAlgebra.__init__(self, **opts)


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


@click.group()
def commands():
    pass


@commands.command()
@click.argument("name")
@click.argument("signature", type=INTLIST)
@click.option("--base", "base_ring")
@click.option("--basis_names", "basis_names", type=STRLIST)
@click.option("--unit", "unit")
def clifford_algebra(*args, **kwargs):
    kwargs = {k: v for (k, v) in kwargs.items() if v is not None}
    click.echo(CliffordAlgebra(**kwargs).bundle())


def simple_cli_options(function):
    import click

    # function = click.pass_context(function)
    function = click.option("--base", "base_ring")(function)
    function = click.option("--basis_names", "basis_names", type=STRLIST)(function)
    function = click.option("--name", "name")(function)
    return function


@commands.command()
@simple_cli_options
def complex_numbers(*args, **kwargs):
    kwargs = {k: v for (k, v) in kwargs.items() if v is not None}
    click.echo(ComplexNumbers(**kwargs).bundle())


@commands.command()
@simple_cli_options
def dual_numbers(*args, **kwargs):
    kwargs = {k: v for (k, v) in kwargs.items() if v is not None}
    click.echo(DualNumbers(**kwargs).bundle())
