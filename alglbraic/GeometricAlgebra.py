from fragments import *
from sympy import Symbol, symbols
from sympy.galgebra import *
from .VectorOperation import *
from .VectorSpace import *
from .Window import *

# Usage:
# Pass in a product operation in terms of float u[N] and float v[N].
#

class GeometricAlgebra(VectorSpace):
    def __init__(self, quadratic):
        Composition.__init__(self)
        MVs = MV.setup(" ".join(map(lambda i: "e"+str(i+1), range(len(quadratic.split(","))))),quadratic)
        basis = MVs[0].blades_flat1
        N = len(basis)
        self.N = N # the dimension of the Clifford Module/Geometric Algebra
        self.dims = len(MVs) # the dimension 1-blades
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

        product = VectorOperation("product",[a,b],AB)
        operations = [ \
            product,
            VectorOperation("inner",[a,b],AinB),
            VectorOperation("outer",[a,b],AoutB),
            VectorOperation("rev",[a],revA),
            Fragment(lower="""
float norm(float a[N]){
    return inner(a,rev(a))[0];
}
        """)]
        VectorSpace.__init__(self,N,product)
        self._members += operations