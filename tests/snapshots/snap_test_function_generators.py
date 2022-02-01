# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestOperator::test_array_expr 1'] = '''float[25] mul(float[25] x, float[25] y){
    return float[25](
   x[0]*y[0] + x[5]*y[1] + x[10]*y[2] + x[15]*y[3] + x[20]*y[4], x[0]*y[5] + x[5]*y[6] + x[10]*y[7] + x[15]*y[8] + x[20]*y[9], x[0]*y[10] + x[5]*y[11] + x[10]*y[12] + x[15]*y[13] + x[20]*y[14], x[0]*y[15] + x[5]*y[16] + x[10]*y[17] + x[15]*y[18] + x[20]*y[19], x[0]*y[20] + x[5]*y[21] + x[10]*y[22] + x[15]*y[23] + x[20]*y[24],
   x[1]*y[0] + x[6]*y[1] + x[11]*y[2] + x[16]*y[3] + x[21]*y[4], x[1]*y[5] + x[6]*y[6] + x[11]*y[7] + x[16]*y[8] + x[21]*y[9], x[1]*y[10] + x[6]*y[11] + x[11]*y[12] + x[16]*y[13] + x[21]*y[14], x[1]*y[15] + x[6]*y[16] + x[11]*y[17] + x[16]*y[18] + x[21]*y[19], x[1]*y[20] + x[6]*y[21] + x[11]*y[22] + x[16]*y[23] + x[21]*y[24],
   x[2]*y[0] + x[7]*y[1] + x[12]*y[2] + x[17]*y[3] + x[22]*y[4], x[2]*y[5] + x[7]*y[6] + x[12]*y[7] + x[17]*y[8] + x[22]*y[9], x[2]*y[10] + x[7]*y[11] + x[12]*y[12] + x[17]*y[13] + x[22]*y[14], x[2]*y[15] + x[7]*y[16] + x[12]*y[17] + x[17]*y[18] + x[22]*y[19], x[2]*y[20] + x[7]*y[21] + x[12]*y[22] + x[17]*y[23] + x[22]*y[24],
   x[3]*y[0] + x[8]*y[1] + x[13]*y[2] + x[18]*y[3] + x[23]*y[4], x[3]*y[5] + x[8]*y[6] + x[13]*y[7] + x[18]*y[8] + x[23]*y[9], x[3]*y[10] + x[8]*y[11] + x[13]*y[12] + x[18]*y[13] + x[23]*y[14], x[3]*y[15] + x[8]*y[16] + x[13]*y[17] + x[18]*y[18] + x[23]*y[19], x[3]*y[20] + x[8]*y[21] + x[13]*y[22] + x[18]*y[23] + x[23]*y[24],
   x[4]*y[0] + x[9]*y[1] + x[14]*y[2] + x[19]*y[3] + x[24]*y[4], x[4]*y[5] + x[9]*y[6] + x[14]*y[7] + x[19]*y[8] + x[24]*y[9], x[4]*y[10] + x[9]*y[11] + x[14]*y[12] + x[19]*y[13] + x[24]*y[14], x[4]*y[15] + x[9]*y[16] + x[14]*y[17] + x[19]*y[18] + x[24]*y[19], x[4]*y[20] + x[9]*y[21] + x[14]*y[22] + x[19]*y[23] + x[24]*y[24]
) /* a 5x5 matrix */;
}'''

snapshots['TestOperator::test_simple_expr 1'] = '''float add(float a, float b){
    return a*b + a;
}'''

snapshots['TestOperator::test_simple_str 1'] = '''float add(float a, float b){
    return a*b;
}'''

snapshots['TestOperator::test_struct_expr 1'] = '''mat5x5 mul(mat5x5 x, mat5x5 y){
    return mat5x5(
   x.i0j0*y.i0j0 + x.i0j1*y.i1j0 + x.i0j2*y.i2j0 + x.i0j3*y.i3j0 + x.i0j4*y.i4j0, x.i0j0*y.i0j1 + x.i0j1*y.i1j1 + x.i0j2*y.i2j1 + x.i0j3*y.i3j1 + x.i0j4*y.i4j1, x.i0j0*y.i0j2 + x.i0j1*y.i1j2 + x.i0j2*y.i2j2 + x.i0j3*y.i3j2 + x.i0j4*y.i4j2, x.i0j0*y.i0j3 + x.i0j1*y.i1j3 + x.i0j2*y.i2j3 + x.i0j3*y.i3j3 + x.i0j4*y.i4j3, x.i0j0*y.i0j4 + x.i0j1*y.i1j4 + x.i0j2*y.i2j4 + x.i0j3*y.i3j4 + x.i0j4*y.i4j4,
   x.i1j0*y.i0j0 + x.i1j1*y.i1j0 + x.i1j2*y.i2j0 + x.i1j3*y.i3j0 + x.i1j4*y.i4j0, x.i1j0*y.i0j1 + x.i1j1*y.i1j1 + x.i1j2*y.i2j1 + x.i1j3*y.i3j1 + x.i1j4*y.i4j1, x.i1j0*y.i0j2 + x.i1j1*y.i1j2 + x.i1j2*y.i2j2 + x.i1j3*y.i3j2 + x.i1j4*y.i4j2, x.i1j0*y.i0j3 + x.i1j1*y.i1j3 + x.i1j2*y.i2j3 + x.i1j3*y.i3j3 + x.i1j4*y.i4j3, x.i1j0*y.i0j4 + x.i1j1*y.i1j4 + x.i1j2*y.i2j4 + x.i1j3*y.i3j4 + x.i1j4*y.i4j4,
   x.i2j0*y.i0j0 + x.i2j1*y.i1j0 + x.i2j2*y.i2j0 + x.i2j3*y.i3j0 + x.i2j4*y.i4j0, x.i2j0*y.i0j1 + x.i2j1*y.i1j1 + x.i2j2*y.i2j1 + x.i2j3*y.i3j1 + x.i2j4*y.i4j1, x.i2j0*y.i0j2 + x.i2j1*y.i1j2 + x.i2j2*y.i2j2 + x.i2j3*y.i3j2 + x.i2j4*y.i4j2, x.i2j0*y.i0j3 + x.i2j1*y.i1j3 + x.i2j2*y.i2j3 + x.i2j3*y.i3j3 + x.i2j4*y.i4j3, x.i2j0*y.i0j4 + x.i2j1*y.i1j4 + x.i2j2*y.i2j4 + x.i2j3*y.i3j4 + x.i2j4*y.i4j4,
   x.i3j0*y.i0j0 + x.i3j1*y.i1j0 + x.i3j2*y.i2j0 + x.i3j3*y.i3j0 + x.i3j4*y.i4j0, x.i3j0*y.i0j1 + x.i3j1*y.i1j1 + x.i3j2*y.i2j1 + x.i3j3*y.i3j1 + x.i3j4*y.i4j1, x.i3j0*y.i0j2 + x.i3j1*y.i1j2 + x.i3j2*y.i2j2 + x.i3j3*y.i3j2 + x.i3j4*y.i4j2, x.i3j0*y.i0j3 + x.i3j1*y.i1j3 + x.i3j2*y.i2j3 + x.i3j3*y.i3j3 + x.i3j4*y.i4j3, x.i3j0*y.i0j4 + x.i3j1*y.i1j4 + x.i3j2*y.i2j4 + x.i3j3*y.i3j4 + x.i3j4*y.i4j4,
   x.i4j0*y.i0j0 + x.i4j1*y.i1j0 + x.i4j2*y.i2j0 + x.i4j3*y.i3j0 + x.i4j4*y.i4j0, x.i4j0*y.i0j1 + x.i4j1*y.i1j1 + x.i4j2*y.i2j1 + x.i4j3*y.i3j1 + x.i4j4*y.i4j1, x.i4j0*y.i0j2 + x.i4j1*y.i1j2 + x.i4j2*y.i2j2 + x.i4j3*y.i3j2 + x.i4j4*y.i4j2, x.i4j0*y.i0j3 + x.i4j1*y.i1j3 + x.i4j2*y.i2j3 + x.i4j3*y.i3j3 + x.i4j4*y.i4j3, x.i4j0*y.i0j4 + x.i4j1*y.i1j4 + x.i4j2*y.i2j4 + x.i4j3*y.i3j4 + x.i4j4*y.i4j4
) /* a 5x5 matrix */;
}'''
