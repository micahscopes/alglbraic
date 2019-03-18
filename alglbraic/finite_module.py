from sympy import Symbol, Matrix, symbols, glsl_code
from string import Template
from alglbraic.struct import GlslStruct
from alglbraic.functions import constant, operator, map as gl_map, OperationsMixin

def test_decorator(func):
    print("evaluating for "+str(func))
    return func
class FiniteModule(GlslStruct, OperationsMixin):
    """A GLSL helper class for a finite module over some ring.
    """

    base_ring_zero = "zero()"
    base_ring_one = "one()"
    mul_fn_name = "mul"
    add_fn_name = "add"
    sub_fn_name = "sub"

    def __init__(self, type_name, base_ring, *basis, unit=None):

        """A Finite Module.

        Keyword arguments:
        type_name -- the type name of this module
        base_ring -- the type name of this module's base ring
        *basis -- names of basis members
        unit -- the name of the unit member (default None)
        use_operators -- whether or not to generate GLSL using operators (default False)
        """

        basis_declarations = [base_ring + " " + b for b in basis]
        GlslStruct.__init__(self, type_name, *basis_declarations)
        self.base_ring = base_ring
        self.basis = basis
        self.unit = unit

    def gl(self, expr, use_operators=False):
        return glsl_code(
            expr,
            array_constructor=self.type_name,
            glsl_types=False,
            use_operators=use_operators,
        )

    def zero_symbols(self):
        return symbols([self.base_ring_zero] * len(self.basis))

    def zero(self, **kwargs):
        module_zero = self.gl(self.zero_symbols())
        return constant("zero", (self.type_name, module_zero), **kwargs)
        
    @test_decorator
    def one_symbols(self):
        if self.unit == None:
            raise Exception("No unit is defined")
        one = [Symbol(self.base_ring_zero)] * len(self.basis)
        one[self.basis.index(self.unit)] = Symbol(self.base_ring_one)
        return one

    def one(self, **kwargs):
        one = self.gl(self.one_symbols())
        return constant("one", (self.type_name, one), **kwargs)

    def add(self, **kwargs):
        u, v = self.symbolic_arguments(2)
        return self.binary_operation("add", u + v, **kwargs)

    def sub(self, **kwargs):
        u, v = self.symbolic_arguments(2)
        return self.binary_operation("sub", u - v, **kwargs)

    def scalar_int_mul(self, fn_name=None, **kwargs):
        fn_name = self.mul_fn_name if not fn_name else fn_name
        return Template(
            """\
$type $fn(int a, $type x){
    return mul(float(a), x);
}"""
        ).substitute(type=self.type_name, fn=fn_name)

    def scalar_float_mul(self, fn_name=None):
        fn_name = self.mul_fn_name if not fn_name else fn_name
        return Template(
            """\
$type $fn(float a, $type x){
    return mul(mul(a, $base_ring_one), x);
}"""
        ).substitute(type=self.type_name, base_ring_one=self.base_ring_one, fn=fn_name)

    def scalar_base_mul(self, fn_name=None):
        fn_name = self.mul_fn_name if not fn_name else fn_name
        type_name = self.type_name
        base_ring = self.base_ring
        a = Symbol(self.A)
        x = self.symbols_vector_for(self.X)
        input_types = [base_ring, type_name]
        input_argnames = [self.A, self.X]
        return gl_map(fn_name, input_types, input_argnames, self.type_name, self.gl(a * x))

