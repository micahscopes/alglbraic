from alglbraic import *
import sys

quadratic=sys.argv[1]
if not quadratic:
    quadratic = "[-1,-1]"

formula = """

z = mul3(
    pwr(flipA(z),pow1),
    pwr(flipB(z),pow2),
    pwr(flipC(z),pow3)
);
"""
geoAlgebra = GeometricAlgebra(quadratic)
dims = geoAlgebra.dims
permutations = Permutations(geoAlgebra.N)

info = "GEOMETRIC ALGEBRAIC FRACTALS 2016!!! Q = "+quadratic

frag = FractalQuest(geoAlgebra,info,permutations,formula=formula)
gl = frag.gl()
output = open("g-%s-w-involutions.frag" % dims, "w")

output.write(gl)
output.close
