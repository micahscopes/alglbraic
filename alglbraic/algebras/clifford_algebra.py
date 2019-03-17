from alglbraic.algebra import Algebra
from galgebra.ga import Ga
from functools import reduce

def build_basis_names(clifford_algebra, prefix='e', separator=''):
    Cl = clifford_algebra
    base = lambda indexes: prefix+separator+separator.join(str(i+1) for i in indexes)
    return [base(indexes) for indexes in Cl.indexes_lst]

class CliffordAlgebra(Algebra):
    def __init__(self, name, signature, *grade_1_basis, base_ring='float', unit='scalar'):
        self.Cl, *self._grade_1_basis = Ga.build(' '.join(grade_1_basis), g=signature)
        basis = [unit]+build_basis_names(self.Cl)
        Algebra.__init__(self, name, base_ring, *basis, unit=unit)

    def _algebraic_element_from_coefficients(self, coefficients):
        return self.Cl.mv(reduce(lambda u,v: u+v, [a*x for a,x in zip(coefficients, self.Cl.blades_lst0)],0))

    def _coefficients_from_algebraic_element(self, element):
        return element.blade_coefs()

    def reverse(self):
        result = self.algebraic_arguments(1).rev()
        return self.algebraic_operation('reverse', result, n=1)