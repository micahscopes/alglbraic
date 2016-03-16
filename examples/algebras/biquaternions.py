from alglbraic import *
import sys

quadratic = "[-1,-1]"

vectorspace = GeometricAlgebra(quadratic)
dims = vectorspace.dims
permutations = None
if(dims < 8):
    permutations = Permutations(vectorspace.N)
info = "GEOMETRIC ALGEBRAIC FRACTALS 2016!!! Q = "+quadratic
name="g"+quadratic
