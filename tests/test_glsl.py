import snapshottest

from alglbraic.glsl import GlslStruct, get_glsl_meta
from alglbraic.glsl import sort_glsl_dependencies
from alglbraic import GLSL


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

        self.assert_match_snapshot(str(struct.definition()))

    def test_glsl_helpers(self):
        assert len(tuple(x.__name__ for x in self.struct.glsl_helpers())) == 0

    def test_glsl_snippets(self):
        assert tuple(x.__name__ for x in self.struct.glsl_snippets()) == ("definition",)


class TestGlslMeta(snapshottest.TestCase):
    def test_get_meta(self):
        misc_info = 'Did you know that some sharks have belly buttons?'

        def glsl_snippet() -> GLSL(depends_on=['someFunction'], misc_info=misc_info):
            return GLSL('float x = someFunction(1);')

        assert get_glsl_meta(glsl_snippet).misc_info == misc_info

class TestGlslDependencyGraph(snapshottest.TestCase):
    def test_sort_dependencies(self):
        def a() -> GLSL:
            return 'a'

        def b() -> GLSL(depends_on=['a']):
            return 'b'
        
        def c() -> GLSL(depends_on=['b']):
            return 'c'

        def y() -> GLSL(depends_on=['c', 'b', 'a']):
            return 'y'

        def z() -> GLSL(depends_on=['y']):
            return 'z'


        glsl_methods = [a, b, c, y, z]
        glsl_methods = dict([(x.__name__, x) for x in glsl_methods])

        def sort(k='a'):
            return sort_glsl_dependencies(glsl_methods, k)

        assert sort('a') == sort('b')
        assert sort('b') == sort('c')
        assert sort('y') == sort('z')