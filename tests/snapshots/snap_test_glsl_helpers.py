# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGlslStruct::test_struct_member_symbols 1'] = '[a.x, a.y, a.z]'

snapshots['TestGlslStruct::test_struct_definition 1'] = '''struct Cl_1_1 {
    float ONE; float e1; float e2; float e12;
}\\  
'''
