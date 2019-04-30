# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestArrayTools::test_inject 1'] = '''/* Inject coordinates i_v of array v into coordinates i_u of array u */
void inject(inout float u[4], int i_u[4], float v[4], int i_v[4]){
    u[i_u[0]] = v[i_v[0]];
    u[i_u[1]] = v[i_v[1]];
    u[i_u[2]] = v[i_v[2]];
    u[i_u[3]] = v[i_v[3]];
}'''

snapshots['TestArrayTools::test_inject 2'] = '''/* Inject array v into coordinates i_u of array u */
void inject(inout float u[4], int i_u[4], float v[4]){
    u[i_u[0]] = v[0];
    u[i_u[1]] = v[1];
    u[i_u[2]] = v[2];
    u[i_u[3]] = v[3];
}'''

snapshots['TestArrayTools::test_inject 3'] = '''/* Inject coordinates i_v of array v into coordinates i_u of struct u */
Cl_1_1 inject(inout float u[4], int i_u[4], float v[4], int i_v[4]){
    float u_ary[4];
    toArray(u, u_ary);
    inject(u_ary, i_u, v);
    return fromArray(u_ary);
}'''

snapshots['TestGlslStruct::test_array_constructor 1'] = '''Cl_1_1 fromArray(float x[4]){
    return Cl_1_1(x[0], x[1], x[2], x[3]);
}'''

snapshots['TestGlslStruct::test_struct_definition 1'] = '''struct Cl_1_1 {
    float ONE;
    float e1;
    float e2;
    float e12;
};'''

snapshots['TestGlslStruct::test_struct_member_symbols 1'] = '[a.x, a.y, a.z]'

snapshots['TestArrayTools::test_inject 4'] = '''/* Inject array v into coordinates i_u of struct u */
Cl_1_1 inject(inout float u[4], int i_u[4], float v[4]){
    float u_ary[4];
    toArray(u, u_ary);
    inject(u_ary, i_u, v);
    return fromArray(u_ary);
}'''

snapshots['TestArrayTools::test_inject 5'] = '''/* Inject coordinates i_v of array v into coordinates i_u of array u */
void inject(inout float u[4], int i_u[3], float v[3], int i_v[3]){
    u[i_u[0]] = v[i_v[0]];
    u[i_u[1]] = v[i_v[1]];
    u[i_u[2]] = v[i_v[2]];
}'''

snapshots['TestArrayTools::test_inject 6'] = '''/* Inject array v into coordinates i_u of array u */
void inject(inout float u[3], int i_u[3], float v[4]){
    u[i_u[0]] = v[0];
    u[i_u[1]] = v[1];
    u[i_u[2]] = v[2];
}'''

snapshots['TestArrayTools::test_inject 7'] = '''/* Inject coordinates i_v of array v into coordinates i_u of struct u */
Cl_1_1 inject(inout float u[4], int i_u[3], float v[3], int i_v[3]){
    float u_ary[4];
    toArray(u, u_ary);
    inject(u_ary, i_u, v);
    return fromArray(u_ary);
}'''

snapshots['TestArrayTools::test_inject 8'] = '''/* Inject array v into coordinates i_u of struct u */
Cl_1_1 inject(inout float u[4], int i_u[3], float v[3]){
    float u_ary[4];
    toArray(u, u_ary);
    inject(u_ary, i_u, v);
    return fromArray(u_ary);
}'''
