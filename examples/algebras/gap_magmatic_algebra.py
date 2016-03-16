from sage.all import *
class MagmaGap(object):
    def __init__(self,magma):
        if type(magma) is str:
            magma = gap.new(magma)
        if type(magma) is not sage.interfaces.gap.GapElement:
            raise TypeError("needs a GAP magma or some GAP code that produces one!")
        if not magma.IsMagma():
            raise TypeError("GAP object is not a magma.")
        self._magma = magma
        x0 = lambda x: x-1
        self._cayley_table = matrix(ZZ,self._magma.CayleyTable()).apply_map(x0)
        self._canonical_cayley_table = matrix(ZZ,self._magma.CayleyTable().CanonicalCayleyTable()).apply_map(x0)
        self._dim = self._cayley_table.dimensions()[0]
        self.name = "magma"
    def __repr__(self):
        return "<Gap:%s>"%str(self.magma())
    magma = lambda s: s._magma
    elements = lambda s: list(s.magma().Elements())
    dimension = lambda s: s._dim
    cayley_table = lambda s: s._cayley_table
    canonical_table = lambda s: s._canonical_cayley_table
    table = canonical_table

    def ith_action(self,i):
        dim = self.dimension()
        mul = matrix(ZZ,dim,dim)
        cay = self.table()
        for j in range(dim):
            mul[j,cay[i][j]] = 1
        return mul

    actions = lambda s: [s.ith_action(i) for i in range(s.dimension())]
    algebra = lambda s: FiniteDimensionalAlgebra(SR,s.actions())#,s.elements())

class QuasigroupGap(MagmaGap):
    def __init__(self,quasigroup):
        super(MagmaGap,self).__init__(quasigroup)
        if not self.magma().IntoQuasigroup().IsMagma():
            raise TypeError("magma is not a quasigroup, so its elements couldn't have inverses.")
    inverses = lambda s: [e.Inverse() for e in s.elements()]
    Linverses = lambda s: [e.LeftInverse() for e in s.elements()]
    Rinverses = lambda s: [e.RightInverse() for e in s.elements()]
    def folding(self):
        al = self.algebra()
        dim = self.dimension()
        invIndices = [self.elements().index(l) for l in self.inverses()]
        ideals = []
        for i in range(dim):
            el = al.term(i)
            inv = al.term(invIndices[i])
            if(el == one):
                continue
                ideal = el-one
            if(el == inv):
                continue
                ideal = el+one
            else:
                ideal = el+inv
            ideals.append(ideal)
        ideal = al.ideal(ideals)
        quoMap = al.quotient_map(ideal)
        return quoMap
    folded_algebra = lambda s: s.folding().codomain()

class LoopGap(QuasigroupGap):
    def __init__(self,loop):
        super(QuasigroupGap,self).__init__(loop)
        if not self.magma().IntoLoop().IsMagma():
            raise TypeError("magma is not a loop, so it wouldn't have identity.")
        self._subloops = None
    one = lambda s: s.magma().One
    def subloops(self):
        if self._subloops == None:
            self._subloops = [LoopGap(sl) for sl in list(self.magma().AllSubloops())]
        return self._subloops
