from fragments import *
from sympy import Symbol, symbols

class Norm(Fragment):
    def __init__(self,size_const='N'):
        Fragment.__init__(self,lower=pNormFunc.substitute(N=size_const))

pNormFunc = Template('''
float pNormSq(float u[$N], float p) {
    float normSq = 0;
    for(int i=0; i<$N; i++){
        normSq = normSq + pow(abs(u[i]),p);
    }
    return normSq;
}

float pNorm(float u[$N], float p) {
    return pow(pNormSq(u,p),1.0/p);
}

float norm(float u[$N]) {
    return pNorm(u,2.0);
}

float[$N] normalize(inout float u[$N]) {
    float nrm = norm(u);
    for(int i=0; i<$N; i++){
        u[i] = u[i]/nrm;
    }
    return u;
}
''')
