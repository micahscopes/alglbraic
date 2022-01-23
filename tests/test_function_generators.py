import unittest
import snapshottest
from sympy import glsl_code
from sympy.abc import *

from alglbraic.functions import operator
from alglbraic.glsl import StructElement


class TestOperator(snapshottest.TestCase):
    def test_simple_expr(self):
        op = operator("add", "float a", "float b", ("float", a + b * a))
        self.assert_match_snapshot(op)

    def test_simple_str(self):
        op = operator("add", "float a", "float b", ("float", glsl_code(a * b)))
        self.assert_match_snapshot(op)

    def test_array_expr(self):
        from sympy.matrices import MatrixSymbol, Matrix

        a = MatrixSymbol("x", 5, 5)
        b = MatrixSymbol("y", 5, 5)

        op = operator("mul", "float[25] x", "float[25] y", ("float[25]", Matrix(a * b)))

        self.assert_match_snapshot(op)

    def test_struct_expr(self):
        from sympy.matrices import Matrix
        from sympy import Symbol

        n, m = 5, 5
        x = Matrix([[Symbol("x.i%ij%i" % (i, j)) for j in range(m)] for i in range(n)])
        y = Matrix([[Symbol("y.i%ij%i" % (i, j)) for j in range(m)] for i in range(n)])
        result = glsl_code(StructElement("mat5x5", x * y))

        op = operator("mul", "mat5x5 x", "mat5x5 y", ("mat5x5", result))

        self.assert_match_snapshot(op)


from alglbraic.functions import constant


class TestConstant(snapshottest.TestCase):
    def test_constant(self):
        one = constant("one", ("float", 1.0))

        self.assert_match_snapshot(one)


if __name__ == "__main__":
    unittest.main()
