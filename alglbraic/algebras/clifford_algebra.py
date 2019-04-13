from alglbraic.algebra import Algebra
from galgebra.ga import Ga
from alglbraic import GLSL
from alglbraic.glsl import meta_glsl
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
        signature,
        *grade_1_basis,
        base_ring="float",
        unit="scalar",
        basis_names=None,
        **kwargs
    ):
        from sympy import symbols

        self.Cl, *self._grade_1_basis = Ga.build(
            "e", g=signature, coords=symbols(grade_1_basis)
        )
        basis_names = (
            [unit] + build_basis_names(self.Cl) if basis_names is None else basis_names
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


class ComplexNumbers(CliffordAlgebra):
    def __init__(self, name="C", base_ring="float", unit="real", **kwargs):
        CliffordAlgebra.__init__(
            self,
            name,
            [-1],
            "imag",
            basis_names=["real", "imag"],
            unit="real",
            base_ring=base_ring,
            **kwargs
        )
