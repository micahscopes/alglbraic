from sage.all import *
DIR = os.path.dirname(os.path.realpath(__file__))
load(DIR+"/../algebras/gap_magmatic_algebra.py")
from alglbraic import *
from sympy import symbols, Symbol, sympify
from subprocess import call
import argparse
import re
gap.load_package("loops")
parser = argparse.ArgumentParser()
parser.add_argument("-s","--subloop", dest='subloop_index', type=int, default = None)
parser.add_argument("-f","--folded", dest='fold', action='store_true')
parser.add_argument("--2d", dest='include2d', action='store_true')
parser.add_argument("-o","--orthonormalize", dest='orthonormalBasis', action='store_true')
parser.add_argument("-i,--inspect", dest='inspectOnly', action='store_true')
parser.add_argument("loop",nargs='?', default='InterestingLoop(32,1)')
parser.add_argument("path",nargs='?', default = None)
options = parser.parse_args()


loop = LoopGap(options.loop)
dim = loop.dimension()
print "Constructing a loop algebra for "+options.loop+"..."
###
info = "fractal quest on algebra formed from %s dimensional loop:" % dim
info = info+str(loop)

if(options.subloop_index):
    i = options.subloop_index - 1
    loop = loop.subloops()[i]
    print "from subloop #%s: %s" % (i,str(loop))
    # subloops = loop.subloops()
    # for i in range(len(subloops)):
    #     if i+1 == options.subloop_index:
    #         loop = subloops[i]
    #         print "%s: %s... this subloop." % (i+1,str(subloops[i]))
    #     else:
    #         print "%s: %s..." % (i+1,str(subloops[i]))

if(options.inspectOnly):
    if not FractalQuest.askToContinue():
        sys.exit()
else:
    print "Initiating "+info

alg = loop.folded_algebra() if options.fold else loop.algebra()
dim = alg.degree()
print "Resulting algebra would be %s dimensional" % dim

def vec(sym,m):
    return vector(SR, [var(sym+"%i" % (i%m+1)) for i in range(m)]);
A = alg(vec("a",dim))
B = alg(vec("b",dim))
AB_coefs = (A*B).vector().coefficients()
s = sympify

permutations = None
if(dim < 5):
    permutations = Permutations(dim)

product = AlgebraicProduct([s(A.vector().coefficients()),s(B.vector().coefficients())],s(AB_coefs))
v = VectorSpace(dim)

def writeFractalQuest(windowDimensions):
    path = options.path
    path = "./" if path == None else path
    if (path.endswith('/')):
        suffix = "-sub-%s" % options.subloop_index if(options.subloop_index) else ""
        suffix += "-2d" if(windowDimensions == 2) else "-3d"
        reg = re.compile('(?:\[)*([^]]+)(?:\])*')
        name = reg.findall(options.loop)[0]+"-algebra"
        name = "-".join(name.split(","))
        filename = path+niceFilename(name)+suffix+".frag"
    else:
        filename = path
    fractal = FractalQuest(v,product,info=info,windowDimensions=windowDimensions)
    printer = GLSLPrinter()
    print("writing %s" % filename)
    output = open(filename, "w")
    output.write(fractal.gl(printer))
    output.close

if(options.include2d or dim == 2):
    writeFractalQuest(2)
if(dim > 2):
    writeFractalQuest(3)
