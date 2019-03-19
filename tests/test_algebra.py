import snapshottest
from alglbraic.algebra import Algebra


class TestGlslTypes(snapshottest.TestCase):
    def setUp(self):
        self.algebra = Algebra("Algebra", "BaseRing", "e1", "e2", "e3", "e4")

    def test_glsl_helpers(self):
        assert set(x.__name__ for x in self.algebra.glsl_helpers()) == set(
            [
                "add",
                "algebraic_operation",
                "binary_operation",
                "n_ary_operation",
                "one",
                "quaternary_operation",
                "scalar_int_mul",
                "sub",
                "ternary_operation",
                "unary_operation",
            ]
        )

    def test_glsl_snippets(self):
        assert set(x.__name__ for x in self.algebra.glsl_snippets()) == set(
            ["algebraic_product", "definition", "scalar_base_mul", "scalar_float_mul"]
        )
