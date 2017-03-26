from alglbraic import *
import sys

def vec(sym,m):
    return vector(SR, [var(sym+"%i" % (i%m+1)) for i in range(m)]);

Qs = "[1,1,-1,-1]"
Q = [2*float(i) for i in Qs.strip("[]").split(",")]
m = Matrix.diagonal(Q)
q = QuadraticForm(m)

Alg = CliffordAlgebra(q)
dim = Alg.dimension()

A = Alg.from_vector(vec("a",dim))
B = Alg.from_vector(vec("b",dim))

AB = A*B
s = sympify

permutations = None
if(dim < 5):
    permutations = Permutations(dim)

product = VectorOperation("product",[s(A.coefficients()),s(B.coefficients())],s(AB.coefficients()))
vectorspace = VectorSpace(dim,product)
# flipper = SignFlipper(dim)

# conjugate = VectorOperation("conjugate",[s(A.vector())],s(A_conj.vector()))
# v.operations += [conjugate]

info = "Clifford Algebra with signature %s" % Qs
name="clifford%s" % Qs
