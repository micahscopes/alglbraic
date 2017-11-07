from alglbraic import *
import sys

def vec(sym,m):
    return vector(SR, [var(sym+"%i" % (i%m+1)) for i in range(m)]);

Qs = "[-1,-1, -1]"
Q = [2*float(i) for i in Qs.strip("[]").split(",")]
m = Matrix.diagonal(Q)
q = QuadraticForm(m)

Alg = CliffordAlgebra(q)
dims = Alg.dimension()

A = Alg.from_vector(vec("a",dims))
B = Alg.from_vector(vec("b",dims))

AB = A*B
s = sympify

permutations = None
if(dims < 5):
    permutations = Permutations(dims)

product = VectorOperation("product",[s(A.coefficients()),s(B.coefficients())],s(AB.coefficients()))
vectorspace = VectorSpace(dims)
# flipper = SignFlipper(dims)

# conjugate = VectorOperation("conjugate",[s(A.vector())],s(A_conj.vector()))
# v.operations += [conjugate]

info = "Clifford Algebra with signature %s" % Qs
name="clifford%s" % Qs
