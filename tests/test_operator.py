import unittest
import snapshottest
from alglbraic.operator import operator
from sympy import glsl_code
from sympy.abc import *

class TestOperator(snapshottest.TestCase):

    def test_simple_expr(self):
        op = operator(
            'float a',
            'float b',
            ('float', a+b*a)
        )
        self.assert_match_snapshot(op)

    def test_simple_str(self):
        op = operator(
            'float a',
            'float b',
            ('float', glsl_code(a*b))
        )
        self.assert_match_snapshot(op)


if __name__ == '__main__':
    unittest.main()
