from alglbraic import *
import sys
def vec(sym,m):
    return vector(SR, [var(sym+"%i" % (i%m+1)) for i in range(m)]);

dim = ZZ.random_element(2,8)

FAlg = FreeAlgebra(SR,dim-1,'i')
F = FAlg.monoid()
gens = F.gens()
mons = [ F(1) ] + list(gens)
mats = []
for k in range(dim-1):
    m = matrix(ZZ,dim,dim,lambda i,j: ZZ.random_element(-1,1))
    mats.append(m)
RANDOM = FreeAlgebraQuotient(FAlg,mons,mats,vec("E",dim-1))
A=RANDOM(vec("a",dim))
B=RANDOM(vec("b",dim))
AB=A*B

info = "random, %s dimensional real algebra with multiplication: " % dim
info = info + str(A*B)

s = sympify

permutations = None
if(dim < 5):
    permutations = Permutations(dim)

product = VectorOperation("product",[s(A.vector()),s(B.vector())],s(AB.vector()))
vectorspace = VectorSpace(dim,product)

# conjugate = VectorOperation("conjugate",[s(A.vector())],s(A_conj.vector()))
# v.operations += [conjugate]

name="arbitrary-%s" % dim
