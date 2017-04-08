from sage.all import *
DIR = os.path.dirname(os.path.realpath(__file__))
load(DIR+"/../algebras/octonions.sage")
from alglbraic import *
from sympy import symbols, Symbol, sympify
from subprocess import call

dim = 8
def vec(sym,m):
    return vector(SR, [var(sym+"%i" % (i%m+1)) for i in range(m)]);

o = octonion_parent(SR)
A = octonion(vec("a",8),o)
B = octonion(vec("b",8),o)
C = octonion(vec("c",8),o)

AB = A*B
s = sympify

permutations = None
if(dim < 5):
    permutations = Permutations(dim)

conjugate = VectorOperation("conjugate",[s(A.L)],s(A.si().L))
product = AlgebraicProduct([s(A.L),s(B.L)],s(AB.L))+conjugate
v = VectorSpace(dim)

vectorspace = v
info = "octonion algebra fractal!!!"
name = "octonions"
