from sage.all import *
from alglbraic import *
from sympy import symbols, Symbol, sympify
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--fold",  action='store_true')
parser.add_argument("group",  action='store_true')
parser.add_argument("filename",nargs=1,default='some-hopf-algebra.py')
cli = parser.parse_args()

# G = WeylGroup(['A',2])
# G = GL(2,2)
# G = Sp(2,2)
# G = KleinFourGroup()
# G = QuaternionGroup()
G = SymmetricGroup(3)
# G = DiCyclicGroup(3)
# G = CyclicPermutationGroup(4)
# G = DihedralGroup(7)
# G = CyclicPermutationGroup(16)
# D1 = CyclicPermutationGroup(4)
# D2 = CyclicPermutationGroup(2)
# G = direct_product_permgroups([D1,D2])
# G = AlternatingGroup(4)
# G = CyclicPermutationGroup(13)
#### M16 group:
# G = PermutationGroup(gap_group=gap.new("AsPermGroup(SmallGroup(16,6))"))

#G = PermutationGroup(gap_group=gap.new("AsPermGroup(SmallGroup(16,3))"))

Alg = G.algebra(SR)
if(fold):
    o1 = [GAlg(l) for l in G.list() if l.order() == 1]
    o2 = [GAlg(l) for l in G.list() if l.order() == 2]
    o3up = [GAlg(l) for l in G.list() if l.order() > 2]
    O2 = [o1[0]+i for i in o2]
    O3 = [i+i.antipode() for i in o3up]
    Alg = GAlg.quotient_module(O2+O3)


###
dim = Alg.dimension()
syms = ("a","b")
As,Bs = [var(" ".join([s+str(i) for i in range(dim)])) for s in syms]
A = Alg.from_vector(vector(As))
B = Alg.from_vector(vector(Bs))
normA_coefs = vector(A.coefficients()).norm().combine()
antipode_coefs = A.antipode().coefficients()
AB_coefs = (A*B).coefficients()
Ai = A.coefficients()
Bi = B.coefficients()
s = sympify
info = str(Alg)


permutations = None
if(dim < 5):
    permutations = Permutations(dim)

product = VectorOperation("product",[s(Ai),s(Bi)],s(AB_coefs))
antipode = VectorOperation("antipode",[s(Ai)],s(antipode_coefs))
norm = VectorOperation("norm",[s(Ai)],s(normA_coefs))
v = VectorSpace(dim,product)
v.operations+=[norm,antipode]
fractal = FractalQuest(v,info,permutations)
printer = GLSLPrinter()
file = "some-hopf-algebra.frag"

print("writing to %s" % cli.file)
output = open(file, "w")
output.write(fractal.gl(printer))
output.close