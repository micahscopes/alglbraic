from sage.all import *
DIR = os.path.dirname(os.path.realpath(__file__))
from sage.all import *
from alglbraic import *
from sympy import symbols, Symbol, sympify
from subprocess import call
import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("--algebra", dest='algebra', default = None)
parser.add_argument("--rotation", dest='rotation', action='store_true')
parser.add_argument("--2d", dest='include2d', action='store_true')
parser.add_argument("path",nargs='?', default = None)
options = parser.parse_args()
execfile(options.algebra)

print "Initiating fractal quest for "+info

permutations = None
if(dim < 5):
    permutations = Permutations(dim)

rotation = options.rotation and dim < 9

def writeFractalQuest(windowDimensions):
    path = options.path
    path = "./" if path == None else path
    if (path.endswith('/')):
        suffix = "-2d" if(windowDimensions == 2) else "-3d"
        suffix += '-rotation' if (options.rotation) else ''
        reg = re.compile('(?:\[)*([^]]+)(?:\])*')
        filename = path+niceFilename(name)+suffix+".frag"
    else:
        filename = path
    fractal = FractalQuest(vectorspace,product,info=info,rotation=rotation,windowDimensions=windowDimensions)
    printer = GLSLPrinter()
    print("writing %s" % filename)
    output = open(filename, "w")
    output.write(fractal.gl())
    output.close

if(options.include2d or dim == 2):
    writeFractalQuest(2)
if(dim > 2):
    writeFractalQuest(3)
