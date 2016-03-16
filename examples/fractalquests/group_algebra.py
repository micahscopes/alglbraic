from sage.all import *
from alglbraic import *
from sympy import symbols, Symbol, sympify
from subprocess import call
import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("-f","--fold", dest='fold', default = None)
parser.add_argument("--2d", dest='include2d', action='store_true')
parser.add_argument("-o","--orthonormalize", dest='orthonormalBasis', action='store_true')
parser.add_argument("-i,--inspect", dest='inspectOnly', action='store_true')
parser.add_argument("group",nargs='?', default='SymmetricGroup(4)')
parser.add_argument("path",nargs='?', default = None)
options = parser.parse_args()

G = eval(options.group)
if isinstance(G,list):
    G = direct_product_permgroups(G)

if(options.fold):
    fold = eval(options.fold)
    if isinstance(fold,int):
        fold = [fold]

Alg = GAlg =  G.algebra(SR)
print "Constructing a group algebra for "+options.group+"..."
folders=[]
if(options.fold and not options.orthonormalBasis):
    print "Folding the %s-dimensional group algebra by designated order-2 elements..." % Alg.dimension()
    o2 = [l for l in G.list() if l.order() == 2]
    e2 = []
    for i in range(len(o2)):
        el = o2[i]
        if i+1 in fold:
            folders.append(i+1)
            e2.append(el)
            print "%s: %s... fold." % (i+1,o2[i])
        else:
            print "%s: %s..." % (i+1,o2[i])

    oLeft = [Alg(inv*el)+Alg(el) for el in G.list() if el.order() > 1 for inv in e2]
    oRight = [Alg(el*inv)+Alg(el) for el in G.list() if el.order() > 1 for inv in e2]
    o = oLeft + oRight
    Alg = Alg.quotient_module(o)
    dim = Alg.dimension()
    print "Group algebra folded into %s dimensions" % dim

if(options.orthonormalBasis):
    dim = len(Alg.center_basis())
    print "Group algebra has a %s dimensional center basis" % dim


# if(options.fold):
#     print "Folding the group algebra by inverse elements..."
#     o = [Alg(l)+Alg(l).antipode() for l in G.list() if l.order() > 2]
#     o += [Alg(l)+Alg(1) for l in G.list() if l.order() == 2]
#     Alg = Alg.quotient_module(o)

###
info = "%s dimensional fractal quest on " % dim
info = info+str(Alg)

def askToContinue():
    # raw_input returns the empty string for "enter"
    yes = set(['yes','y','ye'])
    no = set(['no','n',''])
    sys.stdout.write("Initiate fractal quest? [y/N]   ")
    choice = raw_input().lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        return askToContinue()

if(options.inspectOnly):
    if not askToContinue():
        sys.exit()
else:
    print "Initiating "+info
basis = Alg.center_basis().list() if options.orthonormalBasis else Alg.basis().list()
dim = len(basis)
syms = ("a","b")
symbolsOnBasis = lambda syms,V: [reduce(lambda a,b: a+b,[var(s+str(i))*V[i] for i in range(len(V))]) for s in syms]
AG,BG = symbolsOnBasis(syms,GAlg.basis().list())
A,B = symbolsOnBasis(syms,Alg.basis().list())

if options.fold:
    AB = Alg.retract(A.lift()*B.lift())
    antipode = Alg.retract(A.lift().antipode())
else:
    AB = A*B
    antipode = A.antipode()

if options.orthonormalBasis:
    antipode_coefs = antipode.central_form().coefficients()
    AB_coefs = AB.central_form().coefficients()
else:
    antipode_coefs = antipode.coefficients()
    AB_coefs = AB.coefficients()

s = sympify

permutations = None
if(dim < 5):
    permutations = Permutations(dim)

product = VectorOperation("product",[s(A.coefficients()),s(B.coefficients())],s(AB_coefs))
v = VectorSpace(dim,product)

if(not options.fold):
    antipode = VectorOperation("antipode",[s(A.coefficients())],s(antipode_coefs))
    v.operations += [antipode]

def writeFractalQuest(windowDimensions):
    path = options.path
    path = "./" if path == None else path
    if (path.endswith('/')):
        suffix = "-folded%s" % "".join(str(folders).split()) if(options.fold) else ""
        suffix += "-orthonormal" if(options.orthonormalBasis) else ""
        suffix += "-2d" if(windowDimensions == 2) else "-3d"
        reg = re.compile('(?:\[)*([^]]+)(?:\])*')
        name = reg.findall(options.group)[0]
        name = "-by-".join(name.split(","))
        filename = path+niceFilename(name)+suffix+".frag"
    else:
        filename = path
    fractal = FractalQuest(v,info,permutations,windowDimensions=windowDimensions)
    printer = GLSLPrinter()
    print("writing %s" % filename)
    output = open(filename, "w")
    output.write(fractal.gl(printer))
    output.close

if(options.include2d or dim == 2):
    writeFractalQuest(2)
if(dim > 2):
    writeFractalQuest(3)
