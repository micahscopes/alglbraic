from alglbraic.finite_module import FiniteModule

class Algebra(FiniteModule):
    def __init__(self, *args, **kwargs):
        FiniteModule.__init__(self, *args, **kwargs)
        self.__init_algebra__(*args, **kwargs)

    def __init_algebra__(self, *args, **kwargs):
        pass

    def _algebraic_element_from_coefficients(self, name='x'):
        raise Exception("Be sure to override the `_algebraic_element_from_coefficients` method!")
    
    def _coefficients_from_algebraic_element(self, element):
        raise Exception("Be sure to override the `_coefficients_from_algebraic_element` method!")

    def algebraic_arguments(self, n=2):
        return [self._algebraic_element_from_coefficients(syms) for syms in self.symbolic_arguments(n)]

    def algebraic_product(self, name='product', fn=None, use_operators=False):
        fn = fn if fn else lambda u,v: u*v
        u,v = self.algebraic_arguments(2)
        result = self._coefficients_from_algebraic_element(fn(u,v))
        return self.binary_operation(name, result, use_operators=use_operators)

