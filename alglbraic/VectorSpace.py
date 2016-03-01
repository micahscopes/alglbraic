from fragments import *
from sympy import Symbol, symbols
# Usage:
# Pass in a product operation in terms of float u[N] and float v[N].
#

class VectorSpace(Composition):
    noProduct = """
    Error: make sure to pass a Fragment defining the product
    in terms of u[i], v[j], with i,j in N.  You did not do this!"""

    pNormInits = "// the default p-norm power (p).\nuniform float NormPower; slider[0.000000001,2,100]"
    pNormFunc = """
float pNormSq(float u[N], float p) {
    float normSq = 0;
    for(int i=0; i<N; i++){
        normSq = normSq + pow(u[i],p);
    }
    return normSq;
}

float pNorm(float u[N], float p) {
    return pow(abs(pNormSq(u,p)),1.0/p);
}"""
    norm = """
float norm(float u[N]) {
    return pNorm(u,NormPower);
}"""
    pNorm = Fragment(pNormInits,pNormFunc)
    norm = Fragment(lower=norm)
    def __init__(self, dimensions, product=noProduct, norm=norm):
        if (product == self.noProduct):
            raise NotImplementedError(self.noProduct);
        Composition.__init__(self)
        self._members = [product]
        self.N = dimensions
        self.product = product
        self.norm = norm
        self.operations = []

    def upper(self):
        return "const int N = "+str(self.N)+";"

    def lower(self):
        return Fragment.get('vectorBasics.frag')

    def members(self):
        return squash([self.product,self.pNorm+self.norm]+self.operations)
