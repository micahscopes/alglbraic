from yeropa import *
from sage.all import *

def LeavittPathAlg(G):
    Vs = G.vertices()
    Es = G.edges()
    def GH(e):
        ge = list(e[0:2])
        ge.reverse()
        return tuple(ge+[e[2],"ghost"])
    GEs = [GH(e) for e in Es]
    CK2 = [(e,GH(e)) for e in Es] # these are basis elements for the CK2 relation, e.g. aa*+bb* = v
    def CK2Es(v):
        return [(e,GH(e)) for e in Es if e[0] == v]
    def CK(e):
        return (e,GH(e))

    B = Vs+Es+GEs+CK2
    dim = len(B)

    I = {}
    Act = {}
    names = []
    i = 0
    for el in B:
        I[el] = i
        Act[el] = Matrix(QQ,dim)
        i+=1

    dim = len(I)

    for i,v in enumerate(Vs):
        names.append("v%s"%i)

        Act[v][I[v],I[v]] = 1 # (rel 1)    
        for e in Es: # (rel CK2)
            if e[0] != v:
                continue
            Act[GH(e)][I[e],I[v]] = 1
            for eck2 in CK2Es(v):
                if eck2[0] == e:
                    continue
                Act[GH(e)][I[e],I[eck2]] = -1

    for e in Es: 
        names.append("e%s%s"%(I[e[0]],I[e[1]]))

        s = e[0]
        r = e[1]
        Act[r][I[e],I[e]] = 1 # (rel 2)
        Act[e][I[s],I[e]] = 1 # (rel 2)
        Act[s][I[GH(e)],I[GH(e)]] = 1 # (rel 2)
        Act[GH(e)][I[r],I[GH(e)]] = 1 # (rel 2)

    #     Act[GH(e)][I[e],I[CK(e)]] = 1 # (CK2 basis elements)

    for e in Es: # (rel CK1)
        names.append("gh%s%s"%(I[e[0]],I[e[1]]))

        r = e[1]
    #     print e
    #     Act[e][I[GH(e)],I[r]] = 1

    # for i,ck in enumerate(CK2):
    #     names.append("ck%s%s"%(I[ck[0][0]],I[ck[0][1]]))

    ActMats = []
    i = 0
    B = Vs+Es+GEs
    while i<len(B):
        for el in B:
            if I[el] == i:
                ActMats.append(Act[el])
                i+=1

    CK2CongruenceRelations = {}
    for v in Vs:
        if len(CK2Es(v))<1:
            continue
        CK2CongruenceRelations[I[v]] = [(I[ck[0]],I[ck[1]]) for ck in CK2Es(v)]
    CK2CongruenceRelations

    A = FreeAlgebra(SR,names)
    A.inject_variables()
    # print A.gens(), len(A.gens())
    # print A.monoid().gens()
    CK2gens = [A.monoid().gens()[I[e]]*A.monoid().gens()[I[GH(e)]] for e in Es]

    gens = A.monoid().gens()

    mons = list(gens)+CK2gens
    # print mons
    # print len(ActMats)
    # print A.ngens()
    # print(ActMats)
    B = A.quo(mons,ActMats,names)
    B.inject_variables()
    # print B.gens()[0]
    CK2eqs = []
    for i in CK2CongruenceRelations:
        ck = CK2CongruenceRelations[i]
    #     print B.gens()[0]
    #     print B.gens()[3]*B.gens()[6]
        CK2eqs.append(-B.gens()[i]+sum([B.gens()[c[0]]*B.gens()[c[1]] for c in ck]))


    mod = B.module()
    vs = mod.vector_space()

    print [B(v).vector() for v in CK2eqs]
    v = vs.subspace([B(v).vector() for v in CK2eqs])
    sub = vs.subspace(v)
    quo = mod.quotient(sub)

    # quo.lift((e01*gh01+2*e02*gh02).vector())
    # print quo((e01*gh01+e02*gh02).vector())
    dim = len(mons)
    # sub(vs(e01*gh01 + e02*gh02))
    # vec("a",dim)
    a = B(vec("a",dim))
    b = B(vec("b",dim))
    ab = (a*b).vector()
    a = a.vector()
    b = b.vector()

    ab.coefficients()
    return (a,b,ab)