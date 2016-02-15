from fragments import *
from sympy import Symbol, symbols
from sympy.galgebra import *
# Usage:
# Pass in a product operation in terms of float u[N] and float v[N].
#

class GeometricAlgebra(Composition):
    def __init__(self, quadratic):
        self.quadratic = quadratic
        self._vectorspace = None
        self._product = None
    @property
    def dim(self):
        return self.__dim

    @property
    def quadratic(self):
        return self.__quadratic
    @quadratic.setter
    def quadratic(self, quadratic):
        self.__quadratic = quadratic
        self.__MVs = MV.setup(" ".join(map(lambda i: "e"+str(i+1), range(len(quadratic.split(","))))),quadratic)
        self.__basis = self.__MVs[0].blades_flat1
        self.__dim = len(self.__basis)
        updateVectorSpace()

    def updateVectorSpace(self):
        N = self.__dim
        g = map(lambda i: self.__basis.blades_flat1[i],range(N))
        gMVs = map(lambda i: MV(g[i]),range(N))
        a = map(lambda i: Symbol('a'+getter(i)), xrange(N))
        b = map(lambda i: Symbol('b'+getter(i)), xrange(N))
        As = map(lambda i: a[i]*g[i],range(N))
        Bs = map(lambda i: b[i]*g[i],range(N))
        A = MV(reduce(add,As))
        B = MV(reduce(add,Bs))
        AB=A*B
        ABcoefs = map(lambda i: AB.coef(gMVs[i]),range(N))
        self.__productVector = AB
        if self._product == None:
            self._product = VectorOperation("mul",[a,b],ABcoefs)
        else:
            self._product.vectors = [a,b]
            self._product.results = ABcoefs
        if self._vectorspace == None:
            self._vectorspace = VectorSpace(self.__dim,self._product)
        else:
            self._vectorspace.dim = self.__dim
            self._vectorspace.product = self._product
