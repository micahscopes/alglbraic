from alglbraic import *

quadratic = "[-1, -1, -1]"
geoAlgebra = GeometricAlgebra(quadratic)
dims = geoAlgebra.dims
permutations = Permutations(geoAlgebra.N)
info = "GEOMETRIC ALGEBRAIC FRACTALS 2016!!! Q = "+quadratic

frag = FractalQuest(geoAlgebra,info,permutations)

gl = frag.gl()
output = open("rudimentary-g%s.frag" % dims, "w")
output.write(gl)
output.close
