from sage.all import *
DIR = os.path.dirname(os.path.realpath(__file__))
#load(DIR+"/octonions.sage")
from sage.all import *
from alglbraic import *
from sympy import symbols, Symbol, sympify
from subprocess import call
import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("--quadratic", dest='quadratic', default='[-1,-1]')
parser.add_argument("--2d", dest='include2d', action='store_true')
parser.add_argument("path",nargs='?', default = None)
options = parser.parse_args()

info = "geometric algebra with quadratic signature: "+options.quadratic
print "Initiating fractal quest on "+info

quadratic = options.quadratic
v = GeometricAlgebra(quadratic)

permutations = None
if(dim < 5):
    permutations = Permutations(dim)

def writeFractalQuest(windowDimensions):
    path = options.path
    path = "./" if path == None else path
    if (path.endswith('/')):
        suffix = "-2d" if(windowDimensions == 2) else "-3d"
        reg = re.compile('(?:\[)*([^]]+)(?:\])*')
        name="g"+options.quadratic
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
