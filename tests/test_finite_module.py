import unittest
import snapshottest
from alglbraic.finite_module import FiniteModule
from sympy import glsl_code
from sympy.abc import *

from alglbraic.struct import GlslStruct

class TestFiniteModule(snapshottest.TestCase):

    def setUp(self):
        self.module = FiniteModule(
            'ComplexCl2', 'C',
            'ONE',
            'e1',
            'e2',
            'e12',
            unit='ONE'
        )

    def test_finite_module(self):
        module = self.module

        self.assert_match_snapshot(
            str(module.definition())
        )

        self.assert_match_snapshot(
            str(module.zero())
        )

        self.assert_match_snapshot(
            str(module.one())
        )

        self.assert_match_snapshot(
            str(module.add())
        )

        self.assert_match_snapshot(
            str(module.sub())
        )

        self.assert_match_snapshot(
            str(module.scalar_mul())
        )

    def test_algebraic_product(self):
        pass