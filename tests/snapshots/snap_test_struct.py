# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestArrayTools::test_inject 1'] = '''/* Inject array v at the indices for ONE, e12 in array u */
void injectArray(inout float u[4], float v[2]){
    u[I_Cl_1_1_ONE] = v[0];
    u[I_Cl_1_1_e12] = v[1];
}'''

snapshots['TestArrayTools::test_inject 2'] = '''/* Inject array v into ONE, e12 of struct u */
Cl_1_1 inject(Cl_1_1 u, float v[2]){
    float u_ary[4];
    toArray(u, u_ary);
    injectArray(u_ary, v);
    return fromArray(u_ary);
}'''

snapshots['TestArrayTools::test_inject 3'] = '''/* Inject array v at the indices for ONE, e12 in array u */
void injectArray(inout float u[4], float v[2]){
    u[I_Cl_1_1_ONE] = v[0];
    u[I_Cl_1_1_e12] = v[1];
}'''

snapshots['TestArrayTools::test_inject 4'] = '''/* Inject array v into ONE, e12 of struct u */
Cl_1_1 inject(Cl_1_1 u, float v[2]){
    float u_ary[4];
    toArray(u, u_ary);
    injectArray(u_ary, v);
    return fromArray(u_ary);
}'''

snapshots['TestGlslStruct::test_element_type 1'] = '''Cl_1_1 fromArray(float x[4]){
    return Cl_1_1(x[0], x[1], x[2], x[3]);
}'''

snapshots['TestGlslStruct::test_struct_definition 1'] = '''const int I_Cl_1_1_ONE = 0;
const int I_Cl_1_1_e1 = 1;
const int I_Cl_1_1_e2 = 2;
const int I_Cl_1_1_e12 = 3;

struct Cl_1_1 {
    float ONE;
    float e1;
    float e2;
    float e12;
};'''

snapshots['TestGlslStruct::test_struct_member_symbols 1'] = '[a.x, a.y, a.z]'
