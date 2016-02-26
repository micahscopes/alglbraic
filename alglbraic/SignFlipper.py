from fragments import *

# Does all possible sign involutions in N dimensions (i.e. the direct product
# of N copies of the cyclic group C(2)).  Uses integers mod 2^N to represent
# these possibilities as binary bitsets. e.g. 0b1001 <-> (-,+,+,-).
#
# For convenience in flipping signs, this makes three "flipper functions",
# flipA, flipB, flipC, each flipping signs according to the three uniforms,
# ints flipperA, flipperB, flipperC.

class SignFlipper(Fragment):
    def __init__(self, N):
        """ Pass in the number of dimensions (N) you'd like to flip signs in.
        Uniform integers of the appropriate length (mod 2^N) will be declared to
        represent the involutions."""
        Fragment.__init__(self)
        self.N = N
        self.M = 2**N

    def upper(self):
        return self.params.substitute(M=self.M)

    def lower(self):
        return self.flipFunctions

    params = Template("""
// sign involutions
uniform int flipperA; slider[0,0,$M]
uniform int flipperB; slider[0,0,$M]
uniform int flipperC; slider[0,0,$M]

""")
    flipFunctions = """
float[N] flip(in float A[N], int flipper) {
  for (int i=0; i< N; i++) {
    float p = pow(2.0,float(i));
    int place = int(p);
    int sgn = 1-2*((flipper & place) >> i);
    A[i] = sgn*A[i];
  }
    return A;
}

float[N] flipA(float z[N]) {
  return flip(z,flipperA);
}
float[N] flipB(float z[N]) {
  return flip(z,flipperB);
}
float[N] flipC(float z[N]) {
  return flip(z,flipperC);
}
    """
