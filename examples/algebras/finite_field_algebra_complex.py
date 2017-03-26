from alglbraic import *
import sys

def vec(sym,m,suff=""):
    return vector(SR, [var(sym+"%i%s" % (i%m+1,suff)) for i in range(m)]);
def complexVec(sym,dim):
    reals = vec(sym,dim,suff="_re")
    imags = vec(sym,dim,suff="_im")
    return zip(reals,imags)

dim = 3
F = FiniteField(dim)
Al = F.algebra(SR,category=Semigroups())

Asyms = complexVec("a",dim)
Bsyms = complexVec("b",dim)
As = [v[0]+v[1]*I for v in Asyms]
Bs = [v[0]+v[1]*I for v in Bsyms]
Asubs = {}
Bsubs = {}

Asyms = flatten(Asyms)
Bsyms = flatten(Bsyms)
for a in Asyms:
    Asubs[imag_part(a)] = 0
    Asubs[real_part(a)] = a
for a in Bsyms:
    Asubs[imag_part(a)] = 0
    Asubs[real_part(a)] = a

A = Al.from_vector(vector(As))
B = Al.from_vector(vector(Bs))
AB_coefs = (A*B).coefficients()
for ab in AB_coefs:
    real(ab).substitute(Asubs).substitute(Bsubs)
AB_real = map(lambda ab: ab.real(),AB_coefs)
AB_imag = map(lambda ab: ab.imag(),AB_coefs)

AB_coefs = map(lambda ab: (ab).substitute(Asubs).substitute(Bsubs),flatten(zip(AB_real,AB_imag)))
s = sympify

permutations = None
if(2*dim < 5):
    permutations = Permutations(dim*2)

product = VectorOperation("product",[s(Asyms),s(Bsyms)],s(AB_coefs))
vectorspace = VectorSpace(2*dim,product)

info = "%s real-dimensional algebra of %s dimensional finite field over the complex numbers" % (2*dim,dim)
name="finite-field-algebra-%s-complex" % dim
dim = 2*dim