from fragments import *
from sympy import Symbol, symbols
# Usage:
# Pass in a product operation in terms of float u[N] and float v[N].
#

class VectorSpace(Composition):
    noProduct = """
    Error: make sure to pass a Fragment defining the product
    in terms of u[i], v[j], with i,j in N.  You did not do this!"""
    def __init__(self, dimensions, product=noProduct):
        if (product == self.noProduct):
            raise NotImplementedError(self.noProduct);
        Composition.__init__(self)
        self._members = [product]
        self.N = dimensions
        self.product = product
        self.operations = []

    def upper(self):
        return "const int N = "+str(self.N)+";"

    def lower(self):
        return Fragment.get('vectorBasics.frag')

    def members(self):
        return squash([self.product]+self.operations)
