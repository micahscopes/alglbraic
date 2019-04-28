from alglbraic.algebra import Algebra
from galgebra.ga import Ga
from alglbraic import GLSL
from alglbraic.glsl import meta_glsl
from sympy.matrices.matrices import MatrixError, NonSquareMatrixError
from sympy import diag, Matrix
from functools import reduce


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
        quadratic_form,
        grade_1_basis_names=None,
        base_ring="float",
        unit="scalar",
        basis_names=None,
        ga=None,
        **kwargs
    ):
        from sympy import symbols
        import contextlib
        import io

        # if `quadratic_form` is a matrix, get its dimension from its shape instead:
        try:
            signature = quadratic_form.diagonalize()[1].diagonal()
            quadratic_form = quadratic_form.tolist()
            quadratic_form = ' , '.join(' '.join(str(i) for i in row) for row in quadratic_form)
        except (MatrixError, NonSquareMatrixError) as e:
            raise e
        except Exception:
            signature = quadratic_form

        if not ga:
            if not grade_1_basis_names:
                grade_1_basis_names = "e*" + "|".join(
                    "%i" % (i + 1) for i in range(len(signature))
                )
            else:
                grade_1_basis_names = ' '.join(grade_1_basis_names)

            # import ipdb; ipdb.set_trace()
            the_void = io.StringIO()
            with contextlib.redirect_stdout(the_void):
                ga = Ga.build(grade_1_basis_names, g=quadratic_form)

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
        from sympy import sympify

        if self.base_ring == "float":
            return [
                sympify(co).evalf() if co != 0 else 0.0 for co in element.blade_coefs()
            ]
        else:
            return element.blade_coefs()

    @meta_glsl()
    def pseudoscalar(self, **kwargs) -> GLSL:
        result = self.Cl.I()
        return self.algebraic_operation("I", result, n=0, **kwargs)

    @meta_glsl()
    def dual(self, **kwargs) -> GLSL:
        result = self.algebraic_arguments(1) / self.Cl.I()
        return self.algebraic_operation("dual", result, n=0, **kwargs)

    @meta_glsl()
    def inner(self, **kwargs) -> GLSL:
        u, v = self.algebraic_arguments(2)
        result = u | v
        return self.algebraic_operation("inner", result, n=2, **kwargs)

    @meta_glsl()
    def outer(self, **kwargs) -> GLSL:
        u, v = self.algebraic_arguments(2)
        result = u ^ v
        return self.algebraic_operation("outer", result, n=2, **kwargs)

    @meta_glsl()
    def lcontract(self, **kwargs) -> GLSL:
        u, v = self.algebraic_arguments(2)
        result = u < v
        return self.algebraic_operation("lcontract", result, n=2, **kwargs)

    @meta_glsl()
    def rcontract(self, **kwargs) -> GLSL:
        u, v = self.algebraic_arguments(2)
        result = u > v
        return self.algebraic_operation("rcontract", result, n=2, **kwargs)

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
            "quadratic_form": [-1],
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
            "quadratic_form": [0],
            "basis_names": basis_names,
            "unit": unit,
            "base_ring": base_ring,
        }
        opts.update(kwargs)
        CliffordAlgebra.__init__(self, **opts)

    @meta_glsl()
    def pseudoscalar(self, **kwargs) -> GLSL:
        result = self._grade_1_basis[0]
        return self.algebraic_operation("I", result, n=0, **kwargs)


class ConformalGeometricAlgebra(CliffordAlgebra):
    def __init__(self, dimension, name=None, quadratic_form=None, **opts):
        name = name if name else ("CGA%i" % dimension)
        grade_1_basis_names = ["e%i" % (i+1) for i in range(dimension)] + ["nil", "inf"]

        quadratic_form = (
            diag(*dimension * [1], Matrix([[0, -1], [-1, 0]]))
            if not quadratic_form
            else quadratic_form
        )

        CliffordAlgebra.__init__(
            self, name, quadratic_form, grade_1_basis_names, **opts
        )
        # import ipdb; ipdb.set_trace()