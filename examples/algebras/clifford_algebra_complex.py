from alglbraic import *
import sys

def vec(sym,m,suff=""):
    return vector(SR, [var(sym+"%i%s" % (i%m+1,suff)) for i in range(m)]);
def complexVec(sym,dim):
    reals = vec(sym,dim,suff="_re")
    imags = vec(sym,dim,suff="_im")
    return zip(reals,imags)

Qs = "[-1,0,1]"
Q = [i for i in Qs.strip("[]").split(",")]

Q = QuadraticForm(CC,2,Q)
Al = CliffordAlgebra(Q)
Asyms = complexVec("a",dim(Al))
Bsyms = complexVec("b",dim(Al))
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

dim = Al.dimension()*2
permutations = None
if(dim < 5):
    permutations = Permutations(dim)

product = VectorOperation("product",[s(Asyms),s(Bsyms)],s(AB_coefs))
vectorspace = VectorSpace(dim,product)
# flipper = SignFlipper(dim)

# conjugate = VectorOperation("conjugate",[s(A.vector())],s(A_conj.vector()))
# v.operations += [conjugate]

info = "Clifford Algebra with signature %s" % Qs
name="clifford-complex%s" % Qs
