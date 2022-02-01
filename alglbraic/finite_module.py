from sympy import Symbol, symbols, glsl_code, sympify, IndexedBase
from string import Template
from alglbraic.glsl import GlslStruct, GLSL, StructElement
from alglbraic import glsl_snippet
from alglbraic.functions import map as gl_map, OperationsMixin
from collections.abc import Iterable

ZERO = "ZERO"
ONE = "ONE"
SCALAR = "scalar"

class FiniteModule(GlslStruct, OperationsMixin):
    """A glsl_snippet helper class for a finite module over some ring.
    """

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
        # todo: pull this stuff out into a module with helpers to share conventions
        self.ZERO = self.typed_name(ZERO)
        self.ONE = self.typed_name(ONE)
        self.SCALAR = self.typed_name(SCALAR)

    def gl(self, expr, use_operators=False, element_type=None):
        def to_float(x):
            return sympify(x).evalf() if x != 0 else 0.0

        if self.base_ring == "float" or True:
            if isinstance(expr, Iterable):
                expr = [to_float(co) for co in expr]
            else:
                expr = to_float(expr)

        element_type = element_type if element_type else self.type_name

        def pow_func(b, e):
            e = int(float(e))
            if e == 1:
                return b
            if e == 2:
                return '{}({})'.format(self.mul_fn, ', '.join([b]*e))

            return '{}({}, {})'.format(self.mul_fn, b, pow_func(b, e-1))

        result = glsl_code(
            StructElement(element_type, expr),
            glsl_types=False,
            use_operators=use_operators
            or self.base_ring == "float"
            or self.base_ring == "int",
            zero=self.base_zero(),
            user_functions={'pow': [
                (lambda args: float(args[1]).is_integer() and float(args[1]) < 42, pow_func),
                (lambda args: not float(args[1]).is_integer(), 'wow')
                ]} if self.base_ring != "float" and self.base_ring != "int" else {}
        )
        # a hack to ensure base elements are used instead of floats; makes assumptions
        return result if self.base_ring == "float" or self.base_ring == "int" else result.replace("0.0", str(self.base_zero())).replace("1.0", str(self.base_one()))

    def base_zero(self):
        if self.base_ring == "float":
            return sympify(0.0)
        elif self.base_ring == "int":
            return sympify(0)
        else:
            return Symbol(self.typed_name(ZERO, self.base_ring))

    def zero_symbols(self):
        return [self.base_zero()] * len(self.basis)

    def base_one(self):
        if self.base_ring == "float":
            return sympify(1.0)
        elif self.base_ring == "int":
            return sympify(1)
        else:
            return Symbol(self.typed_name(ONE, self.base_ring))

    @GLSL
    def zero(self, function_name=None, **kwargs):
        function_name = function_name if function_name else self.ZERO
        module_zero = self.gl(self.zero_symbols())
        return self.constant(function_name, module_zero, **kwargs)

    def one_symbols(self):
        if self.unit is None:
            raise Exception("No unit is defined")
        one = [self.base_zero()] * len(self.basis)
        one[self.basis.index(self.unit)] = self.base_one()
        return one

    @GLSL
    def one(self, function_name=None, **kwargs):
        function_name = function_name if function_name else self.ONE
        one = self.gl(self.one_symbols())
        return self.constant(function_name, one, **kwargs)

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

    @GLSL(depends_on=["scalar_base_mul"])
    def scalar_float_mul(self, function_name=mul_fn):
        return (
            glsl_snippet(
                Template(
                    """\
$type $fn(float a, $type X){
    return mul(mul(a, $ONE), X);
}"""
                ).substitute(
                    type=self.type_name, ONE=str(self.base_one()), fn=function_name
                )
            )
            if self.base_ring != "float" and self.base_ring != "int"
            else ""
        )

    @GLSL(depends_on=["scalar_float_mul"])
    def scalar(self, function_name=None):
        function_name = function_name if function_name else self.SCALAR
        return (
            glsl_snippet(
                Template(
                    """\
$type $fn(float a){
    return mul(a, $ONE);
}"""
                ).substitute(
                    type=self.type_name, ONE=self.ONE, fn=function_name
                )
            )
        )

    @GLSL
    def scalar_base_mul(self, function_name=mul_fn):
        type_name = self.type_name
        base_ring = self.base_ring
        a = Symbol(self.A)
        x = self.symbols_vector_for(self.X.upper())
        input_types = [base_ring, type_name]
        input_argnames = [self.A, self.X.upper()]
        return gl_map(
            function_name, input_types, input_argnames, self.type_name, self.gl(a * x)
        )

    @GLSL(depends_on=["scalar_base_mul"])
    def scalar_int_mul(self, function_name=mul_fn, **kwargs):
        return glsl_snippet(
            Template(
                """\
$type $fn(int a, $type X){
    return mul(float(a), X);
}"""
            ).substitute(type=self.type_name, fn=function_name)
        )

    @GLSL(depends_on=["scalar"])
    def build_from_float_array(self, name="fromArray", separator=", "):
        if self.base_ring == "float":
            return ""
        if not self.uniform_member_type:
            raise TypeError(
                "To generate an array constructor, GlslStruct must have members of\
                uniform type"
            )

        template = Template(
            """\
$type_name $fn_name(float X[$size]){
    return $type_name($array_members);
}"""
        )

        x = IndexedBase("X")
        array_members = separator.join(["{}({})".format(self.typed_name(SCALAR, self.base_ring), str(x[i])) for i in range(len(self))])
        return template.substitute(
            fn_name=name,
            type_name=self.type_name,
            base_type=self.uniform_member_type,
            array_members=array_members,
            size=len(self),
        )