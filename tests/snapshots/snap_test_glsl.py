# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGlslStruct::test_struct_definition 1'] = '''struct Cl_1_1 {
    float ONE; float e1; float e2; float e12;
}'''

snapshots['TestGlslStruct::test_struct_member_symbols 1'] = '[a.x, a.y, a.z]'

snapshots['TestGlslBundler::test_compile_snippet_bundle 1'] = '''C product(C u, C v){
    return C(sub(mul(u.real, v.real), mul(u.imag, v.imag)), add(mul(u.imag, v.real), mul(u.real, v.imag)));
}

struct C {
    float real; float imag;
}

C mul(float a, C x){
    return C(mul(a, x.real), mul(a, x.imag));
}

C mul(float a, C x){
    return mul(mul(a, one()), x);
}'''
