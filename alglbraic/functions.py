from string import Template
from sympy import glsl_code

fn = Template("""\
$return_type $name($inputs){
    return $return_value
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

    print(input_types, input_argnames, return_type, return_value)

    return map(name, input_types, input_argnames, return_type, return_value)
    
def constant(name, return_value):
    return operator(name, return_value)


# Power = Template('''
# float[$N] ${fn}Pwr(float a[$N],int n) {
#   // multiple a by itself n times: a -> a**n
# 	float r[$N] = a;
# 	for (int i=0;i<n-1;i++){
# 	   r = $fn(r,a);
#     }
#     return r;
# }
# ''')

# ThreeFn = Template('''
# float[$N] ${fn}3(float a[$N], float b[$N], float c[$N]) {
#   return $fn($fn(a,b),c);
# }''')

# ScalarFn = Template('''
# float[$N] $fn(float a, float b[$N]){
#   float result[$N];
#   for (int i = 0; i < $N; ++i){
#     result[i] = a*b[i];
#   }
#   return result;
# }

# float[$N] $fn(float b[$N], float a) {
#   return $fn(a,b);
# }

# float[$N] $fn(int a, float b[$N]) {
#   return $fn(float(a),b);
# }

# float[$N] $fn(float b[$N], int a) {
#   return $fn(float(a),b);
# }
# ''')
        
        
        
        
        
