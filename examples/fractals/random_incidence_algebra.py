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

N_graph = 3;
m = random_matrix(ZZ, N_graph, x=1, y=2, density=0.8).elementwise_product(lowerTriangularOnes(N_graph))+identity_matrix(N_graph,N_graph);
M = kGeodesicMatrices(m);
dig = DiGraph(sum(M[k+1] for k in range(len(M)-1)))
P = Poset(dig);
Pa = P.incidence_algebra(RR);
P.show()
d = DiGraph(M[1])
i = 0
while (i<len(d.edges())):
    d.edge_labels()[i] = str(i);
    i+=1;
d.edge_labels()

###
dim = Pa.dimension()
syms = ("a","b")
As,Bs = [var(" ".join([s+str(i) for i in range(dim)])) for s in syms]
A = Pa.from_vector(vector(As))
B = Pa.from_vector(vector(Bs))
normA_coefs = vector(A.coefficients()).norm().combine()
AB_coefs = (A*B).coefficients()
Ai = A.coefficients()
Bi = B.coefficients()
s = sympify
info = str(Pa)

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
file = "some-incidence-algebra-%s-from-a-%s-element-poset.frag" % (dim,N_graph)

print("writing to %s" % file)
output = open(file, "w")
output.write(fractal.gl(printer))
output.close
