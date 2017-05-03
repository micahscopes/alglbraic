import itertools
from fragments import *
from sympy import Symbol, symbols

#
# Look through this window into higher dimensional vector spaces.
#

class Window(Fragment):
    frame = Template("""
float[N] frame(float v[N], $point){
    // "Frame" a "window" through which to view vector v, via a "subvector" p.

    // Points p form a linear subspace of the N dimensional Euclidean space,
    // but not necessarily of the vector space we are looking at.  They are
    // really just "slices" of larger vectors.

    if($notorthogonal) {
        return v; //error, please set frame indices to be different
    }
    for(int i = 0; i<N; i++) {
$modify
    }
    $transformation
return v;
}
""")
    def __init__(self, N, frames = ["X","Y","Z"], transformation_hook=''):
        Fragment.__init__(self)
        declare = "uniform int %s; slider[1,%s,%s]"
        self.transformation_hook = transformation_hook
        self.N = N
        self.frames = ["Frame"+f for f in frames]
        self.inits = []
        if(len(self.frames) > 4):
            self.inits = ["const int N_window = %s;" % len(frames)]
        self.inits += [declare % (f,i+1,N) for i,f in enumerate(self.frames)]
        self._upper = "\n".join(self.inits)

    def lower(self):
        fr = self.frames
        if(len(fr) > 4):
            pointVar = "float p[N_window]"
        else:
            pointVar = "vec%i p" % len(fr)
        pairs = itertools.combinations(fr,2)
        logic = ["%s == %s" % (a,b) for a,b in pairs]
        logic = " || ".join(logic)

        addif = "       if (i == %s-1) { v[i] = p[%i]; }"
        addif = "\n ".join([addif % (f,i) for i,f in enumerate(fr)])
        return self.frame.substitute(notorthogonal=logic,point=pointVar,modify=addif,transformation=self.transformation_hook)
