from sympy import Basic, Function, Symbol
from sympy.printing.str import StrPrinter
from sympy.core.function import _coeff_isneg
from galgebra.mv import MV

class GLSLPrinter(StrPrinter):
    """
    Rudimentary GLSL printing tools.  Capable of printing with mul/add/sub functions instead of
    operators.  Prints pow(b,n) instead of b**n.   Goals: support for emulated double/quad/octal
    precision.

    Used predominantly with the geometric algebra module, for now.

    Available settings:
    'use_operators': Boolean (should the printer use operators for +,-,*, or functions?)
    """

    _default_settings = {
        'order': None,
        'full_prec': 'auto',
        'error_on_reserved': False,
        'reserved_word_suffix': '_',
        'use_operators': True,
        'MV_wrap': 'float[N](%s);',
        'element_wrap': '%s',
        'add_wrap': 'add(%s, %s)',
        'sub_wrap': 'sub(%s, %s)',
        'mul_wrap': 'mul(%s, %s)',
        'pow_wrap': 'pow(%s, %s)',
        'abs_wrap': 'abs(%s)'
    }

    def __init__(self, settings={}):
        StrPrinter.__init__(self, settings)

    def _print_Pow(self, expr):
        return self._settings['pow_wrap'] % (self._print(expr.base),
                                 self._print(float(expr.exp)))

    def _print_Abs(self, expr):
        return self._settings['abs_wrap'] % self._print(expr.args[0])

    def _print_int(self, expr):
        return str(float(expr))

    def _print_Add(self, expr, order=None):
        if(self._settings['use_operators']):
            return StrPrinter._print_Add(self,expr,order)

        terms = list(expr.args)

        def partition(p,l):
            return reduce(lambda x, y: (x[0]+[y], x[1]) if p(y) else (x[0], x[1]+[y]), l,  ([], []))
        def add(a,b):
            return self._settings['add_wrap'] % (a,b)
        neg, pos = partition(lambda arg: _coeff_isneg(arg), terms)
        s = pos = reduce(lambda a,b: add(a,b), map(lambda t: self._print(t),pos))
        if(len(neg) > 0):
            # sum the absolute values of the negative terms
            neg = reduce(lambda a,b: add(a,b), map(lambda n: self._print(-n),neg))
            # then subtract them from the positive terms
            s = self._settings['sub_wrap'] % (pos,neg)
        return s

    def _print_Mul(self, expr, order=None):
        if(self._settings['use_operators']):
            return StrPrinter._print_Mul(self,expr)

        terms = list(expr.args)
        def partition(p,l):
            return reduce(lambda x, y: (x[0]+[y], x[1]) if p(y) else (x[0], x[1]+[y]), l,  ([], []))
        def mul(a,b):
            return self._settings['mul_wrap'] % (a,b)
        s = reduce(lambda a,b: mul(a,b), map(lambda t: self._print(t),terms))
        return s

    def _print_MV(self, expr):
        blades = MV(expr).blades_flat1
        # return print(self)
        coefs = map(lambda i: MV(expr).coef(MV(blades[i])),range(len(blades)))
        s = self._settings['MV_wrap'] % ", ".join(map(lambda co: (self._settings['element_wrap'] % self._print(co)),coefs))
        return s
    #
    # def formatBinaryOperation(self,a,b,OPab,uStr="u[%i]",vStr="v[%i]"):
    #     """Given lists a,b of sympy symbols and a map a,b -> OP(a,b),
    #     returns GLSL formatted in terms of u[i],v[i]."""
    #
    #     u = map(lambda i: Symbol(uStr % i), xrange(len(a)))
    #     v = map(lambda i: Symbol(vStr % i), xrange(len(b)))
    #     OPuv = map(lambda OPab_i: OPab_i.subs(dict(zip(a,u)+zip(b,v))), OPab)
    #     OPuvGL = map(lambda OPuv_i: self.makeGL(OPuv_i),OPuv)
    #     return "float[N](%s)" % ", ".join(OPuvGL)
    #
    # def formatUnaryOperation(self,a,OPa,uStr="u[%i]"):
    #     """Given a list of sympy symbols a, and a map a->OP(a),
    #     returns GLSL formatted in terms of u[i] -> OP(u[i])."""
    #
    #     u = map(lambda i: Symbol(uStr % i), xrange(len(a)))
    #     OPu = map(lambda OPa_i: OPa_i.subs(dict(zip(a,u)+zip(b,v))), OPa)
    #     OPuGL = map(lambda OPu_i: self.makeGL(OPu_i),OPu)
    #     return "float[N](%s)" % ", ".join(OPuGL)

    def makeGL(self,expr):
        return self._print(expr)
