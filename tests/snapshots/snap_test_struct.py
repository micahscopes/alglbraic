# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestArrayTools::test_inject 1'] = '''/* Inject array V at the indices for ONE, e12 in array U */
void injectArray(inout float U[4], float V[2]){
    U[I_Cl_1_1_ONE] = V[0];
    U[I_Cl_1_1_e12] = V[1];
}'''

snapshots['TestArrayTools::test_inject 2'] = '''/* Inject array V into ONE, e12 of struct U */
Cl_1_1 inject(Cl_1_1 U, float V[2]){
    float U_ary[4];
    toArray(U, U_ary);
    injectArray(U_ary, V);
    return fromArray(U_ary);
}'''

snapshots['TestArrayTools::test_inject 3'] = '''/* Inject array V at the indices for ONE, e12 in array U */
void injectArray(inout float U[4], float V[2]){
    U[I_Cl_1_1_ONE] = V[0];
    U[I_Cl_1_1_e12] = V[1];
}'''

snapshots['TestArrayTools::test_inject 4'] = '''/* Inject array V into ONE, e12 of struct U */
Cl_1_1 inject(Cl_1_1 U, float V[2]){
    float U_ary[4];
    toArray(U, U_ary);
    injectArray(U_ary, V);
    return fromArray(U_ary);
}'''

snapshots['TestGlslStruct::test_element_type 1'] = '''Cl_1_1 fromArray(float X[4]){
    return Cl_1_1(X[0], X[1], X[2], X[3]);
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
