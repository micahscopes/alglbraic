from fragments import *
from math import factorial

# Permutations can represent all the possible ways a vector's basis can get
# scrambled.  If we think of each permutation as a unary operation, some of the
# them are involutions, as applying them twice will bring back the initial
# vector.  This doesn't mean that they are anti-automorphism, necessarily,
# but they have the potential to be.  It really depends on the algebra.
#
# Check out the Symmetric Group for a look at the symmetries of permutations.
#
# The main thing for me is that playing with permutations gives a look into
# the inherent symmetries of each dimensionality.  It's very beautiful to
# watch these symmetries unfold in different vector spaces.

# todo: option to generate only certain subgroups of symmetric group, i.e. cyclic


class Permutations(Fragment):
    params = Template("""
// mutation indices (Lehmer or Lexicographic)
uniform int mutationA; slider[0,0,$M]
uniform int mutationB; slider[0,0,$M]
uniform int mutationC; slider[0,0,$M]
uniform int mutationD; slider[0,0,$M]

""")
    def __init__(self, N, method="Lehmer"):
        """ pass a vector length and permutation method:
            ('Lehmer' or 'Lexicographic')"""
        Fragment.__init__(self)
        self.method = method
        self.N = N
        self.M = factorial(N)

    def upper(self):
        return self.params.substitute(M=self.M)

    def lower(self):
        return Template(Fragment.get("permutations.frag")).substitute(method=self.method)
