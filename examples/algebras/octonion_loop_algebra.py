from sage.all import *
DIR = os.path.dirname(os.path.realpath(__file__))
load(DIR+"/../algebras/octonions.sage")
from alglbraic import *
from sympy import symbols, Symbol, sympify
from subprocess import call

gap.load_package("loops")

def vec(sym,m):
    return vector(SR, [var(sym+"%i" % (i%m)) for i in range(m)]);

loop="MoufangLoop(16,3)"
#loop="InterestingLoop(32,1)"
multiplication = gap("CayleyTable(%s)"%loop)
subloops = list(gap("AllSubloops(%s);"%loop))
#gap.Elements(subloops[15])
#multiplication = gap("CayleyTable(InterestingLoop(32,1))")
elements = list(gap("Elements(%s)"%loop))
dim = len(elements)
loopOne = str(gap("One(%s)"%loop))
loopElements = [str(l) for l in elements]
loopInverses = [str(e.LeftInverse()) for e in elements]
inverses = [loopElements.index(l) for l in loopInverses]
subloopsElements = [[str(el) for el in sl.Elements()] for sl in subloops]
#subloopIndices = [[loopElements.index(el) for el in loop] for loop in subloopsElements]

cay = matrix(ZZ,multiplication).apply_map(lambda x: x-1)
dim = cay.dimensions()[0]
mats = []
for i in range(dim):
    mul = matrix(ZZ,dim,dim)
    for j in range(dim):
        mul[j,cay[i][j]] = 1
    mats.append(mul)

al = FiniteDimensionalAlgebra(SR,mats)
ideals = []
one = al.term(0)
for i in range(dim):
    el = al.term(i)
    inv = al.term(inverses[i])
    if(el == one):
        continue
        ideal = el-one
    if(el == inv):
        continue
        ideal = el+one
    else:
        ideal = el+inv
    ideals.append(ideal)
ideal = al.ideal(ideals)
quoMap = al.quotient_map(ideal)
quo = quoMap.codomain()
dim = quo.degree()

A = quo(vec("a",8))
B = quo(vec("b",8))
Aco = A.coefficients()
Bco = B.coefficients()
AB = A*B
ABco = AB.coefficients()
s = sympify

permutations = None
if(dim < 5):
    permutations = Permutations(dim)

product = VectorOperation("product",[s(Aco),s(Bco)],s(ABco))
v = VectorSpace(dim,product)

#conjugate = VectorOperation("conjugate",[s(Aco)],s(A.si().L))
#v.operations += [conjugate]
vectorspace = v
info = "octonion from gap Moufang Loop (16,3)"
name = "MoufangLoop(16,3)"
