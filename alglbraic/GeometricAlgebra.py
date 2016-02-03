from fragments import *
from sympy import Symbol, symbols
from sympy.galgebra import *
from .VectorOperation import *
from .VectorSpace import *

# Usage:
# Pass in a product operation in terms of float u[N] and float v[N].
#

class GeometricAlgebra(Composition):
    def __init__(self, quadratic):
        Composition.__init__(self)
        MVs = MV.setup(" ".join(map(lambda i: "e"+str(i+1), range(len(quadratic.split(","))))),quadratic)
        basis = MVs[0].blades_flat1
        N = len(basis)
        self.N = N
        g = map(lambda i: basis[i],range(N))
        gMVs = map(lambda i: MV(g[i]),range(N))
        a = map(lambda i: Symbol('a'+str(i)), xrange(N))
        b = map(lambda i: Symbol('b'+str(i)), xrange(N))
        As = map(lambda i: a[i]*g[i],range(N))
        Bs = map(lambda i: b[i]*g[i],range(N))
        add = lambda a,b: a+b
        A = MV(reduce(add,As))
        B = MV(reduce(add,Bs))
        AB=map(lambda i: (A*B).coef(gMVs[i]),range(N))
        AinB=map(lambda i: (A|B).coef(gMVs[i]),range(N))
        AoutB=map(lambda i: (A^B).coef(gMVs[i]),range(N))
        revA=map(lambda i: (A.rev()).coef(gMVs[i]),range(N))

        glAB = VectorOperation("product",[a,b],AB)
        glAinB = VectorOperation("inner",[a,b],AinB)
        glAoutB = VectorOperation("outer",[a,b],AoutB)
        glRevA = VectorOperation("rev",[a],revA)
        glNorm = Fragment(body="""
float norm(float a[N]){
    return inner(a,rev(a))[0];
}
        """)
        vectSpace = VectorSpace(N,glAB)

        self._members = [vectSpace,glAinB,glAoutB,glRevA,glNorm]
