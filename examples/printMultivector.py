from sympy.galgebra.ga import MV
from GLSLPrinter import *

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-m","--metric")
parser.add_argument("-e","--expression")
args = parser.parse_args()

metric = "[-1,-1,-1]"
if (args.metric):
    metric = args.metric
e = MV.setup(" ".join(map(lambda i: "e"+str(i+1), range(len(metric.split(","))))),metric)
NDIM = e[0].dim
NBASIS = len(e[0].blades_flat1)
def getter(i):
    return "["+str(i)+"]"
g = map(lambda i: e[0].blades_flat1[i],range(NBASIS))
gMVs = map(lambda i: MV(g[i]),range(NBASIS))
a = map(lambda i: Symbol('a'+getter(i)), xrange(NBASIS))
b = map(lambda i: Symbol('b'+getter(i)), xrange(NBASIS))

As = map(lambda i: a[i]*g[i],range(NBASIS))
Bs = map(lambda i: b[i]*g[i],range(NBASIS))

add = lambda b,r: b+r
A = MV(reduce(add,As))
B = MV(reduce(add,Bs))
G = MV(reduce(add,g))
I = MV(g[NBASIS-1])

expr = args.expression if args.expression else "A*B"
def printGL(expr):
    print(GLSLPrinter().makeGL(expr))
printGL(eval(expr))
