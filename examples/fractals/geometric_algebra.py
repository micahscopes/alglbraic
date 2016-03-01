from alglbraic import *
import sys

quadratic=sys.argv[1]
if not quadratic:
    quadratic = "[-1,-1]"
quadratic = "".join(quadratic.split())

geoAlgebra = GeometricAlgebra(quadratic)
dims = geoAlgebra.dims
permutations = None
if(dims < 8):
    permutations = Permutations(geoAlgebra.N)
info = "GEOMETRIC ALGEBRAIC FRACTALS 2016!!! Q = "+quadratic

frag = FractalQuest(geoAlgebra,info,permutations,formula=formula)
gl = frag.gl()
output = open("g-%s.frag" % quadratic, "w")

output.write(gl)
output.close
