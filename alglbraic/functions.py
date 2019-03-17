from string import Template
from sympy import glsl_code

fn = Template("""\
$return_type $name($inputs){
    return $return_value;
}\
""")

def map(name, input_types, input_argnames, return_type, return_value):
    inputs = ', '.join(' '.join(type_name) for type_name in zip(input_types, input_argnames))
    
    if not isinstance(
        return_value, str):
        return_value = glsl_code(return_value)

    gl = fn.substitute({
      'name': name,
      'return_type': return_type,
      'return_value': return_value,
      'inputs': inputs
    })

    return gl

def operator(name, *args):
    input_types, input_argnames = [], []
    try:
        input_types, input_argnames = zip(*[i.split() for i in args[:-1]])
    except:
        pass
    return_type, return_value = args[-1]

    # print(input_types, input_argnames, return_type, return_value)

    return map(name, input_types, input_argnames, return_type, return_value)
    
def constant(name, return_value):
    return operator(name, return_value)

class OperationsMixin:
    A, B, C = ABC = ['a', 'b', 'c']
    U, V, W = UVW = ['u', 'v', 'w']
    X, Y, Z = XYZ = ['x', 'y', 'z']

    def symbolic_arguments(self, n=2):
        return [self.symbols_vector_for(arg) for arg in (self.UVW+self.XYZ)[:n]]

    def unary_operation(self, name, result, use_operators=False):
        input_types = [self.name]
        input_argnames = [self.U]
        return map(name, input_types, input_argnames, self.name, self.gl(result, use_operators=use_operators))

    def binary_operation(self, name, result, use_operators=False):
        input_types = [self.name]*2
        input_argnames = self.UVW
        return map(name, input_types, input_argnames, self.name, self.gl(result, use_operators=use_operators))

    def ternary_operation(self, name, result, use_operators=False):
        input_types = [self.name]*3
        input_argnames = self.UVW
        return map(name, input_types, input_argnames, self.name, self.gl(result, use_operators=use_operators))

