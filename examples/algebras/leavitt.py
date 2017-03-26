DIR = os.path.dirname(os.path.realpath(__file__))
load('%s/../algebras/lpa.py'%DIR)
from alglbraic import *

complex = True

rels = {"a":["c"],"c":["a","b"]}
#rels = {"a":["b","c","d"],"d":["d","b"],"b":["c","d"],}
G = DiGraph(rels)
A,B,AB = LeavittPathAlg(G,complex)

print len(A), A
print len(B), B
print len(AB), AB

dim = len(A)

info = "leavitt path algebra of with dimension %s, for graph" % dim
info = info + str(AB)

s = sympify
permutations = None
if(dim < 5):
    permutations = Permutations(dim)

product = VectorOperation("product",[s(A),s(B)],s(AB))
vectorspace = VectorSpace(dim,product)

# conjugate = VectorOperation("conjugate",[s(A.vector())],s(A_conj.vector()))
# v.operations += [conjugate]

name="lpa-%s%s" % ("complex-" if complex else "", str(rels))
