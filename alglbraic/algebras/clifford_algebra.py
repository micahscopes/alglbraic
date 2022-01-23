from alglbraic.algebra import Algebra
from galgebra.ga import Ga
from alglbraic import glsl_snippet
from alglbraic.glsl import GLSL
from sympy.matrices.matrices import MatrixError, NonSquareMatrixError
from sympy import diag, eye, Matrix
from functools import reduce


def build_basis_names(
    clifford_algebra, prefix="e", grade_1_basis_names=None, separator=""
):
    return [
        prefix
        + separator
        + separator.join([x.strip(prefix).strip("_") for x in str(base).split("^")])
        for base in clifford_algebra.blades_lst
    ]


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
            quadratic_form = " , ".join(
                " ".join(str(i) for i in row) for row in quadratic_form
            )
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
                grade_1_basis_names = " ".join(grade_1_basis_names)

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
                [a * x for a, x in zip(coefficients, self.Cl._all_blades_lst)],
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

    def algebraic_element(self, base_symbol):
        return self._algebraic_element_from_coefficients(
            self.symbols_vector_for(base_symbol)
        )

    @GLSL
    def pseudoscalar(self, **kwargs):
        result = self.Cl.I()
        return self.algebraic_operation("I", result, n=0, **kwargs)

    @GLSL
    def dual(self, **kwargs):
        result = self.algebraic_arguments(1) / self.Cl.I()
        return self.algebraic_operation("dual", result, n=1, **kwargs)

    @GLSL
    def inner(self, **kwargs):
        u, v = self.algebraic_arguments(2)
        result = u | v
        return self.algebraic_operation("inner", result, n=2, **kwargs)

    @GLSL
    def outer(self, **kwargs):
        u, v = self.algebraic_arguments(2)
        result = u ^ v
        return self.algebraic_operation("outer", result, n=2, **kwargs)

    @GLSL(depends_on=[outer])
    def outer_3(self, **kwargs):
        p, q, r = self.n_ary_argnames(3)
        result = "outer(outer(%s, %s), %s)" % (p, q, r)
        return self.algebraic_operation("outer", result, n=3, **kwargs)

    @GLSL
    def lcontract(self, **kwargs):
        u, v = self.algebraic_arguments(2)
        result = u < v
        return self.algebraic_operation("lcontract", result, n=2, **kwargs)

    @GLSL
    def rcontract(self, **kwargs):
        u, v = self.algebraic_arguments(2)
        result = u > v
        return self.algebraic_operation("rcontract", result, n=2, **kwargs)

    @GLSL
    def reverse(self, **kwargs):
        result = self.algebraic_arguments(1).rev()
        return self.algebraic_operation("reverse", result, n=1, **kwargs)

    @GLSL
    def grade_involution(self, **kwargs):
        x = self.algebraic_arguments(1)
        result = x.even() - x.odd()
        return self.algebraic_operation("involve", result, n=1, **kwargs)

    @GLSL(depends_on=[reverse, grade_involution])
    def conjugation(self, **kwargs):
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

    @GLSL
    def pseudoscalar(self, **kwargs):
        result = self._grade_1_basis[0]
        return self.algebraic_operation("I", result, n=0, **kwargs)


class ConformalGeometricAlgebra(CliffordAlgebra):
    def __init__(self, dimension, name=None, quadratic_form=None, **opts):
        name = name if name else ("CGA%i" % dimension)
        grade_1_basis_names = ["e%i" % (i + 1) for i in range(dimension)] + [
            "nil",
            "inf",
        ]
        build_basis_names
        quadratic_form = (
            diag(eye(dimension), Matrix([[0, 1], [1, 0]]))
            if not quadratic_form
            else quadratic_form
        )

        CliffordAlgebra.__init__(
            self, name, quadratic_form, grade_1_basis_names, **opts
        )
        # import ipdb; ipdb.set_trace()
