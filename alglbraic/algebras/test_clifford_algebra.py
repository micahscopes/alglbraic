import unittest
import snapshottest
from alglbraic.algebras.clifford_algebra import CliffordAlgebra
from sympy import glsl_code

from alglbraic.struct import GlslStruct

class TestCliffordAlgebra(snapshottest.TestCase):

    def setUp(self):
        self.algebra = CliffordAlgebra(
            'ComplexCl1_1',
            [-1, 1],
            'e1', 'e2',
            base_ring='C',
            unit='ONE'
        )

    def test_clifford_algebra_product(self):
        self.assert_match_snapshot(
            str(self.algebra.algebraic_product(use_operators=True))
        )

        self.assert_match_snapshot(
            str(self.algebra.reverse(use_operators=True))
        )
    
    def test_big_clifford_algebra_product(self):
        Cl = CliffordAlgebra(
            'ComplexCl4',
            [1, 1, 1, 1],
            'e1', 'e2', 'e3', 'e4',
            base_ring='C',
            unit='ONE'
        )
        self.assert_match_snapshot(
            str(Cl.algebraic_product(use_operators=True))
        )

class TestComplexNumbers(snapshottest.TestCase):

    def setUp(self):
        from alglbraic.algebras.clifford_algebra import ComplexNumbers
        self.C = ComplexNumbers()

    def test_product(self):
        self.assert_match_snapshot(
            str(self.C.algebraic_product(use_operators=True))
        )

    def test_one(self):
        self.assert_match_snapshot(
            str(self.C.one(use_operators=True))
        )