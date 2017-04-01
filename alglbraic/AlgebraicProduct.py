from alglbraic import Composition, VectorOperation, Fragment
from string import Template

Power = Template('''
float[$N] ${fn}Pwr(float a[$N],int n) {
  // multiple a by itself n times: a -> a**n
	float r[$N] = a;
	for (int i=0;i<n-1;i++){
	   r = $fn(r,a);
    }
    return r;
}
''')

ThreeFn = Template('''
float[$N] ${fn}3(float a[$N], float b[$N], float c[$N]) {
  return $fn($fn(a,b),c);
}''')

ScalarFn = Template('''
float[$N] $fn(float a, float b[$N]){
  float result[$N];
  for (int i = 0; i < $N; ++i){
    result[i] = a*b[i];
  }
  return result;
}

float[$N] $fn(float b[$N], float a) {
  return $fn(a,b);
}

float[$N] $fn(int a, float b[$N]) {
  return $fn(float(a),b);
}

float[$N] $fn(float b[$N], int a) {
  return $fn(float(a),b);
}
''')

class AlgebraicProduct(Composition):
    def __init__(self,vectors, results, name='mul', size_const = "N", associative=True, symbols=['u','v'], functionTemplate=None):
        # these are split out to make it easier for generalizing to n-ary 'products' down the line, which won't be associative or have obvious 'power' functions 
        aux = ScalarFn.substitute(N=size_const,fn=name)
        if associative:
            aux+= Power.substitute(N=size_const,fn=name)
            aux+= ThreeFn.substitute(N=size_const,fn=name)
        aux = Fragment(lower=aux)
        op = VectorOperation(name, vectors, results, symbols=symbols, result_size_const = size_const, functionTemplate=functionTemplate)
        Composition.__init__(self,[op,aux])
        
        
        
        
        
        
