from snapshottest import TestCase
from alglbraic.algebras.clifford_algebra import CliffordAlgebra


class TestCliffordAlgebra(TestCase):
    def setUp(self):
        self.algebra = CliffordAlgebra(
            "ComplexCl1_1", [-1, 1], base_ring="C", unit="ONE"
        )

    def test_clifford_algebra_product(self):
        self.assert_match_snapshot(
            str(self.algebra.algebraic_product(use_operators=True))
        )

        self.assert_match_snapshot(str(self.algebra.reverse(use_operators=True)))

    def test_big_clifford_algebra_product(self):
        Cl = CliffordAlgebra("ComplexCl4", [1, 1, 1, 1], base_ring="C", unit="ONE")
        self.assert_match_snapshot(str(Cl.algebraic_product(use_operators=True)))

    def test_clifford_algebra_bundle(self):
        self.assert_match_snapshot(
            str(self.algebra.bundle())
        )


class TestComplexNumbers(TestCase):
    def setUp(self):
        from alglbraic.algebras.clifford_algebra import ComplexNumbers

        self.C = ComplexNumbers()

    def test_product(self):
        self.assert_match_snapshot(str(self.C.algebraic_product(use_operators=True)))

    def test_one(self):
        self.assert_match_snapshot(str(self.C.one(use_operators=True)))


class TestDualNumbers(TestCase):
    def setUp(self):
        from alglbraic.algebras.clifford_algebra import DualNumbers

        self.D = DualNumbers()

    def test_product(self):
        self.assert_match_snapshot(str(self.D.algebraic_product(use_operators=True)))

    def test_one(self):
        self.assert_match_snapshot(str(self.D.one(use_operators=True)))



class TestCGA(TestCase):
    def setUp(self):
        from alglbraic.algebras.clifford_algebra import ConformalGeometricAlgebra

        self.CGA = ConformalGeometricAlgebra(2)

    def test_bundle(self):
        self.assert_match_snapshot(str(self.CGA.bundle()))

    # def test_one(self):
    #     self.assert_match_snapshot(str(self.CGA.one(use_operators=True)))


