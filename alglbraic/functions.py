from string import Template
from sympy import glsl_code

fn = Template("""\
$return_type $fn_name($inputs){
    return $return_value;
}\
""")

def map(fn_name, input_types, input_argnames, return_type, return_value, **kwargs):
    inputs = ', '.join(' '.join(type_name) for type_name in zip(input_types, input_argnames))
    
    if not isinstance(
        return_value, str):
        return_value = glsl_code(return_value)

    gl = fn.substitute({
      'fn_name': fn_name,
      'return_type': return_type,
      'return_value': return_value,
      'inputs': inputs
    })

    return gl

def operator(fn_name, *args, **kwargs):
    input_types, input_argnames = [], []
    try:
        input_types, input_argnames = zip(*[i.split() for i in args[:-1]])
    except:
        pass
    return_type, return_value = args[-1]

    # print(input_types, input_argnames, return_type, return_value)

    return map(fn_name, input_types, input_argnames, return_type, return_value, **kwargs)
    
def constant(fn_name, return_value, **kwargs):
    return operator(fn_name, return_value, **kwargs)

class OperationsMixin:
    A, B, C = ABC = ['a', 'b', 'c']
    U, V, W = UVW = ['u', 'v', 'w']
    X, Y, Z = XYZ = ['x', 'y', 'z']
    L, M, N = LMN = ['l', 'm', 'n']
    P, Q, R, S, T = PQRST = ['p', 'q', 'r', 's', 't']

    def symbolic_arguments(self, n=2):
        return [self.symbols_vector_for(arg) for arg in self.n_ary_argnames(n)]

    def n_ary_argnames(self, n=2):
        return (self.UVW+self.PQRST+self.LMN+self.XYZ)[:n]

    def n_ary_operation(self, n, fn_name, result, use_operators=False):
        input_types = [self.type_name]*n
        input_argnames = [str(x) for x in self.n_ary_argnames(n)]
        return map(fn_name, input_types, input_argnames, self.type_name, self.gl(result, use_operators=use_operators))

    def unary_operation(self,*args,**kwargs): return self.n_ary_operation(1,*args,**kwargs)
    def binary_operation(self,*args,**kwargs): return self.n_ary_operation(2,*args,**kwargs)
    def ternary_operation(self,*args,**kwargs): return self.n_ary_operation(3,*args,**kwargs)
    def quaternary_operation(self,*args,**kwargs): return self.n_ary_operation(4,*args,**kwargs)