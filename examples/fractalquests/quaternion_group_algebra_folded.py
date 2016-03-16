from sage.all import *
from alglbraic import *
from sympy import symbols, Symbol, sympify


G = QuaternionGroup()
GAlg = G.algebra(SR)
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
AB = Alg.retract(A.lift()*B.lift())
normA_coefs = vector(A.coefficients()).norm().combine()
antipode_coefs = Alg.retract(A.lift().antipode()).coefficients()
AB_coefs = AB.coefficients()
Ai = A.coefficients()
Bi = B.coefficients()
s = sympify
info = str(Alg)

formula = """
float MzA[N] = mutate(z,MA);
float MzB[N] = mutate(z,MB);
z = mul(
    pwr(flipA(z),pow1),
    pwr(flipB(z),pow2)
);
"""

###
permutations = Permutations(dim)
product = VectorOperation("product",[s(Ai),s(Bi)],s(AB_coefs))
antipode = VectorOperation("antipode",[s(Ai)],s(antipode_coefs))
v = VectorSpace(dim,product)
v.operations+=[antipode]
fractal = FractalQuest(v,info,permutations,formula=formula)
printer = GLSLPrinter()
file = "folded-quaternion-group-algebra.frag"

print("writing to %s" % file)
output = open(file, "w")
output.write(fractal.gl(printer))
output.close
