from sympy import Symbol, Matrix, symbols, glsl_code
from string import Template
from alglbraic.struct import GlslStruct
from alglbraic.functions import constant, operator, map as gl_map, OperationsMixin


class FiniteModule(GlslStruct, OperationsMixin):
    """A GLSL helper class for a finite module over some ring.
    """

    base_ring_zero = "zero_base()"
    base_ring_one = "one_base()"

    def __init__(self, name, base_ring, *basis, unit=None):

        """A Finite Module.

        Keyword arguments:
        name -- the type name of this module
        base_ring -- the type name of this module's base ring
        *basis -- names of basis members
        unit -- the name of the unit member (default None)
        use_operators -- whether or not to generate GLSL using operators (default False)
        """

        basis_declarations = [base_ring + " " + b for b in basis]
        GlslStruct.__init__(self, name, *basis_declarations)
        self.base_ring = base_ring
        self.basis = basis
        self.unit = unit

    def gl(self, expr, use_operators=False):
        return glsl_code(
            expr,
            array_constructor=self.name,
            glsl_types=False,
            use_operators=use_operators,
        )

    def zero_symbols(self):
        return symbols([self.base_ring_zero] * len(self.basis))

    def zero(self):
        module_zero = self.gl(self.zero_symbols())
        return constant("zero", (self.name, module_zero))

    def one_symbols(self):
        if self.unit == None:
            raise Exception("No unit is defined")
        one = [Symbol(self.base_ring_zero)] * len(self.basis)
        one[self.basis.index(self.unit)] = Symbol(self.base_ring_one)
        return one

    def one(self):
        one = self.gl(self.one_symbols())
        return constant("one", (self.name, one))

    def add(self):
        u, v = self.symbolic_arguments(2)
        return self.binary_operation("add", u + v)

    def sub(self):
        u, v = self.symbolic_arguments(2)
        return self.binary_operation("sub", u - v)

    def scalar_int_mul(self):
        return Template(
            """\
$name mul(int a, $name x){
    return mul(float(a), x);
}"""
        ).substitute(name=self.name)

    def scalar_float_mul(self):
        return Template(
            """\
$name mul(float a, $name x){
    return mul(mul(a, $base_ring_one), x);
}"""
        ).substitute(name=self.name, base_ring_one=self.base_ring_one)

    def scalar_base_mul(self):
        name = self.name
        base_ring = self.base_ring
        a = Symbol(self.A)
        x = self.symbols_vector_for(self.X)
        input_types = [base_ring, name]
        input_argnames = [self.A, self.X]
        return gl_map("mul", input_types, input_argnames, self.name, self.gl(a * x))

