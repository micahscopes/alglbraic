from sympy import Symbol, symbols, glsl_code, sympify
from string import Template
from alglbraic.glsl import GlslStruct, GLSL, StructElement
from alglbraic import glsl_snippet
from alglbraic.functions import constant, map as gl_map, OperationsMixin
from collections.abc import Iterable


class FiniteModule(GlslStruct, OperationsMixin):
    """A glsl_snippet helper class for a finite module over some ring.
    """

    zero_fn = "zero"
    one_fn = "one"
    mul_fn = "mul"
    add_fn = "add"
    sub_fn = "sub"

    def __init__(self, type_name, base_ring, *basis, unit=None):

        """A Finite Module.

        Keyword arguments:
        type_name -- the type name of this module
        base_ring -- the type name of this module's base ring
        *basis -- names of basis members
        unit -- the name of the unit member (default None)
        use_operators -- whether or not to generate glsl_snippet using operators (default False)
        """

        basis_declarations = [base_ring + " " + b for b in basis]
        GlslStruct.__init__(self, type_name, *basis_declarations)
        self.base_ring = base_ring
        self.basis = basis
        self.unit = unit

    def gl(self, expr, use_operators=False, element_type=None):
        def to_float(x):
            return sympify(x).evalf() if x != 0 else 0.0

        if self.base_ring == "float":
            if isinstance(expr, Iterable):
                expr = [to_float(co) for co in expr]
            else:
                expr = to_float(expr)

        element_type = element_type if element_type else self.type_name

        # import ipdb;ipdb.set_trace()
        return glsl_code(
            StructElement(element_type, expr),
            glsl_types=False,
            use_operators=use_operators
            or self.base_ring == "float"
            or self.base_ring == "int",
            zero=self.zero_fn + "()",
        )

    def base_zero(self):
        if self.base_ring == "float":
            return sympify(0.0)
        elif self.base_ring == "int":
            return sympify(0)
        else:
            return Symbol(self.zero_fn + "()")

    def zero_symbols(self):
        return [self.base_zero()] * len(self.basis)

    def base_one(self):
        if self.base_ring == "float":
            return sympify(1.0)
        elif self.base_ring == "int":
            return sympify(1)
        else:
            return Symbol(self.one_fn + "()")

    @GLSL
    def zero(self, function_name=zero_fn, **kwargs):
        module_zero = self.gl(self.zero_symbols())
        return constant(function_name, (self.type_name, module_zero), **kwargs)

    def one_symbols(self):
        if self.unit is None:
            raise Exception("No unit is defined")
        one = [self.base_zero()] * len(self.basis)
        one[self.basis.index(self.unit)] = self.base_one()
        return one

    @GLSL
    def one(self, function_name=one_fn, **kwargs):
        one = self.gl(self.one_symbols())
        return constant(function_name, (self.type_name, one), **kwargs)

    @GLSL
    def add(self, function_name=add_fn, **kwargs):
        u, v = self.symbolic_arguments(2)
        return self.binary_operation(function_name, u + v, **kwargs)

    @GLSL
    def add_3(self, function_name=add_fn, **kwargs):
        u, v, w = self.n_ary_argnames(3)
        result = "%s(%s(%s, %s), %s)" % (function_name, function_name, u, v, w)
        return self.ternary_operation(function_name, result, **kwargs)

    @GLSL
    def add_4(self, function_name=add_fn, **kwargs):
        u, v, w, x = self.n_ary_argnames(4)
        result = "%s(%s(%s(%s, %s), %s), %s)" % (
            function_name,
            function_name,
            function_name,
            u,
            v,
            w,
            x,
        )
        return self.quaternary_operation(function_name, result, **kwargs)

    @GLSL
    def sub(self, function_name=sub_fn, **kwargs):
        u, v = self.symbolic_arguments(2)
        return self.binary_operation(function_name, u - v, **kwargs)

    @GLSL
    def scalar_float_mul(self, function_name=mul_fn):
        return (
            glsl_snippet(
                Template(
                    """\
$type $fn(float a, $type x){
    return mul(mul(a, $one_fn), x);
}"""
                ).substitute(
                    type=self.type_name, one_fn=str(self.base_one()), fn=function_name
                )
            )
            if self.base_ring != "float" and self.base_ring != "int"
            else ""
        )

    @GLSL(depends_on=["scalar_float_mul"])
    def scalar_base_mul(self, function_name=mul_fn):
        type_name = self.type_name
        base_ring = self.base_ring
        a = Symbol(self.A)
        x = self.symbols_vector_for(self.X)
        input_types = [base_ring, type_name]
        input_argnames = [self.A, self.X]
        return gl_map(
            function_name, input_types, input_argnames, self.type_name, self.gl(a * x)
        )

    @GLSL(depends_on=["scalar_base_mul"])
    def scalar_int_mul(self, function_name=mul_fn, **kwargs):
        return glsl_snippet(
            Template(
                """\
$type $fn(int a, $type x){
    return mul(float(a), x);
}"""
            ).substitute(type=self.type_name, fn=function_name)
        )
