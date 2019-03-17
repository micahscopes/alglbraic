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
            str(self.algebra.algebraic_product())
        )

        self.assert_match_snapshot(
            str(self.algebra.reverse())
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
            str(Cl.algebraic_product())
        )