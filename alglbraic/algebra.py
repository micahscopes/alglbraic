from alglbraic.finite_module import FiniteModule
from alglbraic import glsl_snippet
from alglbraic.glsl import GLSL


class Algebra(FiniteModule):
    def __init__(self, *args, associative=True, **kwargs):
        self.associative = associative
        FiniteModule.__init__(self, *args, **kwargs)
        self.__init_algebra__(*args, **kwargs)

    def __init_algebra__(self, *args, **kwargs):
        pass

    def _algebraic_element_from_coefficients(self, name="x"):
        raise NotImplementedError(
            "Be sure to override the `_algebraic_element_from_coefficients` method!"
        )

    def _coefficients_from_algebraic_element(self, element):
        raise NotImplementedError(
            "Be sure to override the `_coefficients_from_algebraic_element` method!"
        )

    def algebraic_arguments(self, n=2):
        args = [
            self._algebraic_element_from_coefficients(syms)
            for syms in self.symbolic_arguments(n)
        ]
        if len(args) > 1:
            return args
        else:
            return args[0]

    def algebraic_operation(self, name, result, n=2, use_operators=False):
        if not isinstance(result, str):
            result = self._coefficients_from_algebraic_element(result)
        return self.n_ary_operation(n, name, result, use_operators=use_operators)

    @GLSL(depends_on=['definition'])
    def algebraic_product(self, name=None, fn=None, use_operators=False):
        name = name if name else self.mul_fn
        fn = fn if fn else lambda u, v: u * v
        u, v = self.algebraic_arguments(2)
        result = self._coefficients_from_algebraic_element(fn(u, v))
        return self.binary_operation(name, result, use_operators=use_operators)

    @GLSL(depends_on=[algebraic_product])
    def algebraic_product_3(self, name=None, **kwargs):
        if not self.associative:
            return None
        name = name if name else self.mul_fn
        p, q, r = self.n_ary_argnames(3)
        result = '%s(%s(%s, %s), %s)' % (name, name, p, q, r)
        return self.algebraic_operation(name, result, n=3, **kwargs)

