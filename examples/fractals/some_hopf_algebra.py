from sage.all import *
from alglbraic import *
from sympy import symbols, Symbol, sympify

def kGeodesicMatrices(m):
    f = lambda x: 1 - pow(sgn(x),2); # using the pow function for python compatibility
    N = m.dimensions()[0];
    mask = []; M=[];
    mask.append(ones_matrix(N,N)); #mask0;
    M.append(identity_matrix(N,N)); #M0; # the matrix of 0-geodesics is the identity matrix
    i=0;
    while (i<50 and M[i] != matrix(N)):
        mask.append(mask[i].elementwise_product(M[i].apply_map(f)));
        M.append((m*M[i]).elementwise_product(mask[i+1]));
        i+=1;
    return M;

def mobius_sum_all_intervals(P):
    return sum([P.mobius_function(i[0],i[1]) for i in P.relations()]);

def lowerTriangularOnes(n):
    i = 0;
    mat = ones_matrix(n,n);
    while (i<n):
        j = i;
        while (j+1<n):
            mat[i,j+1] = 0;
            j+=1;
        i += 1;
    return mat;


# G = WeylGroup(['A',2])
# G = GL(2,2)
# G = Sp(2,2)
# G = KleinFourGroup()
G = QuaternionGroup()
Alg = QuaternionAlgebra(3)
###
dim = Alg.dimension()
syms = ("a","b")
As,Bs = [var(" ".join([s+str(i) for i in range(dim)])) for s in syms]
A = Alg.from_vector(vector(As))
B = Alg.from_vector(vector(Bs))
normA_coefs = vector(A.coefficients()).norm().combine()
AB_coefs = (A*B).coefficients()
Ai = A.coefficients()
Bi = B.coefficients()
s = sympify
info = str(Alg)

formula = """
float MzA[N] = mutate(z,MA);
float MzB[N] = mutate(z,MB);
z = mul(
    pow(MzA,pow1),
    pow(MzB,pow2)
);
"""

###
permutations = Permutations(dim)
product = VectorOperation("product",[s(Ai),s(Bi)],s(AB_coefs))
norm = VectorOperation("norm",[s(Ai)],s(normA_coefs))
v = VectorSpace(dim,product)
v.operations.append(norm)
fractal = FractalQuest(v,info,permutations,formula=formula)
printer = GLSLPrinter()
file = "some-hopf-algebra.frag"

print("writing to %s" % file)
output = open(file, "w")
output.write(fractal.gl(printer))
output.close
