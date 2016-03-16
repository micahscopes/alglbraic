from alglbraic import *
import sys
A = FreeAlgebra(SR,3,'i')
F = A.monoid()
i,j,k = F.gens()
mons = [ F(1), i, j, k ]
M = MatrixSpace(SR,4)
mats = [M([0,1,0,0, -1,0,0,0, 0,0,0,-1, 0,0,1,0]),  M([0,0,1,0, 0,0,0,1, -1,0,0,0, 0,-1,0,0]),  M([0,0,0,1, 0,0,-1,0, 0,1,0,0, -1,0,0,0])]
CC = FreeAlgebraQuotient(A,mons,mats,var("i j k"))
A=CC(vector(var("a0 a1 a2 a3")))
B=CC(vector(var("b0 b1 b2 b3")))
dim = 4
AB = A*B
s = sympify

permutations = None
if(dim < 5):
    permutations = Permutations(dim)

product = VectorOperation("product",[s(A.vector()),s(B.vector())],s(AB.vector()))
vectorspace = VectorSpace(dim,product)

# conjugate = VectorOperation("conjugate",[s(A.vector())],s(A_conj.vector()))
# v.operations += [conjugate]

info = "quaternions numbers: ij=ji=k, ii=-1, jj=-1, kk=-1;"
name="quaternions"
