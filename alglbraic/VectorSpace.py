from fragments import *
from sympy import Symbol, symbols
from string import Template

class VectorSpace(Fragment):
    def __init__(self, dimensions, size_const='N'):
        Fragment.__init__(self)
        self.size_const = size_const
        self.N = dimensions

    def upper(self):
        return 'const int %s = %s;' % (self.size_const,self.N)

    def lower(self):
        return vectorBasics.substitute(N=self.size_const)

vectorBasics = Template('''
float[$N] zero$N() {
  float zero[$N];
  for(int i=0; i<$N; ++i){zero[i] = 0;}
  return zero;
}

float[$N] unit$N(int i) {
  float[$N] unit = zero$N();
  unit[i] = 1;
  return unit;
}

float[$N] add(float a[$N], float b[$N]) {
  float c[$N];
  for (int i = 0; i < $N; ++i){
    c[i] = a[i]+b[i];
  }
  return c;
}

float[$N] sub(float a[$N], float b[$N]) {
  float c[$N];
  for (int i = 0; i < $N; ++i){
    c[i] = a[i]-b[i];
  }
  return c;
}

''')