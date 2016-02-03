from fragments import *
from sympy import Symbol, symbols
from sympy.galgebra import *
# Usage:
# Pass in a product operation in terms of float u[N] and float v[N].
#

class GeometricAlgebra(Composition):
    def __init__(self, dimensions, metric):
        self.__dim = dimensions
        self.__metric = metric

        self.product = VectorOperation()
        self.vectorSpace = VectorSpace(dimensions)
    @property
    def dim(self):
        return self.__dim
    @dim.setter
    def dim(self, dim):
        self.__dim = dim

    @property
    def metric(self):
        return self.__metric
    @dim.setter
    def dim(self, dim):
        self.__metric = metric
