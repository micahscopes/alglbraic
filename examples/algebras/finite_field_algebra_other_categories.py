from alglbraic import *
import sys

def vec(sym,m,suff=""):
    return vector(SR, [var(sym+"%i%s" % (i%m+1,suff)) for i in range(m)]);

dim = 5
p = 3
f = FiniteField(p)
R = MatrixSpace(f,3)
cat = R.categories()[31]
print cat
F = FiniteField(dim)
f = F.algebra(SR,category=cat)
a = f.an_element()
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
flipper = SignFlipper(dim)

# conjugate = VectorOperation("conjugate",[s(A.vector())],s(A_conj.vector()))
# v.operations += [conjugate]

info = "Algebra of finite field of dimension %s" % dim
name="finite-field-algebra-alt-%s" % dim
