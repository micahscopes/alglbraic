import snapshottest

from alglbraic.glsl import GlslBundler, GlslStruct, glsl_meta, GLSL
from alglbraic.glsl import glsl_snippet


class TestGlslBundler(snapshottest.TestCase):
    def setUp(self):
        self.struct = GlslStruct(
            "Cl_1_1", "float ONE", "float e1", "float e2", "float e12"
        )

    def test_glsl_helpers(self):
        assert len(tuple(x.__name__ for x in self.struct.glsl_helpers())) == 0

    def test_glsl_snippets(self):
        assert tuple(x.__name__ for x in self.struct.glsl_snippets()) == ("definition", "build_from_array", "export_to_array", "zero_array")

    def test_compile_snippet_bundle(self):
        from alglbraic.algebras.clifford_algebra import ComplexNumbers

        C = ComplexNumbers()
        self.assertMatchSnapshot(C.bundle())


class TestMetaGlsl(snapshottest.TestCase):
    def test_get_meta(self):
        misc_info = "Did you know that some sharks have belly buttons?"

        def glsl_snippet_maker() -> glsl_snippet(depends_on=["someFunction"], misc_info=misc_info):
            return glsl_snippet("float x = someFunction(1);")

        assert glsl_meta(glsl_snippet_maker).misc_info == misc_info

    def test_meta_glsl_decorator(self):
        @GLSL(info="wow")
        def a():
            return "a"

        assert glsl_meta(a).info == "wow"
        assert a.GLSL.info == "wow"

    def test_layered_meta_glsl(self):
        @GLSL
        @GLSL(info="woah")
        def b():
            return "b"

        assert glsl_meta(b).info == "woah"
        assert b.GLSL.info == "woah"


class TestGlslDependencyGraph(snapshottest.TestCase):
    def test_sort_snippets(self):
        from alglbraic.algebras.clifford_algebra import ComplexNumbers

        C = ComplexNumbers()

        snippets = [x.__name__ for x in C.glsl_snippets()]
        for _ in range(30):
            snippets2 = [x.__name__ for x in C.glsl_snippets()]
            assert snippets == snippets2

    def test_sort_dependencies(self):
        def a() -> glsl_snippet(depends_on=[]):
            return "a"

        def c() -> glsl_snippet(depends_on=[a]):
            return "c"

        def b() -> glsl_snippet(depends_on=[c]):
            return "b"

        def y() -> glsl_snippet(depends_on=[c, b, a]):
            return "y"

        def z() -> glsl_snippet(depends_on=[y]):
            return "z"

        sorted_glsl_methods = [a, c, b, y, z]
        # print([x.__name__ for x in sort_glsl_dependencies(sorted_glsl_methods)])
        for _i in range(50):
            # make sure that sorting isn't dependent on the starting node
            resorted_glsl_methods = GlslBundler.sort_glsl_dependencies(sorted_glsl_methods)
            assert resorted_glsl_methods == sorted_glsl_methods
