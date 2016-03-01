from sage.all import *
from alglbraic import *
from sympy import symbols, Symbol, sympify
from subprocess import call
import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("-f","--fold", dest='fold', default = None)
parser.add_argument("--2d", dest='include2d', action='store_true')
parser.add_argument("-i,--inspect", dest='inspectOnly', action='store_true')
parser.add_argument("group",nargs='?', default='SymmetricGroup(4)')
parser.add_argument("path",nargs='?', default = None)
options = parser.parse_args()

G = eval(options.group)
if isinstance(G,list):
    G = direct_product_permgroups(G)

fold = eval(options.fold)
if isinstance(fold,int):
    fold = [fold]

Alg = G.algebra(SR)
print "Constructing a group algebra for "+options.group+"..."
folders=[]
if(options.fold):
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

# if(options.fold):
#     print "Folding the group algebra by inverse elements..."
#     o = [Alg(l)+Alg(l).antipode() for l in G.list() if l.order() > 2]
#     o += [Alg(l)+Alg(1) for l in G.list() if l.order() == 2]
#     Alg = Alg.quotient_module(o)

###
dim = Alg.dimension()
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
    print "Group algebra folded into %s dimensions" % dim
    if not askToContinue():
        sys.exit()
else:
    print "Initiating "+info

syms = ("a","b")
As,Bs = [var(" ".join([s+str(i) for i in range(dim)])) for s in syms]
A = Alg.from_vector(vector(As))
B = Alg.from_vector(vector(Bs))

if(options.fold):
    AB = Alg.retract(A.lift()*B.lift())
    AB_coefs = AB.coefficients()
    antipode_coefs = Alg.retract(A.lift().antipode()).coefficients()
else:
    AB_coefs = (A*B).coefficients()
    antipode_coefs = A.antipode().coefficients()

Ai = A.coefficients()
Bi = B.coefficients()
s = sympify

permutations = None
if(dim < 5):
    permutations = Permutations(dim)

product = VectorOperation("product",[s(Ai),s(Bi)],s(AB_coefs))
v = VectorSpace(dim,product)

if(not options.fold):
    antipode = VectorOperation("antipode",[s(Ai)],s(antipode_coefs))
    v.operations += [antipode]

def writeFractalQuest(windowDimensions):
    path = options.path
    path = "./" if path == None else path
    if (path.endswith('/')):
        suffix = "-folded%s" % "".join(str(folders).split()) if(options.fold) else ""
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
