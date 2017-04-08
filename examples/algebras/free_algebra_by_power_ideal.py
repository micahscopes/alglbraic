from alglbraic import *
import sys

def vec(sym,m,suff=""):
    return vector(SR, [var(sym+"%i%s" % (i%m+1,suff)) for i in range(m)]);

dim = 2
from sage.rings.noncommutative_ideals import Ideal_nc
from itertools import product
class PowerIdeal(Ideal_nc):
    def __init__(self, R, n):
        self._power = n
        self._power = n
        Ideal_nc.__init__(self, R, [R.prod(m) for m in product(R.gens(), repeat=n)])
    def reduce(self,x):
        R = self.ring()
        return add([c*R(m) for m,c in x if len(m)<self._power],R(0))

F = FreeAlgebra(QQ, dim)
I3 = PowerIdeal(F,3); I3
f = F.quo(I3);

dim = f.dimension()

X = vec('x',dim)
Y = vec('y',dim)

X = f.from_vector(X)
Y = f.from_vector(Y)

s = sympify

permutations = None
if(dim < 5):
    permutations = Permutations(dim)

product = VectorOperation("product",[s(X.coefficients()),s(Y.coefficients())],s((X*Y).coefficients()))
vectorspace = VectorSpace(dim,product)

info = " %s-dimensional quotient of %s variable polynomial ring mod %s" % (N,dim,String(ideal))
name="%s-var-polynomial-ring-mod-%s" % (N,String(ideal))
