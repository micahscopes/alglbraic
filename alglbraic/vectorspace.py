from .fragment import *
from sympy import Symbol, symbols
# Usage:
# Pass in a product operation in terms of float u[N] and float v[N].
#

class VectorSpace(Fragment):
    noProduct = """
    Error: make sure to pass an expression for the product
    in terms of u[i], v[j], with i,j in N.  You did not do this!"""
    def __init__(self, dimensions, product=noProduct):
        self.dims = dimensions
        self.product = product

    def head(self):
        return "const int N = "+str(self.dims)

    def body(self):
        if (self.product == self.noProduct):
            raise NotImplementedError(self.noProduct);
        body = Template(Fragment.get('vectorOperations.frag'))
        body = body.safe_substitute(product=self.product)
        return body
