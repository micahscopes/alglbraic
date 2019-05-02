from string import Template
from sympy import glsl_code
from . import glsl_snippet

fn = Template(
    """\
$return_type $function_name($inputs){
    return $return_value;
}\
"""
)


def map(
    function_name, input_types, input_argnames, return_type, return_value, **kwargs
):
    inputs = ", ".join(
        " ".join(type_name) for type_name in zip(input_types, input_argnames)
    )

    if not isinstance(return_value, str):
        return_value = glsl_code(return_value)

    gl = fn.substitute(
        {
            "function_name": function_name,
            "return_type": return_type,
            "return_value": return_value,
            "inputs": inputs,
        }
    )

    return glsl_snippet(gl)


def operator(function_name, *args, **kwargs):
    try:
        input_types, input_argnames = zip(*[i.split() for i in args[:-1]])
    except ValueError:
        input_types, input_argnames = [], []

    return_type, return_value = args[-1]

    # print(input_types, input_argnames, return_type, return_value)

    return glsl_snippet(
        map(
            function_name,
            input_types,
            input_argnames,
            return_type,
            return_value,
            **kwargs
        )
    )


def constant(function_name, return_value, **kwargs):
    return operator(function_name, return_value, **kwargs)


class OperationsMixin(object):
    A, B, C = ABC = ["a", "b", "c"]
    U, V, W = UVW = ["u", "v", "w"]
    X, Y, Z = XYZ = ["x", "y", "z"]
    L, M, N = LMN = ["l", "m", "n"]
    P, Q, R, S, T = PQRST = ["p", "q", "r", "s", "t"]
    type_name = NotImplemented

    def gl(self, *args, **kwargs):
        return NotImplemented

    def symbolic_arguments(self, n=2):
        return [self.symbols_vector_for(arg) for arg in self.n_ary_argnames(n)]

    def n_ary_argnames(self, n=2):
        return (self.UVW + self.PQRST + self.LMN + self.XYZ)[:n]

    def n_ary_operation(self, n, function_name, result, use_operators=False):
        input_types = [self.type_name] * n
        input_argnames = [str(x) for x in self.n_ary_argnames(n)]
        return map(
            function_name,
            input_types,
            input_argnames,
            self.type_name,
            self.gl(result, use_operators=use_operators) if not isinstance(result, str) else result,
        )

    def unary_operation(self, function_name, result, **kwargs):
        return self.n_ary_operation(1, function_name, result, **kwargs)

    def binary_operation(self, function_name, result, **kwargs):
        return self.n_ary_operation(2, function_name, result, **kwargs)

    def ternary_operation(self, function_name, result, **kwargs):
        return self.n_ary_operation(3, function_name, result, **kwargs)

    def quaternary_operation(self, function_name, result, **kwargs):
        return self.n_ary_operation(4, function_name, result, **kwargs)
