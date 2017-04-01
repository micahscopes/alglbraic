from alglbraic import Composition, VectorOperation, Norm
from sage.all import CliffordAlgebra, DiagonalQuadraticForm, SR, var, vector
from string import Template
from sympy import Symbol, symbols, sympify

def vec(sym,m,suff=""):
    return vector(SR, [var(sym+"%i%s" % (i%m+1,suff)) for i in range(m)]);

midTmp = Template('''
$rtype $func($args, float angle) {
  float sin_th = sin(angle*2*PI);
  float cos_th = cos(angle*2*PI);
  
  return $result;
}
''')

class RotationOperation(VectorOperation):
    def __init__(self,N,size_const=None,functionName=None,quadraticSignature=None):
        functionName = functionName if functionName else 'rotate'
        quadraticSignature = quadraticSignature if quadraticSignature else [1]*N
        RotAlgebra = CliffordAlgebra(DiagonalQuadraticForm(SR,quadraticSignature))
        RotBasis = [a for a in RotAlgebra.basis().list() if a.degree() == 1]
        v = sum([var('v'+str(ael[0]))*ael[1] for ael in zip(range(len(RotBasis)),RotBasis)])

        rotFrom = vec('RotFrom',N)
        RotFrom = sum([rotFrom[i]*RotBasis[i] for i in range(N)])

        rotTo = vec('RotTo',N)
        RotTo = sum([rotTo[i]*RotBasis[i] for i in range(N)])

        rotor_blade = RotFrom*RotTo
        R = var('cos_th')+rotor_blade*var('sin_th')
        r = (R*v*R.transpose()/(R.transpose()*R).to_vector()[0])
        r_coeffs = [t.trig_simplify() for t in r.to_vector()][1:1+N]

        VectorOperation.__init__(self,functionName,[v.to_vector()[1:1+N],rotFrom.list(),rotTo.list()],r_coeffs,symbols=['v','fr','to'],functionTemplate=midTmp,result_size_const=size_const)
