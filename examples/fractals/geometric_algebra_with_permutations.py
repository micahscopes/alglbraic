from alglbraic import *

quadratic = "[-1,-1]"
formula = """
float MzA[N] = mutate(z,MA);
float MzB[N] = mutate(z,MB);
float MzC[N] = mutate(z,MC);
z = mul3(
    pow(MzA,pow1),
    pow(MzB,pow2),
    pow(MzC,pow3)
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
