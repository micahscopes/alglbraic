import snapshottest
from alglbraic.algebra import Algebra


class TestGlslTypes(snapshottest.TestCase):
    def setUp(self):
        self.algebra = Algebra("Algebra", "BaseRing", "e1", "e2", "e3", "e4")

    def test_glsl_helpers(self):
        alg_helpers = set(x.__name__ for x in self.algebra.glsl_helpers())
        expected_helpers = set(
            [
                "add",
                "add_3",
                "add_4",
                "algebraic_operation",
                "binary_operation",
                "n_ary_operation",
                "definition",
                "one",
                "quaternary_operation",
                "scalar_int_mul",
                "scalar_float_mul",
                "scalar_base_mul",
                "sub",
                "ternary_operation",
                "unary_operation",
            ]
        )

        diff = alg_helpers.difference(expected_helpers)
        assert diff == set()

    def test_glsl_snippets(self):
        snippets = set(x.__name__ for x in self.algebra.glsl_snippets())
        expected_snippets = {
            "definition",
            "build_from_array",
            "export_to_array",
            "algebraic_product",
            "algebraic_product_3",
            "scalar_float_mul",
            "sub",
            "one",
            "scalar_base_mul",
            "add",
            "add_3",
            "add_4",
            "scalar_int_mul",
            "zero",
            "zero_array"
        }
        assert snippets == expected_snippets
