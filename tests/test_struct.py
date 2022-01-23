import snapshottest
from alglbraic.glsl import GlslStruct

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

    def test_element_type(self):
        self.assert_match_snapshot(
            str(self.struct.build_from_array())
        )

class TestArrayTools(snapshottest.TestCase):
    def setUp(self):

        self.struct = GlslStruct(
            "Cl_1_1", "float ONE", "float e1", "float e2", "float e12"
        )

    def test_inject(self):
        members = ['ONE', 'e12']
        # self.assert_match_snapshot(self.struct.injections(4).into_array_from_subarray_at_indices())
        self.assert_match_snapshot(self.struct.injections(members).into_array_from_subarray())
        # self.assert_match_snapshot(self.struct.injections(4).into_struct_from_subarray_at_indices())
        self.assert_match_snapshot(self.struct.injections(members).into_struct_from_subarray())

        # self.assert_match_snapshot(self.struct.injections(3).into_array_from_subarray_at_indices())
        self.assert_match_snapshot(self.struct.injections(members).into_array_from_subarray())
        # self.assert_match_snapshot(self.struct.injections(3).into_struct_from_subarray_at_indices())
        self.assert_match_snapshot(self.struct.injections(members).into_struct_from_subarray())