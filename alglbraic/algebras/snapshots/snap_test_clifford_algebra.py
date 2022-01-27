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

CGA2 fromArray(float X[16]){
    return CGA2(X[0], X[1], X[2], X[3], X[4], X[5], X[6], X[7], X[8], X[9], X[10], X[11], X[12], X[13], X[14], X[15]);
}

void toArray(CGA2 X, inout float X_ary[16]){
    X_ary[0] = X.scalar;
    X_ary[1] = X.e1;
    X_ary[2] = X.e2;
    X_ary[3] = X.enil;
    X_ary[4] = X.einf;
    X_ary[5] = X.e12;
    X_ary[6] = X.e1nil;
    X_ary[7] = X.e1inf;
    X_ary[8] = X.e2nil;
    X_ary[9] = X.e2inf;
    X_ary[10] = X.enilinf;
    X_ary[11] = X.e12nil;
    X_ary[12] = X.e12inf;
    X_ary[13] = X.e1nilinf;
    X_ary[14] = X.e2nilinf;
    X_ary[15] = X.e12nilinf;
}

void zero(inout float X[16]){
    X[0] = 0.0;
    X[1] = 0.0;
    X[2] = 0.0;
    X[3] = 0.0;
    X[4] = 0.0;
    X[5] = 0.0;
    X[6] = 0.0;
    X[7] = 0.0;
    X[8] = 0.0;
    X[9] = 0.0;
    X[10] = 0.0;
    X[11] = 0.0;
    X[12] = 0.0;
    X[13] = 0.0;
    X[14] = 0.0;
    X[15] = 0.0;
}

CGA2 add(CGA2 X, CGA2 Y){
    return CGA2(X.scalar + Y.scalar, X.e1 + Y.e1, X.e2 + Y.e2, X.enil + Y.enil, X.einf + Y.einf, X.e12 + Y.e12, X.e1nil + Y.e1nil, X.e1inf + Y.e1inf, X.e2nil + Y.e2nil, X.e2inf + Y.e2inf, X.enilinf + Y.enilinf, X.e12nil + Y.e12nil, X.e12inf + Y.e12inf, X.e1nilinf + Y.e1nilinf, X.e2nilinf + Y.e2nilinf, X.e12nilinf + Y.e12nilinf);
}

CGA2 add(CGA2 X, CGA2 Y, CGA2 Z){
    return add(add(X, Y), Z);
}

CGA2 add(CGA2 X, CGA2 Y, CGA2 Z, CGA2 P){
    return add(add(add(X, Y), Z), P);
}

CGA2 one(){
    return CGA2(1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
}



CGA2 sub(CGA2 X, CGA2 Y){
    return CGA2(X.scalar - Y.scalar, X.e1 - Y.e1, X.e2 - Y.e2, X.enil - Y.enil, X.einf - Y.einf, X.e12 - Y.e12, X.e1nil - Y.e1nil, X.e1inf - Y.e1inf, X.e2nil - Y.e2nil, X.e2inf - Y.e2inf, X.enilinf - Y.enilinf, X.e12nil - Y.e12nil, X.e12inf - Y.e12inf, X.e1nilinf - Y.e1nilinf, X.e2nilinf - Y.e2nilinf, X.e12nilinf - Y.e12nilinf);
}

CGA2 zero(){
    return CGA2(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
}

CGA2 mul(float a, CGA2 X){
    return CGA2(X.scalar*a, X.e1*a, X.e2*a, X.enil*a, X.einf*a, X.e12*a, X.e1nil*a, X.e1inf*a, X.e2nil*a, X.e2inf*a, X.enilinf*a, X.e12nil*a, X.e12inf*a, X.e1nilinf*a, X.e2nilinf*a, X.e12nilinf*a);
}

CGA2 mul(CGA2 X, CGA2 Y){
    return CGA2(X.e1*Y.e1 - X.e12*Y.e12 - X.e12inf*Y.e12nil - X.e12nil*Y.e12inf - X.e12nilinf*Y.e12nilinf - X.e1inf*Y.e1nil - X.e1nil*Y.e1inf + X.e1nilinf*Y.e1nilinf + X.e2*Y.e2 - X.e2inf*Y.e2nil - X.e2nil*Y.e2inf + X.e2nilinf*Y.e2nilinf + X.einf*Y.enil + X.enil*Y.einf + X.enilinf*Y.enilinf + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2 - X.e12inf*Y.e2nil - X.e12nil*Y.e2inf + X.e12nilinf*Y.e2nilinf + X.e1inf*Y.enil + X.e1nil*Y.einf + X.e1nilinf*Y.enilinf - X.e2*Y.e12 - X.e2inf*Y.e12nil - X.e2nil*Y.e12inf - X.e2nilinf*Y.e12nilinf - X.einf*Y.e1nil - X.enil*Y.e1inf + X.enilinf*Y.e1nilinf + X.scalar*Y.e1, X.e1*Y.e12 - X.e12*Y.e1 + X.e12inf*Y.e1nil + X.e12nil*Y.e1inf - X.e12nilinf*Y.e1nilinf + X.e1inf*Y.e12nil + X.e1nil*Y.e12inf + X.e1nilinf*Y.e12nilinf + X.e2*Y.scalar + X.e2inf*Y.enil + X.e2nil*Y.einf + X.e2nilinf*Y.enilinf - X.einf*Y.e2nil - X.enil*Y.e2inf + X.enilinf*Y.e2nilinf + X.scalar*Y.e2, X.e1*Y.e1nil - X.e12*Y.e12nil - X.e12nil*Y.e12 + X.e12nil*Y.e12nilinf - X.e12nilinf*Y.e12nil - X.e1nil*Y.e1 + X.e1nil*Y.e1nilinf + X.e1nilinf*Y.e1nil + X.e2*Y.e2nil - X.e2nil*Y.e2 + X.e2nil*Y.e2nilinf + X.e2nilinf*Y.e2nil - X.enil*Y.enilinf + X.enil*Y.scalar + X.enilinf*Y.enil + X.scalar*Y.enil, X.e1*Y.e1inf - X.e12*Y.e12inf - X.e12inf*Y.e12 - X.e12inf*Y.e12nilinf + X.e12nilinf*Y.e12inf - X.e1inf*Y.e1 - X.e1inf*Y.e1nilinf - X.e1nilinf*Y.e1inf + X.e2*Y.e2inf - X.e2inf*Y.e2 - X.e2inf*Y.e2nilinf - X.e2nilinf*Y.e2inf + X.einf*Y.enilinf + X.einf*Y.scalar - X.enilinf*Y.einf + X.scalar*Y.einf, X.e1*Y.e2 + X.e12*Y.scalar + X.e12inf*Y.enil + X.e12nil*Y.einf + X.e12nilinf*Y.enilinf - X.e1inf*Y.e2nil - X.e1nil*Y.e2inf + X.e1nilinf*Y.e2nilinf - X.e2*Y.e1 + X.e2inf*Y.e1nil + X.e2nil*Y.e1inf - X.e2nilinf*Y.e1nilinf + X.einf*Y.e12nil + X.enil*Y.e12inf + X.enilinf*Y.e12nilinf + X.scalar*Y.e12, X.e1*Y.enil + X.e12*Y.e2nil - X.e12nil*Y.e2 + X.e12nil*Y.e2nilinf + X.e12nilinf*Y.e2nil - X.e1nil*Y.enilinf + X.e1nil*Y.scalar + X.e1nilinf*Y.enil - X.e2*Y.e12nil - X.e2nil*Y.e12 + X.e2nil*Y.e12nilinf - X.e2nilinf*Y.e12nil - X.enil*Y.e1 + X.enil*Y.e1nilinf + X.enilinf*Y.e1nil + X.scalar*Y.e1nil, X.e1*Y.einf + X.e12*Y.e2inf - X.e12inf*Y.e2 - X.e12inf*Y.e2nilinf - X.e12nilinf*Y.e2inf + X.e1inf*Y.enilinf + X.e1inf*Y.scalar - X.e1nilinf*Y.einf - X.e2*Y.e12inf - X.e2inf*Y.e12 - X.e2inf*Y.e12nilinf + X.e2nilinf*Y.e12inf - X.einf*Y.e1 - X.einf*Y.e1nilinf - X.enilinf*Y.e1inf + X.scalar*Y.e1inf, X.e1*Y.e12nil - X.e12*Y.e1nil + X.e12nil*Y.e1 - X.e12nil*Y.e1nilinf - X.e12nilinf*Y.e1nil + X.e1nil*Y.e12 - X.e1nil*Y.e12nilinf + X.e1nilinf*Y.e12nil + X.e2*Y.enil - X.e2nil*Y.enilinf + X.e2nil*Y.scalar + X.e2nilinf*Y.enil - X.enil*Y.e2 + X.enil*Y.e2nilinf + X.enilinf*Y.e2nil + X.scalar*Y.e2nil, X.e1*Y.e12inf - X.e12*Y.e1inf + X.e12inf*Y.e1 + X.e12inf*Y.e1nilinf + X.e12nilinf*Y.e1inf + X.e1inf*Y.e12 + X.e1inf*Y.e12nilinf - X.e1nilinf*Y.e12inf + X.e2*Y.einf + X.e2inf*Y.enilinf + X.e2inf*Y.scalar - X.e2nilinf*Y.einf - X.einf*Y.e2 - X.einf*Y.e2nilinf - X.enilinf*Y.e2inf + X.scalar*Y.e2inf, X.e1*Y.e1nilinf - X.e12*Y.e12nilinf + X.e12inf*Y.e12nil - X.e12nil*Y.e12inf - X.e12nilinf*Y.e12 + X.e1inf*Y.e1nil - X.e1nil*Y.e1inf + X.e1nilinf*Y.e1 + X.e2*Y.e2nilinf + X.e2inf*Y.e2nil - X.e2nil*Y.e2inf + X.e2nilinf*Y.e2 - X.einf*Y.enil + X.enil*Y.einf + X.enilinf*Y.scalar + X.scalar*Y.enilinf, X.e1*Y.e2nil + X.e12*Y.enil - X.e12nil*Y.enilinf + X.e12nil*Y.scalar + X.e12nilinf*Y.enil - X.e1nil*Y.e2 + X.e1nil*Y.e2nilinf + X.e1nilinf*Y.e2nil - X.e2*Y.e1nil + X.e2nil*Y.e1 - X.e2nil*Y.e1nilinf - X.e2nilinf*Y.e1nil + X.enil*Y.e12 - X.enil*Y.e12nilinf + X.enilinf*Y.e12nil + X.scalar*Y.e12nil, X.e1*Y.e2inf + X.e12*Y.einf + X.e12inf*Y.enilinf + X.e12inf*Y.scalar - X.e12nilinf*Y.einf - X.e1inf*Y.e2 - X.e1inf*Y.e2nilinf - X.e1nilinf*Y.e2inf - X.e2*Y.e1inf + X.e2inf*Y.e1 + X.e2inf*Y.e1nilinf + X.e2nilinf*Y.e1inf + X.einf*Y.e12 + X.einf*Y.e12nilinf - X.enilinf*Y.e12inf + X.scalar*Y.e12inf, X.e1*Y.enilinf + X.e12*Y.e2nilinf + X.e12inf*Y.e2nil - X.e12nil*Y.e2inf + X.e12nilinf*Y.e2 - X.e1inf*Y.enil + X.e1nil*Y.einf + X.e1nilinf*Y.scalar - X.e2*Y.e12nilinf + X.e2inf*Y.e12nil - X.e2nil*Y.e12inf - X.e2nilinf*Y.e12 + X.einf*Y.e1nil - X.enil*Y.e1inf + X.enilinf*Y.e1 + X.scalar*Y.e1nilinf, X.e1*Y.e12nilinf - X.e12*Y.e1nilinf - X.e12inf*Y.e1nil + X.e12nil*Y.e1inf - X.e12nilinf*Y.e1 - X.e1inf*Y.e12nil + X.e1nil*Y.e12inf + X.e1nilinf*Y.e12 + X.e2*Y.enilinf - X.e2inf*Y.enil + X.e2nil*Y.einf + X.e2nilinf*Y.scalar + X.einf*Y.e2nil - X.enil*Y.e2inf + X.enilinf*Y.e2 + X.scalar*Y.e2nilinf, X.e1*Y.e2nilinf + X.e12*Y.enilinf - X.e12inf*Y.enil + X.e12nil*Y.einf + X.e12nilinf*Y.scalar + X.e1inf*Y.e2nil - X.e1nil*Y.e2inf + X.e1nilinf*Y.e2 - X.e2*Y.e1nilinf - X.e2inf*Y.e1nil + X.e2nil*Y.e1inf - X.e2nilinf*Y.e1 - X.einf*Y.e12nil + X.enil*Y.e12inf + X.enilinf*Y.e12 + X.scalar*Y.e12nilinf);
}

CGA2 mul(int a, CGA2 X){
    return mul(float(a), X);
}

CGA2 mul(CGA2 X, CGA2 Y, CGA2 Z){
    return mul(mul(X, Y), Z);
}

CGA2 dual(CGA2 X){
    return CGA2(X.e12nilinf, X.e2nilinf, -X.e1nilinf, -X.e12nil, X.e12inf, -X.enilinf, -X.e2nil, X.e2inf, X.e1nil, -X.e1inf, X.e12, X.enil, -X.einf, X.e2, -X.e1, -X.scalar);
}

CGA2 involve(CGA2 X){
    return CGA2(X.scalar, -X.e1, -X.e2, -X.enil, -X.einf, X.e12, X.e1nil, X.e1inf, X.e2nil, X.e2inf, X.enilinf, -X.e12nil, -X.e12inf, -X.e1nilinf, -X.e2nilinf, X.e12nilinf);
}

CGA2 inner(CGA2 X, CGA2 Y){
    return CGA2(X.e1*Y.e1 - X.e12*Y.e12 - X.e12inf*Y.e12nil - X.e12nil*Y.e12inf - X.e12nilinf*Y.e12nilinf - X.e1inf*Y.e1nil - X.e1nil*Y.e1inf + X.e1nilinf*Y.e1nilinf + X.e2*Y.e2 - X.e2inf*Y.e2nil - X.e2nil*Y.e2inf + X.e2nilinf*Y.e2nilinf + X.einf*Y.enil + X.enil*Y.einf + X.enilinf*Y.enilinf, X.e12*Y.e2 - X.e12inf*Y.e2nil - X.e12nil*Y.e2inf + X.e12nilinf*Y.e2nilinf + X.e1inf*Y.enil + X.e1nil*Y.einf + X.e1nilinf*Y.enilinf - X.e2*Y.e12 - X.e2inf*Y.e12nil - X.e2nil*Y.e12inf - X.e2nilinf*Y.e12nilinf - X.einf*Y.e1nil - X.enil*Y.e1inf + X.enilinf*Y.e1nilinf, X.e1*Y.e12 - X.e12*Y.e1 + X.e12inf*Y.e1nil + X.e12nil*Y.e1inf - X.e12nilinf*Y.e1nilinf + X.e1inf*Y.e12nil + X.e1nil*Y.e12inf + X.e1nilinf*Y.e12nilinf + X.e2inf*Y.enil + X.e2nil*Y.einf + X.e2nilinf*Y.enilinf - X.einf*Y.e2nil - X.enil*Y.e2inf + X.enilinf*Y.e2nilinf, X.e1*Y.e1nil - X.e12*Y.e12nil - X.e12nil*Y.e12 + X.e12nil*Y.e12nilinf - X.e12nilinf*Y.e12nil - X.e1nil*Y.e1 + X.e1nil*Y.e1nilinf + X.e1nilinf*Y.e1nil + X.e2*Y.e2nil - X.e2nil*Y.e2 + X.e2nil*Y.e2nilinf + X.e2nilinf*Y.e2nil - X.enil*Y.enilinf + X.enilinf*Y.enil, X.e1*Y.e1inf - X.e12*Y.e12inf - X.e12inf*Y.e12 - X.e12inf*Y.e12nilinf + X.e12nilinf*Y.e12inf - X.e1inf*Y.e1 - X.e1inf*Y.e1nilinf - X.e1nilinf*Y.e1inf + X.e2*Y.e2inf - X.e2inf*Y.e2 - X.e2inf*Y.e2nilinf - X.e2nilinf*Y.e2inf + X.einf*Y.enilinf - X.enilinf*Y.einf, X.e12inf*Y.enil + X.e12nil*Y.einf + X.e12nilinf*Y.enilinf + X.einf*Y.e12nil + X.enil*Y.e12inf + X.enilinf*Y.e12nilinf, -X.e12nil*Y.e2 + X.e12nilinf*Y.e2nil + X.e1nilinf*Y.enil - X.e2*Y.e12nil + X.e2nil*Y.e12nilinf + X.enil*Y.e1nilinf, -X.e12inf*Y.e2 - X.e12nilinf*Y.e2inf - X.e1nilinf*Y.einf - X.e2*Y.e12inf - X.e2inf*Y.e12nilinf - X.einf*Y.e1nilinf, X.e1*Y.e12nil + X.e12nil*Y.e1 - X.e12nilinf*Y.e1nil - X.e1nil*Y.e12nilinf + X.e2nilinf*Y.enil + X.enil*Y.e2nilinf, X.e1*Y.e12inf + X.e12inf*Y.e1 + X.e12nilinf*Y.e1inf + X.e1inf*Y.e12nilinf - X.e2nilinf*Y.einf - X.einf*Y.e2nilinf, X.e1*Y.e1nilinf - X.e12*Y.e12nilinf - X.e12nilinf*Y.e12 + X.e1nilinf*Y.e1 + X.e2*Y.e2nilinf + X.e2nilinf*Y.e2, X.e12nilinf*Y.enil - X.enil*Y.e12nilinf, -X.e12nilinf*Y.einf + X.einf*Y.e12nilinf, X.e12nilinf*Y.e2 - X.e2*Y.e12nilinf, X.e1*Y.e12nilinf - X.e12nilinf*Y.e1, 0.0);
}

CGA2 lcontract(CGA2 X, CGA2 Y){
    return CGA2(X.e1*Y.e1 - X.e12*Y.e12 - X.e12inf*Y.e12nil - X.e12nil*Y.e12inf - X.e12nilinf*Y.e12nilinf - X.e1inf*Y.e1nil - X.e1nil*Y.e1inf + X.e1nilinf*Y.e1nilinf + X.e2*Y.e2 - X.e2inf*Y.e2nil - X.e2nil*Y.e2inf + X.e2nilinf*Y.e2nilinf + X.einf*Y.enil + X.enil*Y.einf + X.enilinf*Y.enilinf + X.scalar*Y.scalar, -X.e2*Y.e12 - X.e2inf*Y.e12nil - X.e2nil*Y.e12inf - X.e2nilinf*Y.e12nilinf - X.einf*Y.e1nil - X.enil*Y.e1inf + X.enilinf*Y.e1nilinf + X.scalar*Y.e1, X.e1*Y.e12 + X.e1inf*Y.e12nil + X.e1nil*Y.e12inf + X.e1nilinf*Y.e12nilinf - X.einf*Y.e2nil - X.enil*Y.e2inf + X.enilinf*Y.e2nilinf + X.scalar*Y.e2, X.e1*Y.e1nil - X.e12*Y.e12nil + X.e12nil*Y.e12nilinf + X.e1nil*Y.e1nilinf + X.e2*Y.e2nil + X.e2nil*Y.e2nilinf - X.enil*Y.enilinf + X.scalar*Y.enil, X.e1*Y.e1inf - X.e12*Y.e12inf - X.e12inf*Y.e12nilinf - X.e1inf*Y.e1nilinf + X.e2*Y.e2inf - X.e2inf*Y.e2nilinf + X.einf*Y.enilinf + X.scalar*Y.einf, X.einf*Y.e12nil + X.enil*Y.e12inf + X.enilinf*Y.e12nilinf + X.scalar*Y.e12, -X.e2*Y.e12nil + X.e2nil*Y.e12nilinf + X.enil*Y.e1nilinf + X.scalar*Y.e1nil, -X.e2*Y.e12inf - X.e2inf*Y.e12nilinf - X.einf*Y.e1nilinf + X.scalar*Y.e1inf, X.e1*Y.e12nil - X.e1nil*Y.e12nilinf + X.enil*Y.e2nilinf + X.scalar*Y.e2nil, X.e1*Y.e12inf + X.e1inf*Y.e12nilinf - X.einf*Y.e2nilinf + X.scalar*Y.e2inf, X.e1*Y.e1nilinf - X.e12*Y.e12nilinf + X.e2*Y.e2nilinf + X.scalar*Y.enilinf, -X.enil*Y.e12nilinf + X.scalar*Y.e12nil, X.einf*Y.e12nilinf + X.scalar*Y.e12inf, -X.e2*Y.e12nilinf + X.scalar*Y.e1nilinf, X.e1*Y.e12nilinf + X.scalar*Y.e2nilinf, X.scalar*Y.e12nilinf);
}

CGA2 outer(CGA2 X, CGA2 Y){
    return CGA2(X.scalar*Y.scalar, X.e1*Y.scalar + X.scalar*Y.e1, X.e2*Y.scalar + X.scalar*Y.e2, X.enil*Y.scalar + X.scalar*Y.enil, X.einf*Y.scalar + X.scalar*Y.einf, X.e1*Y.e2 + X.e12*Y.scalar - X.e2*Y.e1 + X.scalar*Y.e12, X.e1*Y.enil + X.e1nil*Y.scalar - X.enil*Y.e1 + X.scalar*Y.e1nil, X.e1*Y.einf + X.e1inf*Y.scalar - X.einf*Y.e1 + X.scalar*Y.e1inf, X.e2*Y.enil + X.e2nil*Y.scalar - X.enil*Y.e2 + X.scalar*Y.e2nil, X.e2*Y.einf + X.e2inf*Y.scalar - X.einf*Y.e2 + X.scalar*Y.e2inf, -X.einf*Y.enil + X.enil*Y.einf + X.enilinf*Y.scalar + X.scalar*Y.enilinf, X.e1*Y.e2nil + X.e12*Y.enil + X.e12nil*Y.scalar - X.e1nil*Y.e2 - X.e2*Y.e1nil + X.e2nil*Y.e1 + X.enil*Y.e12 + X.scalar*Y.e12nil, X.e1*Y.e2inf + X.e12*Y.einf + X.e12inf*Y.scalar - X.e1inf*Y.e2 - X.e2*Y.e1inf + X.e2inf*Y.e1 + X.einf*Y.e12 + X.scalar*Y.e12inf, X.e1*Y.enilinf - X.e1inf*Y.enil + X.e1nil*Y.einf + X.e1nilinf*Y.scalar + X.einf*Y.e1nil - X.enil*Y.e1inf + X.enilinf*Y.e1 + X.scalar*Y.e1nilinf, X.e2*Y.enilinf - X.e2inf*Y.enil + X.e2nil*Y.einf + X.e2nilinf*Y.scalar + X.einf*Y.e2nil - X.enil*Y.e2inf + X.enilinf*Y.e2 + X.scalar*Y.e2nilinf, X.e1*Y.e2nilinf + X.e12*Y.enilinf - X.e12inf*Y.enil + X.e12nil*Y.einf + X.e12nilinf*Y.scalar + X.e1inf*Y.e2nil - X.e1nil*Y.e2inf + X.e1nilinf*Y.e2 - X.e2*Y.e1nilinf - X.e2inf*Y.e1nil + X.e2nil*Y.e1inf - X.e2nilinf*Y.e1 - X.einf*Y.e12nil + X.enil*Y.e12inf + X.enilinf*Y.e12 + X.scalar*Y.e12nilinf);
}

CGA2 I(){
    return CGA2(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0);
}

CGA2 rcontract(CGA2 X, CGA2 Y){
    return CGA2(X.e1*Y.e1 - X.e12*Y.e12 - X.e12inf*Y.e12nil - X.e12nil*Y.e12inf - X.e12nilinf*Y.e12nilinf - X.e1inf*Y.e1nil - X.e1nil*Y.e1inf + X.e1nilinf*Y.e1nilinf + X.e2*Y.e2 - X.e2inf*Y.e2nil - X.e2nil*Y.e2inf + X.e2nilinf*Y.e2nilinf + X.einf*Y.enil + X.enil*Y.einf + X.enilinf*Y.enilinf + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2 - X.e12inf*Y.e2nil - X.e12nil*Y.e2inf + X.e12nilinf*Y.e2nilinf + X.e1inf*Y.enil + X.e1nil*Y.einf + X.e1nilinf*Y.enilinf, -X.e12*Y.e1 + X.e12inf*Y.e1nil + X.e12nil*Y.e1inf - X.e12nilinf*Y.e1nilinf + X.e2*Y.scalar + X.e2inf*Y.enil + X.e2nil*Y.einf + X.e2nilinf*Y.enilinf, -X.e12nil*Y.e12 - X.e12nilinf*Y.e12nil - X.e1nil*Y.e1 + X.e1nilinf*Y.e1nil - X.e2nil*Y.e2 + X.e2nilinf*Y.e2nil + X.enil*Y.scalar + X.enilinf*Y.enil, -X.e12inf*Y.e12 + X.e12nilinf*Y.e12inf - X.e1inf*Y.e1 - X.e1nilinf*Y.e1inf - X.e2inf*Y.e2 - X.e2nilinf*Y.e2inf + X.einf*Y.scalar - X.enilinf*Y.einf, X.e12*Y.scalar + X.e12inf*Y.enil + X.e12nil*Y.einf + X.e12nilinf*Y.enilinf, -X.e12nil*Y.e2 + X.e12nilinf*Y.e2nil + X.e1nil*Y.scalar + X.e1nilinf*Y.enil, -X.e12inf*Y.e2 - X.e12nilinf*Y.e2inf + X.e1inf*Y.scalar - X.e1nilinf*Y.einf, X.e12nil*Y.e1 - X.e12nilinf*Y.e1nil + X.e2nil*Y.scalar + X.e2nilinf*Y.enil, X.e12inf*Y.e1 + X.e12nilinf*Y.e1inf + X.e2inf*Y.scalar - X.e2nilinf*Y.einf, -X.e12nilinf*Y.e12 + X.e1nilinf*Y.e1 + X.e2nilinf*Y.e2 + X.enilinf*Y.scalar, X.e12nil*Y.scalar + X.e12nilinf*Y.enil, X.e12inf*Y.scalar - X.e12nilinf*Y.einf, X.e12nilinf*Y.e2 + X.e1nilinf*Y.scalar, -X.e12nilinf*Y.e1 + X.e2nilinf*Y.scalar, X.e12nilinf*Y.scalar);
}

CGA2 reverse(CGA2 X){
    return CGA2(X.scalar, X.e1, X.e2, X.enil, X.einf, -X.e12, -X.e1nil, -X.e1inf, -X.e2nil, -X.e2inf, -X.enilinf, -X.e12nil, -X.e12inf, -X.e1nilinf, -X.e2nilinf, X.e12nilinf);
}

CGA2 conjugate(CGA2 X){
    return reverse(involve(X));
}

CGA2 outer(CGA2 X, CGA2 Y, CGA2 Z){
    return outer(outer(X, Y), Z);
}
'''

snapshots['TestCliffordAlgebra::test_big_clifford_algebra_product 1'] = '''ComplexCl4 mul(ComplexCl4 X, ComplexCl4 Y){
    return ComplexCl4(X.ONE*Y.ONE + X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 + X.e1234*Y.e1234 - X.e124*Y.e124 - X.e13*Y.e13 - X.e134*Y.e134 - X.e14*Y.e14 + X.e2*Y.e2 - X.e23*Y.e23 - X.e234*Y.e234 - X.e24*Y.e24 + X.e3*Y.e3 - X.e34*Y.e34 + X.e4*Y.e4, X.ONE*Y.e1 + X.e1*Y.ONE + X.e12*Y.e2 - X.e123*Y.e23 - X.e1234*Y.e234 - X.e124*Y.e24 + X.e13*Y.e3 - X.e134*Y.e34 + X.e14*Y.e4 - X.e2*Y.e12 - X.e23*Y.e123 + X.e234*Y.e1234 - X.e24*Y.e124 - X.e3*Y.e13 - X.e34*Y.e134 - X.e4*Y.e14, X.ONE*Y.e2 + X.e1*Y.e12 - X.e12*Y.e1 + X.e123*Y.e13 + X.e1234*Y.e134 + X.e124*Y.e14 + X.e13*Y.e123 - X.e134*Y.e1234 + X.e14*Y.e124 + X.e2*Y.ONE + X.e23*Y.e3 - X.e234*Y.e34 + X.e24*Y.e4 - X.e3*Y.e23 - X.e34*Y.e234 - X.e4*Y.e24, X.ONE*Y.e3 + X.e1*Y.e13 - X.e12*Y.e123 - X.e123*Y.e12 - X.e1234*Y.e124 + X.e124*Y.e1234 - X.e13*Y.e1 + X.e134*Y.e14 + X.e14*Y.e134 + X.e2*Y.e23 - X.e23*Y.e2 + X.e234*Y.e24 + X.e24*Y.e234 + X.e3*Y.ONE + X.e34*Y.e4 - X.e4*Y.e34, X.ONE*Y.e4 + X.e1*Y.e14 - X.e12*Y.e124 - X.e123*Y.e1234 + X.e1234*Y.e123 - X.e124*Y.e12 - X.e13*Y.e134 - X.e134*Y.e13 - X.e14*Y.e1 + X.e2*Y.e24 - X.e23*Y.e234 - X.e234*Y.e23 - X.e24*Y.e2 + X.e3*Y.e34 - X.e34*Y.e3 + X.e4*Y.ONE, X.ONE*Y.e12 + X.e1*Y.e2 + X.e12*Y.ONE + X.e123*Y.e3 - X.e1234*Y.e34 + X.e124*Y.e4 - X.e13*Y.e23 - X.e134*Y.e234 - X.e14*Y.e24 - X.e2*Y.e1 + X.e23*Y.e13 + X.e234*Y.e134 + X.e24*Y.e14 + X.e3*Y.e123 - X.e34*Y.e1234 + X.e4*Y.e124, X.ONE*Y.e13 + X.e1*Y.e3 + X.e12*Y.e23 - X.e123*Y.e2 + X.e1234*Y.e24 + X.e124*Y.e234 + X.e13*Y.ONE + X.e134*Y.e4 - X.e14*Y.e34 - X.e2*Y.e123 - X.e23*Y.e12 - X.e234*Y.e124 + X.e24*Y.e1234 - X.e3*Y.e1 + X.e34*Y.e14 + X.e4*Y.e134, X.ONE*Y.e14 + X.e1*Y.e4 + X.e12*Y.e24 - X.e123*Y.e234 - X.e1234*Y.e23 - X.e124*Y.e2 + X.e13*Y.e34 - X.e134*Y.e3 + X.e14*Y.ONE - X.e2*Y.e124 - X.e23*Y.e1234 + X.e234*Y.e123 - X.e24*Y.e12 - X.e3*Y.e134 - X.e34*Y.e13 - X.e4*Y.e1, X.ONE*Y.e23 + X.e1*Y.e123 - X.e12*Y.e13 + X.e123*Y.e1 - X.e1234*Y.e14 - X.e124*Y.e134 + X.e13*Y.e12 + X.e134*Y.e124 - X.e14*Y.e1234 + X.e2*Y.e3 + X.e23*Y.ONE + X.e234*Y.e4 - X.e24*Y.e34 - X.e3*Y.e2 + X.e34*Y.e24 + X.e4*Y.e234, X.ONE*Y.e24 + X.e1*Y.e124 - X.e12*Y.e14 + X.e123*Y.e134 + X.e1234*Y.e13 + X.e124*Y.e1 + X.e13*Y.e1234 - X.e134*Y.e123 + X.e14*Y.e12 + X.e2*Y.e4 + X.e23*Y.e34 - X.e234*Y.e3 + X.e24*Y.ONE - X.e3*Y.e234 - X.e34*Y.e23 - X.e4*Y.e2, X.ONE*Y.e34 + X.e1*Y.e134 - X.e12*Y.e1234 - X.e123*Y.e124 - X.e1234*Y.e12 + X.e124*Y.e123 - X.e13*Y.e14 + X.e134*Y.e1 + X.e14*Y.e13 + X.e2*Y.e234 - X.e23*Y.e24 + X.e234*Y.e2 + X.e24*Y.e23 + X.e3*Y.e4 + X.e34*Y.ONE - X.e4*Y.e3, X.ONE*Y.e123 + X.e1*Y.e23 + X.e12*Y.e3 + X.e123*Y.ONE + X.e1234*Y.e4 - X.e124*Y.e34 - X.e13*Y.e2 + X.e134*Y.e24 + X.e14*Y.e234 - X.e2*Y.e13 + X.e23*Y.e1 - X.e234*Y.e14 - X.e24*Y.e134 + X.e3*Y.e12 + X.e34*Y.e124 - X.e4*Y.e1234, X.ONE*Y.e124 + X.e1*Y.e24 + X.e12*Y.e4 + X.e123*Y.e34 - X.e1234*Y.e3 + X.e124*Y.ONE - X.e13*Y.e234 - X.e134*Y.e23 - X.e14*Y.e2 - X.e2*Y.e14 + X.e23*Y.e134 + X.e234*Y.e13 + X.e24*Y.e1 + X.e3*Y.e1234 - X.e34*Y.e123 + X.e4*Y.e12, X.ONE*Y.e134 + X.e1*Y.e34 + X.e12*Y.e234 - X.e123*Y.e24 + X.e1234*Y.e2 + X.e124*Y.e23 + X.e13*Y.e4 + X.e134*Y.ONE - X.e14*Y.e3 - X.e2*Y.e1234 - X.e23*Y.e124 - X.e234*Y.e12 + X.e24*Y.e123 - X.e3*Y.e14 + X.e34*Y.e1 + X.e4*Y.e13, X.ONE*Y.e234 + X.e1*Y.e1234 - X.e12*Y.e134 + X.e123*Y.e14 - X.e1234*Y.e1 - X.e124*Y.e13 + X.e13*Y.e124 + X.e134*Y.e12 - X.e14*Y.e123 + X.e2*Y.e34 + X.e23*Y.e4 + X.e234*Y.ONE - X.e24*Y.e3 - X.e3*Y.e24 + X.e34*Y.e2 + X.e4*Y.e23, X.ONE*Y.e1234 + X.e1*Y.e234 + X.e12*Y.e34 + X.e123*Y.e4 + X.e1234*Y.ONE - X.e124*Y.e3 - X.e13*Y.e24 + X.e134*Y.e2 + X.e14*Y.e23 - X.e2*Y.e134 + X.e23*Y.e14 - X.e234*Y.e1 - X.e24*Y.e13 + X.e3*Y.e124 + X.e34*Y.e12 - X.e4*Y.e123);
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

ComplexCl1_1 fromArray(C X[4]){
    return ComplexCl1_1(X[0], X[1], X[2], X[3]);
}

void toArray(ComplexCl1_1 X, inout C X_ary[4]){
    X_ary[0] = X.ONE;
    X_ary[1] = X.e1;
    X_ary[2] = X.e2;
    X_ary[3] = X.e12;
}

void zero(inout C X[4]){
    X[0] = zero();
    X[1] = zero();
    X[2] = zero();
    X[3] = zero();
}

ComplexCl1_1 add(ComplexCl1_1 X, ComplexCl1_1 Y){
    return ComplexCl1_1(add(X.ONE, Y.ONE), add(X.e1, Y.e1), add(X.e2, Y.e2), add(X.e12, Y.e12));
}

ComplexCl1_1 add(ComplexCl1_1 X, ComplexCl1_1 Y, ComplexCl1_1 Z){
    return add(add(X, Y), Z);
}

ComplexCl1_1 add(ComplexCl1_1 X, ComplexCl1_1 Y, ComplexCl1_1 Z, ComplexCl1_1 P){
    return add(add(add(X, Y), Z), P);
}

ComplexCl1_1 one(){
    return ComplexCl1_1(one(), zero(), zero(), zero());
}

ComplexCl1_1 mul(float a, ComplexCl1_1 x){
    return mul(mul(a, one()), x);
}

ComplexCl1_1 sub(ComplexCl1_1 X, ComplexCl1_1 Y){
    return ComplexCl1_1(sub(X.ONE, Y.ONE), sub(X.e1, Y.e1), sub(X.e2, Y.e2), sub(X.e12, Y.e12));
}

ComplexCl1_1 zero(){
    return ComplexCl1_1(zero(), zero(), zero(), zero());
}

ComplexCl1_1 mul(C a, ComplexCl1_1 X){
    return ComplexCl1_1(mul(X.ONE, a), mul(X.e1, a), mul(X.e2, a), mul(X.e12, a));
}

ComplexCl1_1 mul(ComplexCl1_1 X, ComplexCl1_1 Y){
    return ComplexCl1_1(sub(add(add(mul(X.ONE, Y.ONE), mul(X.e12, Y.e12)), mul(X.e2, Y.e2)), mul(X.e1, Y.e1)), sub(add(add(mul(X.ONE, Y.e1), mul(X.e1, Y.ONE)), mul(X.e12, Y.e2)), mul(X.e2, Y.e12)), sub(add(add(mul(X.ONE, Y.e2), mul(X.e12, Y.e1)), mul(X.e2, Y.ONE)), mul(X.e1, Y.e12)), sub(add(add(mul(X.ONE, Y.e12), mul(X.e1, Y.e2)), mul(X.e12, Y.ONE)), mul(X.e2, Y.e1)));
}

ComplexCl1_1 mul(int a, ComplexCl1_1 X){
    return mul(float(a), X);
}

ComplexCl1_1 mul(ComplexCl1_1 X, ComplexCl1_1 Y, ComplexCl1_1 Z){
    return mul(mul(X, Y), Z);
}

ComplexCl1_1 dual(ComplexCl1_1 X){
    return ComplexCl1_1(X.e12, mul(-1, X.e2), mul(-1, X.e1), X.ONE);
}

ComplexCl1_1 involve(ComplexCl1_1 X){
    return ComplexCl1_1(X.ONE, mul(-1, X.e1), mul(-1, X.e2), X.e12);
}

ComplexCl1_1 inner(ComplexCl1_1 X, ComplexCl1_1 Y){
    return ComplexCl1_1(sub(add(mul(X.e12, Y.e12), mul(X.e2, Y.e2)), mul(X.e1, Y.e1)), sub(mul(X.e12, Y.e2), mul(X.e2, Y.e12)), sub(mul(X.e12, Y.e1), mul(X.e1, Y.e12)), 0);
}

ComplexCl1_1 lcontract(ComplexCl1_1 X, ComplexCl1_1 Y){
    return ComplexCl1_1(sub(add(add(mul(X.ONE, Y.ONE), mul(X.e12, Y.e12)), mul(X.e2, Y.e2)), mul(X.e1, Y.e1)), sub(mul(X.ONE, Y.e1), mul(X.e2, Y.e12)), sub(mul(X.ONE, Y.e2), mul(X.e1, Y.e12)), mul(X.ONE, Y.e12));
}

ComplexCl1_1 outer(ComplexCl1_1 X, ComplexCl1_1 Y){
    return ComplexCl1_1(mul(X.ONE, Y.ONE), add(mul(X.ONE, Y.e1), mul(X.e1, Y.ONE)), add(mul(X.ONE, Y.e2), mul(X.e2, Y.ONE)), sub(add(add(mul(X.ONE, Y.e12), mul(X.e1, Y.e2)), mul(X.e12, Y.ONE)), mul(X.e2, Y.e1)));
}

ComplexCl1_1 I(){
    return ComplexCl1_1(0, 0, 0, 1);
}

ComplexCl1_1 rcontract(ComplexCl1_1 X, ComplexCl1_1 Y){
    return ComplexCl1_1(sub(add(add(mul(X.ONE, Y.ONE), mul(X.e12, Y.e12)), mul(X.e2, Y.e2)), mul(X.e1, Y.e1)), add(mul(X.e1, Y.ONE), mul(X.e12, Y.e2)), add(mul(X.e12, Y.e1), mul(X.e2, Y.ONE)), mul(X.e12, Y.ONE));
}

ComplexCl1_1 reverse(ComplexCl1_1 X){
    return ComplexCl1_1(X.ONE, X.e1, X.e2, mul(-1, X.e12));
}

ComplexCl1_1 conjugate(ComplexCl1_1 X){
    return reverse(involve(X));
}

ComplexCl1_1 outer(ComplexCl1_1 X, ComplexCl1_1 Y, ComplexCl1_1 Z){
    return outer(outer(X, Y), Z);
}
'''

snapshots['TestCliffordAlgebra::test_clifford_algebra_product 1'] = '''ComplexCl1_1 mul(ComplexCl1_1 X, ComplexCl1_1 Y){
    return ComplexCl1_1(X.ONE*Y.ONE - X.e1*Y.e1 + X.e12*Y.e12 + X.e2*Y.e2, X.ONE*Y.e1 + X.e1*Y.ONE + X.e12*Y.e2 - X.e2*Y.e12, X.ONE*Y.e2 - X.e1*Y.e12 + X.e12*Y.e1 + X.e2*Y.ONE, X.ONE*Y.e12 + X.e1*Y.e2 + X.e12*Y.ONE - X.e2*Y.e1);
}'''

snapshots['TestCliffordAlgebra::test_clifford_algebra_product 2'] = '''ComplexCl1_1 reverse(ComplexCl1_1 X){
    return ComplexCl1_1(X.ONE, X.e1, X.e2, -X.e12);
}'''

snapshots['TestComplexNumbers::test_one 1'] = '''C one(){
    return C(1.0, 0.0);
}'''

snapshots['TestComplexNumbers::test_product 1'] = '''C mul(C X, C Y){
    return C(-X.imag*Y.imag + X.real*Y.real, X.imag*Y.real + X.real*Y.imag);
}'''

snapshots['TestDualNumbers::test_one 1'] = '''Dual one(){
    return Dual(1.0, 0.0);
}'''

snapshots['TestDualNumbers::test_product 1'] = '''Dual mul(Dual X, Dual Y){
    return Dual(X.real*Y.real, X.nil*Y.real + X.real*Y.nil);
}'''
