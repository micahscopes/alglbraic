import unittest
import snapshottest
from alglbraic.functions import operator
from sympy import glsl_code

from alglbraic.glsl import GlslStruct

class TestGlslStruct(snapshottest.TestCase):

    def test_struct_member_symbols(self):
        struct = GlslStruct('Vec3', 'int x', 'int y', 'int z')
        syms = struct.symbols_for('a')
        self.assert_match_snapshot(str(syms))
        
    def test_struct_definition(self):
        struct = GlslStruct(
            'Cl_1_1',
            'float ONE',
            'float e1',
            'float e2',
            'float e12'
        )

        self.assert_match_snapshot(
            str(struct.definition())
        )
        
