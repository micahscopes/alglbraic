from alglbraic.finite_module import FiniteModule
from alglbraic import GLSL
from alglbraic.glsl import meta_glsl


class Algebra(FiniteModule):
    def __init__(self, *args, **kwargs):
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

    def algebraic_operation(self, name, result, n=2, use_operators=False) -> GLSL:
        if not isinstance(result, str):
            result = self._coefficients_from_algebraic_element(result)
        return self.n_ary_operation(n, name, result, use_operators=use_operators)

    @meta_glsl(depends_on=['definition'])
    def algebraic_product(self, name=None, fn=None, use_operators=False) -> GLSL:
        name = name if name else self.mul_fn
        fn = fn if fn else lambda u, v: u * v
        u, v = self.algebraic_arguments(2)
        result = self._coefficients_from_algebraic_element(fn(u, v))
        return self.binary_operation(name, result, use_operators=use_operators)
