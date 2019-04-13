import snapshottest

from alglbraic.glsl import GlslStruct, get_meta_glsl, meta_glsl
from alglbraic.glsl import sort_glsl_dependencies
from alglbraic.glsl import GLSL


class TestGlslStruct(snapshottest.TestCase):
    def setUp(self):
        self.struct = GlslStruct(
            "Cl_1_1", "float ONE", "float e1", "float e2", "float e12"
        )

    def test_struct_member_symbols(self):
        struct = GlslStruct("Vec3", "int x", "int y", "int z")
        syms = struct.symbols_for("a")
        self.assert_match_snapshot(str(syms))

    def test_struct_definition(self):
        struct = GlslStruct("Cl_1_1", "float ONE", "float e1", "float e2", "float e12")

        self.assert_match_snapshot(
            str(struct.definition())
        )

    def test_uniform_member_type(self):
        uniform_struct = GlslStruct("UniformStruct", "float x", "float y", "float z")
        assert uniform_struct.uniform_member_type == "float"

        nonuniform_struct = GlslStruct("NonuniformStruct", "int x", "float y")
        assert not nonuniform_struct.uniform_member_type

    def test_array_constructor(self):
        self.assert_match_snapshot(
            str(self.struct.build_from_array())
        )


class TestGlslBundler(snapshottest.TestCase):
    def setUp(self):
        self.struct = GlslStruct(
            "Cl_1_1", "float ONE", "float e1", "float e2", "float e12"
        )

    def test_glsl_helpers(self):
        assert len(tuple(x.__name__ for x in self.struct.glsl_helpers())) == 0

    def test_glsl_snippets(self):
        assert tuple(x.__name__ for x in self.struct.glsl_snippets()) == ("definition", "build_from_array",)

    def test_compile_snippet_bundle(self):
        from alglbraic.algebras.clifford_algebra import ComplexNumbers

        C = ComplexNumbers()
        self.assertMatchSnapshot(C.compile_snippet_bundle())


class TestMetaGlsl(snapshottest.TestCase):
    def test_get_meta(self):
        misc_info = "Did you know that some sharks have belly buttons?"

        def glsl_snippet() -> GLSL(depends_on=["someFunction"], misc_info=misc_info):
            return GLSL("float x = someFunction(1);")

        assert get_meta_glsl(glsl_snippet).misc_info == misc_info

    def test_meta_glsl_decorator(self):
        @meta_glsl(info="wow")
        def a():
            return "a"

        assert get_meta_glsl(a).info == "wow"
        assert a.meta_glsl.info == "wow"

    def test_layered_meta_glsl(self):
        @meta_glsl()
        @meta_glsl(info="woah")
        def b():
            return "b"

        assert get_meta_glsl(b).info == "woah"
        assert b.meta_glsl.info == "woah"


class TestGlslDependencyGraph(snapshottest.TestCase):
    def test_sort_snippets(self):
        from alglbraic.algebras.clifford_algebra import ComplexNumbers

        C = ComplexNumbers()

        snippets = [x.__name__ for x in C.glsl_snippets()]
        for _ in range(30):
            snippets2 = [x.__name__ for x in C.glsl_snippets()]
            assert snippets == snippets2

    def test_sort_dependencies(self):
        def a() -> GLSL(depends_on=[]):
            return "a"

        def c() -> GLSL(depends_on=[a]):
            return "c"

        def b() -> GLSL(depends_on=[c]):
            return "b"

        def y() -> GLSL(depends_on=[c, b, a]):
            return "y"

        def z() -> GLSL(depends_on=[y]):
            return "z"

        sorted_glsl_methods = [a, c, b, y, z]
        # print([x.__name__ for x in sort_glsl_dependencies(sorted_glsl_methods)])
        for _i in range(50):
            # make sure that sorting isn't dependent on the starting node
            resorted_glsl_methods = sort_glsl_dependencies(sorted_glsl_methods)
            assert resorted_glsl_methods == sorted_glsl_methods
