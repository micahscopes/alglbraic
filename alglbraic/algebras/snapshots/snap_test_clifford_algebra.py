# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCGA::test_bundle 1'] = '''const int I_CGA2_scalar = 0;
const int I_CGA2_e1 = 1;
const int I_CGA2_e2 = 2;
const int I_CGA2_enil = 3;
const int I_CGA2_einf = 4;
const int I_CGA2_e12 = 5;
const int I_CGA2_e1nil = 6;
const int I_CGA2_e1inf = 7;
const int I_CGA2_e2nil = 8;
const int I_CGA2_e2inf = 9;
const int I_CGA2_enilinf = 10;
const int I_CGA2_e12nil = 11;
const int I_CGA2_e12inf = 12;
const int I_CGA2_e1nilinf = 13;
const int I_CGA2_e2nilinf = 14;
const int I_CGA2_e12nilinf = 15;

struct CGA2 {
    float scalar;
    float e1;
    float e2;
    float enil;
    float einf;
    float e12;
    float e1nil;
    float e1inf;
    float e2nil;
    float e2inf;
    float enilinf;
    float e12nil;
    float e12inf;
    float e1nilinf;
    float e2nilinf;
    float e12nilinf;
};

CGA2 fromArray(float x[16]){
    return CGA2(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15]);
}

void toArray(CGA2 x, inout float x_ary[16]){
    x_ary[0] = x.scalar;
    x_ary[1] = x.e1;
    x_ary[2] = x.e2;
    x_ary[3] = x.enil;
    x_ary[4] = x.einf;
    x_ary[5] = x.e12;
    x_ary[6] = x.e1nil;
    x_ary[7] = x.e1inf;
    x_ary[8] = x.e2nil;
    x_ary[9] = x.e2inf;
    x_ary[10] = x.enilinf;
    x_ary[11] = x.e12nil;
    x_ary[12] = x.e12inf;
    x_ary[13] = x.e1nilinf;
    x_ary[14] = x.e2nilinf;
    x_ary[15] = x.e12nilinf;
}

void zero(inout float x[16]){
    x[0] = 0.0;
    x[1] = 0.0;
    x[2] = 0.0;
    x[3] = 0.0;
    x[4] = 0.0;
    x[5] = 0.0;
    x[6] = 0.0;
    x[7] = 0.0;
    x[8] = 0.0;
    x[9] = 0.0;
    x[10] = 0.0;
    x[11] = 0.0;
    x[12] = 0.0;
    x[13] = 0.0;
    x[14] = 0.0;
    x[15] = 0.0;
}

CGA2 add(CGA2 u, CGA2 v){
    return CGA2(u.scalar + v.scalar, u.e1 + v.e1, u.e2 + v.e2, u.enil + v.enil, u.einf + v.einf, u.e12 + v.e12, u.e1nil + v.e1nil, u.e1inf + v.e1inf, u.e2nil + v.e2nil, u.e2inf + v.e2inf, u.enilinf + v.enilinf, u.e12nil + v.e12nil, u.e12inf + v.e12inf, u.e1nilinf + v.e1nilinf, u.e2nilinf + v.e2nilinf, u.e12nilinf + v.e12nilinf);
}

CGA2 one(){
    return CGA2(1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
}



CGA2 sub(CGA2 u, CGA2 v){
    return CGA2(u.scalar - v.scalar, u.e1 - v.e1, u.e2 - v.e2, u.enil - v.enil, u.einf - v.einf, u.e12 - v.e12, u.e1nil - v.e1nil, u.e1inf - v.e1inf, u.e2nil - v.e2nil, u.e2inf - v.e2inf, u.enilinf - v.enilinf, u.e12nil - v.e12nil, u.e12inf - v.e12inf, u.e1nilinf - v.e1nilinf, u.e2nilinf - v.e2nilinf, u.e12nilinf - v.e12nilinf);
}

CGA2 zero(){
    return CGA2(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
}

CGA2 mul(float a, CGA2 x){
    return CGA2(a*x.scalar, a*x.e1, a*x.e2, a*x.enil, a*x.einf, a*x.e12, a*x.e1nil, a*x.e1inf, a*x.e2nil, a*x.e2inf, a*x.enilinf, a*x.e12nil, a*x.e12inf, a*x.e1nilinf, a*x.e2nilinf, a*x.e12nilinf);
}

CGA2 mul(CGA2 u, CGA2 v){
    return CGA2(u.e1*v.e1 - u.e12*v.e12 + u.e12inf*v.e12nil + u.e12nil*v.e12inf - u.e12nilinf*v.e12nilinf + u.e1inf*v.e1nil + u.e1nil*v.e1inf + u.e1nilinf*v.e1nilinf + u.e2*v.e2 + u.e2inf*v.e2nil + u.e2nil*v.e2inf + u.e2nilinf*v.e2nilinf - u.einf*v.enil - u.enil*v.einf + u.enilinf*v.enilinf + u.scalar*v.scalar, u.e1*v.scalar + u.e12*v.e2 + u.e12inf*v.e2nil + u.e12nil*v.e2inf + u.e12nilinf*v.e2nilinf - u.e1inf*v.enil - u.e1nil*v.einf + u.e1nilinf*v.enilinf - u.e2*v.e12 + u.e2inf*v.e12nil + u.e2nil*v.e12inf - u.e2nilinf*v.e12nilinf + u.einf*v.e1nil + u.enil*v.e1inf + u.enilinf*v.e1nilinf + u.scalar*v.e1, u.e1*v.e12 - u.e12*v.e1 - u.e12inf*v.e1nil - u.e12nil*v.e1inf - u.e12nilinf*v.e1nilinf - u.e1inf*v.e12nil - u.e1nil*v.e12inf + u.e1nilinf*v.e12nilinf + u.e2*v.scalar - u.e2inf*v.enil - u.e2nil*v.einf + u.e2nilinf*v.enilinf + u.einf*v.e2nil + u.enil*v.e2inf + u.enilinf*v.e2nilinf + u.scalar*v.e2, u.e1*v.e1nil - u.e12*v.e12nil - u.e12nil*v.e12 - u.e12nil*v.e12nilinf + u.e12nilinf*v.e12nil - u.e1nil*v.e1 - u.e1nil*v.e1nilinf - u.e1nilinf*v.e1nil + u.e2*v.e2nil - u.e2nil*v.e2 - u.e2nil*v.e2nilinf - u.e2nilinf*v.e2nil + u.enil*v.enilinf + u.enil*v.scalar - u.enilinf*v.enil + u.scalar*v.enil, u.e1*v.e1inf - u.e12*v.e12inf - u.e12inf*v.e12 + u.e12inf*v.e12nilinf - u.e12nilinf*v.e12inf - u.e1inf*v.e1 + u.e1inf*v.e1nilinf + u.e1nilinf*v.e1inf + u.e2*v.e2inf - u.e2inf*v.e2 + u.e2inf*v.e2nilinf + u.e2nilinf*v.e2inf - u.einf*v.enilinf + u.einf*v.scalar + u.enilinf*v.einf + u.scalar*v.einf, u.e1*v.e2 + u.e12*v.scalar - u.e12inf*v.enil - u.e12nil*v.einf + u.e12nilinf*v.enilinf + u.e1inf*v.e2nil + u.e1nil*v.e2inf + u.e1nilinf*v.e2nilinf - u.e2*v.e1 - u.e2inf*v.e1nil - u.e2nil*v.e1inf - u.e2nilinf*v.e1nilinf - u.einf*v.e12nil - u.enil*v.e12inf + u.enilinf*v.e12nilinf + u.scalar*v.e12, u.e1*v.enil + u.e12*v.e2nil - u.e12nil*v.e2 - u.e12nil*v.e2nilinf - u.e12nilinf*v.e2nil + u.e1nil*v.enilinf + u.e1nil*v.scalar - u.e1nilinf*v.enil - u.e2*v.e12nil - u.e2nil*v.e12 - u.e2nil*v.e12nilinf + u.e2nilinf*v.e12nil - u.enil*v.e1 - u.enil*v.e1nilinf - u.enilinf*v.e1nil + u.scalar*v.e1nil, u.e1*v.einf + u.e12*v.e2inf - u.e12inf*v.e2 + u.e12inf*v.e2nilinf + u.e12nilinf*v.e2inf - u.e1inf*v.enilinf + u.e1inf*v.scalar + u.e1nilinf*v.einf - u.e2*v.e12inf - u.e2inf*v.e12 + u.e2inf*v.e12nilinf - u.e2nilinf*v.e12inf - u.einf*v.e1 + u.einf*v.e1nilinf + u.enilinf*v.e1inf + u.scalar*v.e1inf, u.e1*v.e12nil - u.e12*v.e1nil + u.e12nil*v.e1 + u.e12nil*v.e1nilinf + u.e12nilinf*v.e1nil + u.e1nil*v.e12 + u.e1nil*v.e12nilinf - u.e1nilinf*v.e12nil + u.e2*v.enil + u.e2nil*v.enilinf + u.e2nil*v.scalar - u.e2nilinf*v.enil - u.enil*v.e2 - u.enil*v.e2nilinf - u.enilinf*v.e2nil + u.scalar*v.e2nil, u.e1*v.e12inf - u.e12*v.e1inf + u.e12inf*v.e1 - u.e12inf*v.e1nilinf - u.e12nilinf*v.e1inf + u.e1inf*v.e12 - u.e1inf*v.e12nilinf + u.e1nilinf*v.e12inf + u.e2*v.einf - u.e2inf*v.enilinf + u.e2inf*v.scalar + u.e2nilinf*v.einf - u.einf*v.e2 + u.einf*v.e2nilinf + u.enilinf*v.e2inf + u.scalar*v.e2inf, u.e1*v.e1nilinf - u.e12*v.e12nilinf + u.e12inf*v.e12nil - u.e12nil*v.e12inf - u.e12nilinf*v.e12 + u.e1inf*v.e1nil - u.e1nil*v.e1inf + u.e1nilinf*v.e1 + u.e2*v.e2nilinf + u.e2inf*v.e2nil - u.e2nil*v.e2inf + u.e2nilinf*v.e2 - u.einf*v.enil + u.enil*v.einf + u.enilinf*v.scalar + u.scalar*v.enilinf, u.e1*v.e2nil + u.e12*v.enil + u.e12nil*v.enilinf + u.e12nil*v.scalar - u.e12nilinf*v.enil - u.e1nil*v.e2 - u.e1nil*v.e2nilinf - u.e1nilinf*v.e2nil - u.e2*v.e1nil + u.e2nil*v.e1 + u.e2nil*v.e1nilinf + u.e2nilinf*v.e1nil + u.enil*v.e12 + u.enil*v.e12nilinf - u.enilinf*v.e12nil + u.scalar*v.e12nil, u.e1*v.e2inf + u.e12*v.einf - u.e12inf*v.enilinf + u.e12inf*v.scalar + u.e12nilinf*v.einf - u.e1inf*v.e2 + u.e1inf*v.e2nilinf + u.e1nilinf*v.e2inf - u.e2*v.e1inf + u.e2inf*v.e1 - u.e2inf*v.e1nilinf - u.e2nilinf*v.e1inf + u.einf*v.e12 - u.einf*v.e12nilinf + u.enilinf*v.e12inf + u.scalar*v.e12inf, u.e1*v.enilinf + u.e12*v.e2nilinf + u.e12inf*v.e2nil - u.e12nil*v.e2inf + u.e12nilinf*v.e2 - u.e1inf*v.enil + u.e1nil*v.einf + u.e1nilinf*v.scalar - u.e2*v.e12nilinf + u.e2inf*v.e12nil - u.e2nil*v.e12inf - u.e2nilinf*v.e12 + u.einf*v.e1nil - u.enil*v.e1inf + u.enilinf*v.e1 + u.scalar*v.e1nilinf, u.e1*v.e12nilinf - u.e12*v.e1nilinf - u.e12inf*v.e1nil + u.e12nil*v.e1inf - u.e12nilinf*v.e1 - u.e1inf*v.e12nil + u.e1nil*v.e12inf + u.e1nilinf*v.e12 + u.e2*v.enilinf - u.e2inf*v.enil + u.e2nil*v.einf + u.e2nilinf*v.scalar + u.einf*v.e2nil - u.enil*v.e2inf + u.enilinf*v.e2 + u.scalar*v.e2nilinf, u.e1*v.e2nilinf + u.e12*v.enilinf - u.e12inf*v.enil + u.e12nil*v.einf + u.e12nilinf*v.scalar + u.e1inf*v.e2nil - u.e1nil*v.e2inf + u.e1nilinf*v.e2 - u.e2*v.e1nilinf - u.e2inf*v.e1nil + u.e2nil*v.e1inf - u.e2nilinf*v.e1 - u.einf*v.e12nil + u.enil*v.e12inf + u.enilinf*v.e12 + u.scalar*v.e12nilinf);
}

CGA2 mul(int a, CGA2 x){
    return mul(float(a), x);
}

CGA2 dual(CGA2 u){
    return CGA2(u.e12nilinf, u.e2nilinf, -u.e1nilinf, u.e12nil, -u.e12inf, -u.enilinf, u.e2nil, -u.e2inf, -u.e1nil, u.e1inf, u.e12, -u.enil, u.einf, u.e2, -u.e1, -u.scalar);
}

CGA2 involve(CGA2 u){
    return CGA2(u.scalar, -u.e1, -u.e2, -u.enil, -u.einf, u.e12, u.e1nil, u.e1inf, u.e2nil, u.e2inf, u.enilinf, -u.e12nil, -u.e12inf, -u.e1nilinf, -u.e2nilinf, u.e12nilinf);
}

CGA2 inner(CGA2 u, CGA2 v){
    return CGA2(u.e1*v.e1 - u.e12*v.e12 + u.e12inf*v.e12nil + u.e12nil*v.e12inf - u.e12nilinf*v.e12nilinf + u.e1inf*v.e1nil + u.e1nil*v.e1inf + u.e1nilinf*v.e1nilinf + u.e2*v.e2 + u.e2inf*v.e2nil + u.e2nil*v.e2inf + u.e2nilinf*v.e2nilinf - u.einf*v.enil - u.enil*v.einf + u.enilinf*v.enilinf, u.e12*v.e2 + u.e12inf*v.e2nil + u.e12nil*v.e2inf + u.e12nilinf*v.e2nilinf - u.e1inf*v.enil - u.e1nil*v.einf + u.e1nilinf*v.enilinf - u.e2*v.e12 + u.e2inf*v.e12nil + u.e2nil*v.e12inf - u.e2nilinf*v.e12nilinf + u.einf*v.e1nil + u.enil*v.e1inf + u.enilinf*v.e1nilinf, u.e1*v.e12 - u.e12*v.e1 - u.e12inf*v.e1nil - u.e12nil*v.e1inf - u.e12nilinf*v.e1nilinf - u.e1inf*v.e12nil - u.e1nil*v.e12inf + u.e1nilinf*v.e12nilinf - u.e2inf*v.enil - u.e2nil*v.einf + u.e2nilinf*v.enilinf + u.einf*v.e2nil + u.enil*v.e2inf + u.enilinf*v.e2nilinf, u.e1*v.e1nil - u.e12*v.e12nil - u.e12nil*v.e12 - u.e12nil*v.e12nilinf + u.e12nilinf*v.e12nil - u.e1nil*v.e1 - u.e1nil*v.e1nilinf - u.e1nilinf*v.e1nil + u.e2*v.e2nil - u.e2nil*v.e2 - u.e2nil*v.e2nilinf - u.e2nilinf*v.e2nil + u.enil*v.enilinf - u.enilinf*v.enil, u.e1*v.e1inf - u.e12*v.e12inf - u.e12inf*v.e12 + u.e12inf*v.e12nilinf - u.e12nilinf*v.e12inf - u.e1inf*v.e1 + u.e1inf*v.e1nilinf + u.e1nilinf*v.e1inf + u.e2*v.e2inf - u.e2inf*v.e2 + u.e2inf*v.e2nilinf + u.e2nilinf*v.e2inf - u.einf*v.enilinf + u.enilinf*v.einf, -u.e12inf*v.enil - u.e12nil*v.einf + u.e12nilinf*v.enilinf - u.einf*v.e12nil - u.enil*v.e12inf + u.enilinf*v.e12nilinf, -u.e12nil*v.e2 - u.e12nilinf*v.e2nil - u.e1nilinf*v.enil - u.e2*v.e12nil - u.e2nil*v.e12nilinf - u.enil*v.e1nilinf, -u.e12inf*v.e2 + u.e12nilinf*v.e2inf + u.e1nilinf*v.einf - u.e2*v.e12inf + u.e2inf*v.e12nilinf + u.einf*v.e1nilinf, u.e1*v.e12nil + u.e12nil*v.e1 + u.e12nilinf*v.e1nil + u.e1nil*v.e12nilinf - u.e2nilinf*v.enil - u.enil*v.e2nilinf, u.e1*v.e12inf + u.e12inf*v.e1 - u.e12nilinf*v.e1inf - u.e1inf*v.e12nilinf + u.e2nilinf*v.einf + u.einf*v.e2nilinf, u.e1*v.e1nilinf - u.e12*v.e12nilinf - u.e12nilinf*v.e12 + u.e1nilinf*v.e1 + u.e2*v.e2nilinf + u.e2nilinf*v.e2, -u.e12nilinf*v.enil + u.enil*v.e12nilinf, u.e12nilinf*v.einf - u.einf*v.e12nilinf, u.e12nilinf*v.e2 - u.e2*v.e12nilinf, u.e1*v.e12nilinf - u.e12nilinf*v.e1, 0.0);
}

CGA2 lcontract(CGA2 u, CGA2 v){
    return CGA2(u.e1*v.e1 - u.e12*v.e12 + u.e12inf*v.e12nil + u.e12nil*v.e12inf - u.e12nilinf*v.e12nilinf + u.e1inf*v.e1nil + u.e1nil*v.e1inf + u.e1nilinf*v.e1nilinf + u.e2*v.e2 + u.e2inf*v.e2nil + u.e2nil*v.e2inf + u.e2nilinf*v.e2nilinf - u.einf*v.enil - u.enil*v.einf + u.enilinf*v.enilinf + u.scalar*v.scalar, -u.e2*v.e12 + u.e2inf*v.e12nil + u.e2nil*v.e12inf - u.e2nilinf*v.e12nilinf + u.einf*v.e1nil + u.enil*v.e1inf + u.enilinf*v.e1nilinf + u.scalar*v.e1, u.e1*v.e12 - u.e1inf*v.e12nil - u.e1nil*v.e12inf + u.e1nilinf*v.e12nilinf + u.einf*v.e2nil + u.enil*v.e2inf + u.enilinf*v.e2nilinf + u.scalar*v.e2, u.e1*v.e1nil - u.e12*v.e12nil - u.e12nil*v.e12nilinf - u.e1nil*v.e1nilinf + u.e2*v.e2nil - u.e2nil*v.e2nilinf + u.enil*v.enilinf + u.scalar*v.enil, u.e1*v.e1inf - u.e12*v.e12inf + u.e12inf*v.e12nilinf + u.e1inf*v.e1nilinf + u.e2*v.e2inf + u.e2inf*v.e2nilinf - u.einf*v.enilinf + u.scalar*v.einf, -u.einf*v.e12nil - u.enil*v.e12inf + u.enilinf*v.e12nilinf + u.scalar*v.e12, -u.e2*v.e12nil - u.e2nil*v.e12nilinf - u.enil*v.e1nilinf + u.scalar*v.e1nil, -u.e2*v.e12inf + u.e2inf*v.e12nilinf + u.einf*v.e1nilinf + u.scalar*v.e1inf, u.e1*v.e12nil + u.e1nil*v.e12nilinf - u.enil*v.e2nilinf + u.scalar*v.e2nil, u.e1*v.e12inf - u.e1inf*v.e12nilinf + u.einf*v.e2nilinf + u.scalar*v.e2inf, u.e1*v.e1nilinf - u.e12*v.e12nilinf + u.e2*v.e2nilinf + u.scalar*v.enilinf, u.enil*v.e12nilinf + u.scalar*v.e12nil, -u.einf*v.e12nilinf + u.scalar*v.e12inf, -u.e2*v.e12nilinf + u.scalar*v.e1nilinf, u.e1*v.e12nilinf + u.scalar*v.e2nilinf, u.scalar*v.e12nilinf);
}

CGA2 outer(CGA2 u, CGA2 v){
    return CGA2(u.scalar*v.scalar, u.e1*v.scalar + u.scalar*v.e1, u.e2*v.scalar + u.scalar*v.e2, u.enil*v.scalar + u.scalar*v.enil, u.einf*v.scalar + u.scalar*v.einf, u.e1*v.e2 + u.e12*v.scalar - u.e2*v.e1 + u.scalar*v.e12, u.e1*v.enil + u.e1nil*v.scalar - u.enil*v.e1 + u.scalar*v.e1nil, u.e1*v.einf + u.e1inf*v.scalar - u.einf*v.e1 + u.scalar*v.e1inf, u.e2*v.enil + u.e2nil*v.scalar - u.enil*v.e2 + u.scalar*v.e2nil, u.e2*v.einf + u.e2inf*v.scalar - u.einf*v.e2 + u.scalar*v.e2inf, -u.einf*v.enil + u.enil*v.einf + u.enilinf*v.scalar + u.scalar*v.enilinf, u.e1*v.e2nil + u.e12*v.enil + u.e12nil*v.scalar - u.e1nil*v.e2 - u.e2*v.e1nil + u.e2nil*v.e1 + u.enil*v.e12 + u.scalar*v.e12nil, u.e1*v.e2inf + u.e12*v.einf + u.e12inf*v.scalar - u.e1inf*v.e2 - u.e2*v.e1inf + u.e2inf*v.e1 + u.einf*v.e12 + u.scalar*v.e12inf, u.e1*v.enilinf - u.e1inf*v.enil + u.e1nil*v.einf + u.e1nilinf*v.scalar + u.einf*v.e1nil - u.enil*v.e1inf + u.enilinf*v.e1 + u.scalar*v.e1nilinf, u.e2*v.enilinf - u.e2inf*v.enil + u.e2nil*v.einf + u.e2nilinf*v.scalar + u.einf*v.e2nil - u.enil*v.e2inf + u.enilinf*v.e2 + u.scalar*v.e2nilinf, u.e1*v.e2nilinf + u.e12*v.enilinf - u.e12inf*v.enil + u.e12nil*v.einf + u.e12nilinf*v.scalar + u.e1inf*v.e2nil - u.e1nil*v.e2inf + u.e1nilinf*v.e2 - u.e2*v.e1nilinf - u.e2inf*v.e1nil + u.e2nil*v.e1inf - u.e2nilinf*v.e1 - u.einf*v.e12nil + u.enil*v.e12inf + u.enilinf*v.e12 + u.scalar*v.e12nilinf);
}

CGA2 I(){
    return CGA2(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0);
}

CGA2 rcontract(CGA2 u, CGA2 v){
    return CGA2(u.e1*v.e1 - u.e12*v.e12 + u.e12inf*v.e12nil + u.e12nil*v.e12inf - u.e12nilinf*v.e12nilinf + u.e1inf*v.e1nil + u.e1nil*v.e1inf + u.e1nilinf*v.e1nilinf + u.e2*v.e2 + u.e2inf*v.e2nil + u.e2nil*v.e2inf + u.e2nilinf*v.e2nilinf - u.einf*v.enil - u.enil*v.einf + u.enilinf*v.enilinf + u.scalar*v.scalar, u.e1*v.scalar + u.e12*v.e2 + u.e12inf*v.e2nil + u.e12nil*v.e2inf + u.e12nilinf*v.e2nilinf - u.e1inf*v.enil - u.e1nil*v.einf + u.e1nilinf*v.enilinf, -u.e12*v.e1 - u.e12inf*v.e1nil - u.e12nil*v.e1inf - u.e12nilinf*v.e1nilinf + u.e2*v.scalar - u.e2inf*v.enil - u.e2nil*v.einf + u.e2nilinf*v.enilinf, -u.e12nil*v.e12 + u.e12nilinf*v.e12nil - u.e1nil*v.e1 - u.e1nilinf*v.e1nil - u.e2nil*v.e2 - u.e2nilinf*v.e2nil + u.enil*v.scalar - u.enilinf*v.enil, -u.e12inf*v.e12 - u.e12nilinf*v.e12inf - u.e1inf*v.e1 + u.e1nilinf*v.e1inf - u.e2inf*v.e2 + u.e2nilinf*v.e2inf + u.einf*v.scalar + u.enilinf*v.einf, u.e12*v.scalar - u.e12inf*v.enil - u.e12nil*v.einf + u.e12nilinf*v.enilinf, -u.e12nil*v.e2 - u.e12nilinf*v.e2nil + u.e1nil*v.scalar - u.e1nilinf*v.enil, -u.e12inf*v.e2 + u.e12nilinf*v.e2inf + u.e1inf*v.scalar + u.e1nilinf*v.einf, u.e12nil*v.e1 + u.e12nilinf*v.e1nil + u.e2nil*v.scalar - u.e2nilinf*v.enil, u.e12inf*v.e1 - u.e12nilinf*v.e1inf + u.e2inf*v.scalar + u.e2nilinf*v.einf, -u.e12nilinf*v.e12 + u.e1nilinf*v.e1 + u.e2nilinf*v.e2 + u.enilinf*v.scalar, u.e12nil*v.scalar - u.e12nilinf*v.enil, u.e12inf*v.scalar + u.e12nilinf*v.einf, u.e12nilinf*v.e2 + u.e1nilinf*v.scalar, -u.e12nilinf*v.e1 + u.e2nilinf*v.scalar, u.e12nilinf*v.scalar);
}

CGA2 reverse(CGA2 u){
    return CGA2(u.scalar, u.e1, u.e2, u.enil, u.einf, -u.e12, -u.e1nil, -u.e1inf, -u.e2nil, -u.e2inf, -u.enilinf, -u.e12nil, -u.e12inf, -u.e1nilinf, -u.e2nilinf, u.e12nilinf);
}

CGA2 conjugate(CGA2 u){
    return reverse(involve(u));
}
'''

snapshots['TestCliffordAlgebra::test_big_clifford_algebra_product 1'] = '''ComplexCl4 mul(ComplexCl4 u, ComplexCl4 v){
    return ComplexCl4(u.ONE*v.ONE + u.e1*v.e1 - u.e12*v.e12 - u.e123*v.e123 + u.e1234*v.e1234 - u.e124*v.e124 - u.e13*v.e13 - u.e134*v.e134 - u.e14*v.e14 + u.e2*v.e2 - u.e23*v.e23 - u.e234*v.e234 - u.e24*v.e24 + u.e3*v.e3 - u.e34*v.e34 + u.e4*v.e4, u.ONE*v.e1 + u.e1*v.ONE + u.e12*v.e2 - u.e123*v.e23 - u.e1234*v.e234 - u.e124*v.e24 + u.e13*v.e3 - u.e134*v.e34 + u.e14*v.e4 - u.e2*v.e12 - u.e23*v.e123 + u.e234*v.e1234 - u.e24*v.e124 - u.e3*v.e13 - u.e34*v.e134 - u.e4*v.e14, u.ONE*v.e2 + u.e1*v.e12 - u.e12*v.e1 + u.e123*v.e13 + u.e1234*v.e134 + u.e124*v.e14 + u.e13*v.e123 - u.e134*v.e1234 + u.e14*v.e124 + u.e2*v.ONE + u.e23*v.e3 - u.e234*v.e34 + u.e24*v.e4 - u.e3*v.e23 - u.e34*v.e234 - u.e4*v.e24, u.ONE*v.e3 + u.e1*v.e13 - u.e12*v.e123 - u.e123*v.e12 - u.e1234*v.e124 + u.e124*v.e1234 - u.e13*v.e1 + u.e134*v.e14 + u.e14*v.e134 + u.e2*v.e23 - u.e23*v.e2 + u.e234*v.e24 + u.e24*v.e234 + u.e3*v.ONE + u.e34*v.e4 - u.e4*v.e34, u.ONE*v.e4 + u.e1*v.e14 - u.e12*v.e124 - u.e123*v.e1234 + u.e1234*v.e123 - u.e124*v.e12 - u.e13*v.e134 - u.e134*v.e13 - u.e14*v.e1 + u.e2*v.e24 - u.e23*v.e234 - u.e234*v.e23 - u.e24*v.e2 + u.e3*v.e34 - u.e34*v.e3 + u.e4*v.ONE, u.ONE*v.e12 + u.e1*v.e2 + u.e12*v.ONE + u.e123*v.e3 - u.e1234*v.e34 + u.e124*v.e4 - u.e13*v.e23 - u.e134*v.e234 - u.e14*v.e24 - u.e2*v.e1 + u.e23*v.e13 + u.e234*v.e134 + u.e24*v.e14 + u.e3*v.e123 - u.e34*v.e1234 + u.e4*v.e124, u.ONE*v.e13 + u.e1*v.e3 + u.e12*v.e23 - u.e123*v.e2 + u.e1234*v.e24 + u.e124*v.e234 + u.e13*v.ONE + u.e134*v.e4 - u.e14*v.e34 - u.e2*v.e123 - u.e23*v.e12 - u.e234*v.e124 + u.e24*v.e1234 - u.e3*v.e1 + u.e34*v.e14 + u.e4*v.e134, u.ONE*v.e14 + u.e1*v.e4 + u.e12*v.e24 - u.e123*v.e234 - u.e1234*v.e23 - u.e124*v.e2 + u.e13*v.e34 - u.e134*v.e3 + u.e14*v.ONE - u.e2*v.e124 - u.e23*v.e1234 + u.e234*v.e123 - u.e24*v.e12 - u.e3*v.e134 - u.e34*v.e13 - u.e4*v.e1, u.ONE*v.e23 + u.e1*v.e123 - u.e12*v.e13 + u.e123*v.e1 - u.e1234*v.e14 - u.e124*v.e134 + u.e13*v.e12 + u.e134*v.e124 - u.e14*v.e1234 + u.e2*v.e3 + u.e23*v.ONE + u.e234*v.e4 - u.e24*v.e34 - u.e3*v.e2 + u.e34*v.e24 + u.e4*v.e234, u.ONE*v.e24 + u.e1*v.e124 - u.e12*v.e14 + u.e123*v.e134 + u.e1234*v.e13 + u.e124*v.e1 + u.e13*v.e1234 - u.e134*v.e123 + u.e14*v.e12 + u.e2*v.e4 + u.e23*v.e34 - u.e234*v.e3 + u.e24*v.ONE - u.e3*v.e234 - u.e34*v.e23 - u.e4*v.e2, u.ONE*v.e34 + u.e1*v.e134 - u.e12*v.e1234 - u.e123*v.e124 - u.e1234*v.e12 + u.e124*v.e123 - u.e13*v.e14 + u.e134*v.e1 + u.e14*v.e13 + u.e2*v.e234 - u.e23*v.e24 + u.e234*v.e2 + u.e24*v.e23 + u.e3*v.e4 + u.e34*v.ONE - u.e4*v.e3, u.ONE*v.e123 + u.e1*v.e23 + u.e12*v.e3 + u.e123*v.ONE + u.e1234*v.e4 - u.e124*v.e34 - u.e13*v.e2 + u.e134*v.e24 + u.e14*v.e234 - u.e2*v.e13 + u.e23*v.e1 - u.e234*v.e14 - u.e24*v.e134 + u.e3*v.e12 + u.e34*v.e124 - u.e4*v.e1234, u.ONE*v.e124 + u.e1*v.e24 + u.e12*v.e4 + u.e123*v.e34 - u.e1234*v.e3 + u.e124*v.ONE - u.e13*v.e234 - u.e134*v.e23 - u.e14*v.e2 - u.e2*v.e14 + u.e23*v.e134 + u.e234*v.e13 + u.e24*v.e1 + u.e3*v.e1234 - u.e34*v.e123 + u.e4*v.e12, u.ONE*v.e134 + u.e1*v.e34 + u.e12*v.e234 - u.e123*v.e24 + u.e1234*v.e2 + u.e124*v.e23 + u.e13*v.e4 + u.e134*v.ONE - u.e14*v.e3 - u.e2*v.e1234 - u.e23*v.e124 - u.e234*v.e12 + u.e24*v.e123 - u.e3*v.e14 + u.e34*v.e1 + u.e4*v.e13, u.ONE*v.e234 + u.e1*v.e1234 - u.e12*v.e134 + u.e123*v.e14 - u.e1234*v.e1 - u.e124*v.e13 + u.e13*v.e124 + u.e134*v.e12 - u.e14*v.e123 + u.e2*v.e34 + u.e23*v.e4 + u.e234*v.ONE - u.e24*v.e3 - u.e3*v.e24 + u.e34*v.e2 + u.e4*v.e23, u.ONE*v.e1234 + u.e1*v.e234 + u.e12*v.e34 + u.e123*v.e4 + u.e1234*v.ONE - u.e124*v.e3 - u.e13*v.e24 + u.e134*v.e2 + u.e14*v.e23 - u.e2*v.e134 + u.e23*v.e14 - u.e234*v.e1 - u.e24*v.e13 + u.e3*v.e124 + u.e34*v.e12 - u.e4*v.e123);
}'''

snapshots['TestCliffordAlgebra::test_clifford_algebra_bundle 1'] = '''const int I_ComplexCl1_1_ONE = 0;
const int I_ComplexCl1_1_e1 = 1;
const int I_ComplexCl1_1_e2 = 2;
const int I_ComplexCl1_1_e12 = 3;

struct ComplexCl1_1 {
    C ONE;
    C e1;
    C e2;
    C e12;
};

ComplexCl1_1 fromArray(C x[4]){
    return ComplexCl1_1(x[0], x[1], x[2], x[3]);
}

void toArray(ComplexCl1_1 x, inout C x_ary[4]){
    x_ary[0] = x.ONE;
    x_ary[1] = x.e1;
    x_ary[2] = x.e2;
    x_ary[3] = x.e12;
}

void zero(inout C x[4]){
    x[0] = zero();
    x[1] = zero();
    x[2] = zero();
    x[3] = zero();
}

ComplexCl1_1 add(ComplexCl1_1 u, ComplexCl1_1 v){
    return ComplexCl1_1(add(u.ONE, v.ONE), add(u.e1, v.e1), add(u.e2, v.e2), add(u.e12, v.e12));
}

ComplexCl1_1 one(){
    return ComplexCl1_1(one(), zero(), zero(), zero());
}

ComplexCl1_1 mul(float a, ComplexCl1_1 x){
    return mul(mul(a, one()), x);
}

ComplexCl1_1 sub(ComplexCl1_1 u, ComplexCl1_1 v){
    return ComplexCl1_1(sub(u.ONE, v.ONE), sub(u.e1, v.e1), sub(u.e2, v.e2), sub(u.e12, v.e12));
}

ComplexCl1_1 zero(){
    return ComplexCl1_1(zero(), zero(), zero(), zero());
}

ComplexCl1_1 mul(C a, ComplexCl1_1 x){
    return ComplexCl1_1(mul(a, x.ONE), mul(a, x.e1), mul(a, x.e2), mul(a, x.e12));
}

ComplexCl1_1 mul(ComplexCl1_1 u, ComplexCl1_1 v){
    return ComplexCl1_1(sub(add(add(mul(u.ONE, v.ONE), mul(u.e12, v.e12)), mul(u.e2, v.e2)), mul(u.e1, v.e1)), sub(add(add(mul(u.ONE, v.e1), mul(u.e1, v.ONE)), mul(u.e12, v.e2)), mul(u.e2, v.e12)), sub(add(add(mul(u.ONE, v.e2), mul(u.e12, v.e1)), mul(u.e2, v.ONE)), mul(u.e1, v.e12)), sub(add(add(mul(u.ONE, v.e12), mul(u.e1, v.e2)), mul(u.e12, v.ONE)), mul(u.e2, v.e1)));
}

ComplexCl1_1 mul(int a, ComplexCl1_1 x){
    return mul(float(a), x);
}

ComplexCl1_1 dual(ComplexCl1_1 u){
    return ComplexCl1_1(u.e12, mul(-1, u.e2), mul(-1, u.e1), u.ONE);
}

ComplexCl1_1 involve(ComplexCl1_1 u){
    return ComplexCl1_1(u.ONE, mul(-1, u.e1), mul(-1, u.e2), u.e12);
}

ComplexCl1_1 inner(ComplexCl1_1 u, ComplexCl1_1 v){
    return ComplexCl1_1(sub(add(mul(u.e12, v.e12), mul(u.e2, v.e2)), mul(u.e1, v.e1)), sub(mul(u.e12, v.e2), mul(u.e2, v.e12)), sub(mul(u.e12, v.e1), mul(u.e1, v.e12)), 0);
}

ComplexCl1_1 lcontract(ComplexCl1_1 u, ComplexCl1_1 v){
    return ComplexCl1_1(sub(add(add(mul(u.ONE, v.ONE), mul(u.e12, v.e12)), mul(u.e2, v.e2)), mul(u.e1, v.e1)), sub(mul(u.ONE, v.e1), mul(u.e2, v.e12)), sub(mul(u.ONE, v.e2), mul(u.e1, v.e12)), mul(u.ONE, v.e12));
}

ComplexCl1_1 outer(ComplexCl1_1 u, ComplexCl1_1 v){
    return ComplexCl1_1(mul(u.ONE, v.ONE), add(mul(u.ONE, v.e1), mul(u.e1, v.ONE)), add(mul(u.ONE, v.e2), mul(u.e2, v.ONE)), sub(add(add(mul(u.ONE, v.e12), mul(u.e1, v.e2)), mul(u.e12, v.ONE)), mul(u.e2, v.e1)));
}

ComplexCl1_1 I(){
    return ComplexCl1_1(0, 0, 0, 1);
}

ComplexCl1_1 rcontract(ComplexCl1_1 u, ComplexCl1_1 v){
    return ComplexCl1_1(sub(add(add(mul(u.ONE, v.ONE), mul(u.e12, v.e12)), mul(u.e2, v.e2)), mul(u.e1, v.e1)), add(mul(u.e1, v.ONE), mul(u.e12, v.e2)), add(mul(u.e12, v.e1), mul(u.e2, v.ONE)), mul(u.e12, v.ONE));
}

ComplexCl1_1 reverse(ComplexCl1_1 u){
    return ComplexCl1_1(u.ONE, u.e1, u.e2, mul(-1, u.e12));
}

ComplexCl1_1 conjugate(ComplexCl1_1 u){
    return reverse(involve(u));
}
'''

snapshots['TestCliffordAlgebra::test_clifford_algebra_product 1'] = '''ComplexCl1_1 mul(ComplexCl1_1 u, ComplexCl1_1 v){
    return ComplexCl1_1(u.ONE*v.ONE - u.e1*v.e1 + u.e12*v.e12 + u.e2*v.e2, u.ONE*v.e1 + u.e1*v.ONE + u.e12*v.e2 - u.e2*v.e12, u.ONE*v.e2 - u.e1*v.e12 + u.e12*v.e1 + u.e2*v.ONE, u.ONE*v.e12 + u.e1*v.e2 + u.e12*v.ONE - u.e2*v.e1);
}'''

snapshots['TestCliffordAlgebra::test_clifford_algebra_product 2'] = '''ComplexCl1_1 reverse(ComplexCl1_1 u){
    return ComplexCl1_1(u.ONE, u.e1, u.e2, -u.e12);
}'''

snapshots['TestComplexNumbers::test_one 1'] = '''C one(){
    return C(1.0, 0.0);
}'''

snapshots['TestComplexNumbers::test_product 1'] = '''C mul(C u, C v){
    return C(-u.imag*v.imag + u.real*v.real, u.imag*v.real + u.real*v.imag);
}'''

snapshots['TestDualNumbers::test_one 1'] = '''Dual one(){
    return Dual(1.0, 0.0);
}'''

snapshots['TestDualNumbers::test_product 1'] = '''Dual mul(Dual u, Dual v){
    return Dual(u.real*v.real, u.nilpotent*v.real + u.real*v.nilpotent);
}'''
