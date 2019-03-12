from sympy import Symbol, symbols
from string import Template
from .struct import GlslStruct


class FiniteModule:
    def __init__(self, name, base_ring):
        self.name = name
        self.base_ring = base_ring

        # GlslStruct.__init__(*args, **kwargs)


class FiniteModuleWithBasis(FiniteModule, GlslStruct):
    def __init__(self, name, base_ring, *basis):
        FiniteModule.__init__(self, name, base_ring)
        basis_declarations = [base_ring + " " + b for b in basis]
        GlslStruct.__init__(self, name, basis_declarations)
        self.basis = basis

    def zero(self):
        from .functions import constant
        return constant(self.base_ring+' zero()')

#     def zero(self):
#       return zero.substitute({'N': self.size})

#     def unit(self):
#       return zero.substitute({'N': self.size})

#     def zero(self):
#       return zero.substitute({'N': self.size})

#     def zero(self):
#       return zero.substitute({'N': self.size})


# zero = Template(
#     """
# $base_ring[${N}] zero() {
#   $base_ring zero[${N}]()
# }

# #pragma glslify: export(zero)
# """
# )

# unit = Template(
#     """
# #pragma glslify: zero = require(./zero.glsl)
# $base_ring[${N}] unit(int i) {
#   $base_ring[${N}] unit = zero();
#   unit[i] = base_ring_unit;
#   return unit;
# }

# #pragma glslify: export(unit)
# """
# )

# add = Template(
#     """
# $base_ring[$N] add($base_ring a[$N], $base_ring b[$N]) {
#   $base_ring c[$N];
#   for (int i = 0; i < $N; ++i){
#     c[i] = a[i]+b[i];
#   }
#   return c;
# }
# """
# )

# sub = Template(
#     """\
# $base_ring[$N] sub($base_ring a[$N], $base_ring b[$N]) {
#   $base_ring c[$N];
#   for (int i = 0; i < $N; ++i){
#     c[i] = a[i]-b[i];
#   }
#   return c;
# }\
# """
# )


# mul = Template(
#     '''\
# float[N] mul(float b[N], float a) {
#   return mul(a,b);
# }

# float[N] mul(int a, float b[N]) {
#   return mul(float(a),b);
# }

# float[N] mul(float b[N], int a) {
#   return mul(float(a),b);
# }

# float[N] mul3(float a[N], float b[N], float c[N]) {
#   return mul(mul(a,b),c);
# }\
# '''
