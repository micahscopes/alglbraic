from alglbraic import *

quadratic=sys.argv[1]
if not quadratic:
    quadratic = "[-1,-1]"

formula = """
float MzA[N] = mutate(z,MA);
float MzB[N] = mutate(z,MB);
float MzC[N] = mutate(z,MC);
z = mul3(
    pwr(MzA,pow1),
    pwr(MzB,pow2),
    pwr(MzC,pow3)
);
"""
geoAlgebra = GeometricAlgebra(quadratic)
dims = geoAlgebra.dims
permutations = Permutations(geoAlgebra.N)
info = "GEOMETRIC ALGEBRAIC FRACTALS 2016!!! Q = "+quadratic

frag = FractalQuest(geoAlgebra,info,permutations,formula=formula)
gl = frag.gl()
output = open("g-%s.frag" % dims, "w")

output.write(gl)
output.close
