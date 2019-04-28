# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCGA::test_bundle 1'] = '''struct CGA2 {
    float scalar; float e1; float e2; float e3; float e4; float e12; float e13; float e14; float e23; float e24; float e34; float e123; float e124; float e134; float e234; float e1234;
}

CGA2 fromArray(float x[16]){
    return CGA2(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15]);
}

float[16] toArray(CGA2 x){
    return float[16](x.scalar, x.e1, x.e2, x.e3, x.e4, x.e12, x.e13, x.e14, x.e23, x.e24, x.e34, x.e123, x.e124, x.e134, x.e234, x.e1234);
}

CGA2 add(CGA2 u, CGA2 v){
    return CGA2(u.scalar + v.scalar, u.e1 + v.e1, u.e2 + v.e2, u.e3 + v.e3, u.e4 + v.e4, u.e12 + v.e12, u.e13 + v.e13, u.e14 + v.e14, u.e23 + v.e23, u.e24 + v.e24, u.e34 + v.e34, u.e123 + v.e123, u.e124 + v.e124, u.e134 + v.e134, u.e234 + v.e234, u.e1234 + v.e1234);
}

CGA2 one(){
    return CGA2(1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
}

CGA2 mul(float a, CGA2 x){
    return mul(mul(a, 1.00000000000000), x);
}

CGA2 sub(CGA2 u, CGA2 v){
    return CGA2(u.scalar - v.scalar, u.e1 - v.e1, u.e2 - v.e2, u.e3 - v.e3, u.e4 - v.e4, u.e12 - v.e12, u.e13 - v.e13, u.e14 - v.e14, u.e23 - v.e23, u.e24 - v.e24, u.e34 - v.e34, u.e123 - v.e123, u.e124 - v.e124, u.e134 - v.e134, u.e234 - v.e234, u.e1234 - v.e1234);
}

CGA2 zero(){
    return CGA2(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);
}

CGA2 mul(float a, CGA2 x){
    return CGA2(a*x.scalar, a*x.e1, a*x.e2, a*x.e3, a*x.e4, a*x.e12, a*x.e13, a*x.e14, a*x.e23, a*x.e24, a*x.e34, a*x.e123, a*x.e124, a*x.e134, a*x.e234, a*x.e1234);
}

CGA2 mul(int a, CGA2 x){
    return mul(float(a), x);
}

CGA2 mul(CGA2 u, CGA2 v){
    return CGA2(u.e1*v.e1 - u.e12*v.e12 + u.e123*v.e124 - u.e1234*v.e1234 + u.e124*v.e123 + u.e13*v.e14 + u.e134*v.e134 + u.e14*v.e13 + u.e2*v.e2 + u.e23*v.e24 + u.e234*v.e234 + u.e24*v.e23 - u.e3*v.e4 + u.e34*v.e34 - u.e4*v.e3 + u.scalar*v.scalar, u.e1*v.scalar + u.e12*v.e2 + u.e123*v.e24 + u.e1234*v.e234 + u.e124*v.e23 - u.e13*v.e4 + u.e134*v.e34 - u.e14*v.e3 - u.e2*v.e12 + u.e23*v.e124 - u.e234*v.e1234 + u.e24*v.e123 + u.e3*v.e14 + u.e34*v.e134 + u.e4*v.e13 + u.scalar*v.e1, u.e1*v.e12 - u.e12*v.e1 - u.e123*v.e14 - u.e1234*v.e134 - u.e124*v.e13 - u.e13*v.e124 + u.e134*v.e1234 - u.e14*v.e123 + u.e2*v.scalar - u.e23*v.e4 + u.e234*v.e34 - u.e24*v.e3 + u.e3*v.e24 + u.e34*v.e234 + u.e4*v.e23 + u.scalar*v.e2, u.e1*v.e13 - u.e12*v.e123 - u.e123*v.e12 - u.e123*v.e1234 + u.e1234*v.e123 - u.e13*v.e1 - u.e13*v.e134 - u.e134*v.e13 + u.e2*v.e23 - u.e23*v.e2 - u.e23*v.e234 - u.e234*v.e23 + u.e3*v.e34 + u.e3*v.scalar - u.e34*v.e3 + u.scalar*v.e3, u.e1*v.e14 - u.e12*v.e124 - u.e1234*v.e124 - u.e124*v.e12 + u.e124*v.e1234 + u.e134*v.e14 - u.e14*v.e1 + u.e14*v.e134 + u.e2*v.e24 + u.e234*v.e24 - u.e24*v.e2 + u.e24*v.e234 + u.e34*v.e4 - u.e4*v.e34 + u.e4*v.scalar + u.scalar*v.e4, u.e1*v.e2 + u.e12*v.scalar - u.e123*v.e4 + u.e1234*v.e34 - u.e124*v.e3 + u.e13*v.e24 + u.e134*v.e234 + u.e14*v.e23 - u.e2*v.e1 - u.e23*v.e14 - u.e234*v.e134 - u.e24*v.e13 - u.e3*v.e124 + u.e34*v.e1234 - u.e4*v.e123 + u.scalar*v.e12, u.e1*v.e3 + u.e12*v.e23 - u.e123*v.e2 - u.e123*v.e234 - u.e1234*v.e23 + u.e13*v.e34 + u.e13*v.scalar - u.e134*v.e3 - u.e2*v.e123 - u.e23*v.e12 - u.e23*v.e1234 + u.e234*v.e123 - u.e3*v.e1 - u.e3*v.e134 - u.e34*v.e13 + u.scalar*v.e13, u.e1*v.e4 + u.e12*v.e24 + u.e1234*v.e24 - u.e124*v.e2 + u.e124*v.e234 + u.e134*v.e4 - u.e14*v.e34 + u.e14*v.scalar - u.e2*v.e124 - u.e234*v.e124 - u.e24*v.e12 + u.e24*v.e1234 + u.e34*v.e14 - u.e4*v.e1 + u.e4*v.e134 + u.scalar*v.e14, u.e1*v.e123 - u.e12*v.e13 + u.e123*v.e1 + u.e123*v.e134 + u.e1234*v.e13 + u.e13*v.e12 + u.e13*v.e1234 - u.e134*v.e123 + u.e2*v.e3 + u.e23*v.e34 + u.e23*v.scalar - u.e234*v.e3 - u.e3*v.e2 - u.e3*v.e234 - u.e34*v.e23 + u.scalar*v.e23, u.e1*v.e124 - u.e12*v.e14 - u.e1234*v.e14 + u.e124*v.e1 - u.e124*v.e134 + u.e134*v.e124 + u.e14*v.e12 - u.e14*v.e1234 + u.e2*v.e4 + u.e234*v.e4 - u.e24*v.e34 + u.e24*v.scalar + u.e34*v.e24 - u.e4*v.e2 + u.e4*v.e234 + u.scalar*v.e24, u.e1*v.e134 - u.e12*v.e1234 - u.e123*v.e124 - u.e1234*v.e12 + u.e124*v.e123 - u.e13*v.e14 + u.e134*v.e1 + u.e14*v.e13 + u.e2*v.e234 - u.e23*v.e24 + u.e234*v.e2 + u.e24*v.e23 + u.e3*v.e4 + u.e34*v.scalar - u.e4*v.e3 + u.scalar*v.e34, u.e1*v.e23 + u.e12*v.e3 + u.e123*v.e34 + u.e123*v.scalar - u.e1234*v.e3 - u.e13*v.e2 - u.e13*v.e234 - u.e134*v.e23 - u.e2*v.e13 + u.e23*v.e1 + u.e23*v.e134 + u.e234*v.e13 + u.e3*v.e12 + u.e3*v.e1234 - u.e34*v.e123 + u.scalar*v.e123, u.e1*v.e24 + u.e12*v.e4 + u.e1234*v.e4 - u.e124*v.e34 + u.e124*v.scalar + u.e134*v.e24 - u.e14*v.e2 + u.e14*v.e234 - u.e2*v.e14 - u.e234*v.e14 + u.e24*v.e1 - u.e24*v.e134 + u.e34*v.e124 + u.e4*v.e12 - u.e4*v.e1234 + u.scalar*v.e124, u.e1*v.e34 + u.e12*v.e234 - u.e123*v.e24 + u.e1234*v.e2 + u.e124*v.e23 + u.e13*v.e4 + u.e134*v.scalar - u.e14*v.e3 - u.e2*v.e1234 - u.e23*v.e124 - u.e234*v.e12 + u.e24*v.e123 - u.e3*v.e14 + u.e34*v.e1 + u.e4*v.e13 + u.scalar*v.e134, u.e1*v.e1234 - u.e12*v.e134 + u.e123*v.e14 - u.e1234*v.e1 - u.e124*v.e13 + u.e13*v.e124 + u.e134*v.e12 - u.e14*v.e123 + u.e2*v.e34 + u.e23*v.e4 + u.e234*v.scalar - u.e24*v.e3 - u.e3*v.e24 + u.e34*v.e2 + u.e4*v.e23 + u.scalar*v.e234, u.e1*v.e234 + u.e12*v.e34 + u.e123*v.e4 + u.e1234*v.scalar - u.e124*v.e3 - u.e13*v.e24 + u.e134*v.e2 + u.e14*v.e23 - u.e2*v.e134 + u.e23*v.e14 - u.e234*v.e1 - u.e24*v.e13 + u.e3*v.e124 + u.e34*v.e12 - u.e4*v.e123 + u.scalar*v.e1234);
}

CGA2 dual(){
    return CGA2(u.e1234, u.e234, -u.e134, u.e123, -u.e124, -u.e34, u.e23, -u.e24, -u.e13, u.e14, u.e12, -u.e3, u.e4, u.e2, -u.e1, -u.scalar);
}

CGA2 involve(CGA2 u){
    return CGA2(u.scalar, -u.e1, -u.e2, -u.e3, -u.e4, u.e12, u.e13, u.e14, u.e23, u.e24, u.e34, -u.e123, -u.e124, -u.e134, -u.e234, u.e1234);
}

CGA2 inner(CGA2 u, CGA2 v){
    return CGA2(u.e1*v.e1 - u.e12*v.e12 + u.e123*v.e124 - u.e1234*v.e1234 + u.e124*v.e123 + u.e13*v.e14 + u.e134*v.e134 + u.e14*v.e13 + u.e2*v.e2 + u.e23*v.e24 + u.e234*v.e234 + u.e24*v.e23 - u.e3*v.e4 + u.e34*v.e34 - u.e4*v.e3, u.e12*v.e2 + u.e123*v.e24 + u.e1234*v.e234 + u.e124*v.e23 - u.e13*v.e4 + u.e134*v.e34 - u.e14*v.e3 - u.e2*v.e12 + u.e23*v.e124 - u.e234*v.e1234 + u.e24*v.e123 + u.e3*v.e14 + u.e34*v.e134 + u.e4*v.e13, u.e1*v.e12 - u.e12*v.e1 - u.e123*v.e14 - u.e1234*v.e134 - u.e124*v.e13 - u.e13*v.e124 + u.e134*v.e1234 - u.e14*v.e123 - u.e23*v.e4 + u.e234*v.e34 - u.e24*v.e3 + u.e3*v.e24 + u.e34*v.e234 + u.e4*v.e23, u.e1*v.e13 - u.e12*v.e123 - u.e123*v.e12 - u.e123*v.e1234 + u.e1234*v.e123 - u.e13*v.e1 - u.e13*v.e134 - u.e134*v.e13 + u.e2*v.e23 - u.e23*v.e2 - u.e23*v.e234 - u.e234*v.e23 + u.e3*v.e34 - u.e34*v.e3, u.e1*v.e14 - u.e12*v.e124 - u.e1234*v.e124 - u.e124*v.e12 + u.e124*v.e1234 + u.e134*v.e14 - u.e14*v.e1 + u.e14*v.e134 + u.e2*v.e24 + u.e234*v.e24 - u.e24*v.e2 + u.e24*v.e234 + u.e34*v.e4 - u.e4*v.e34, -u.e123*v.e4 + u.e1234*v.e34 - u.e124*v.e3 - u.e3*v.e124 + u.e34*v.e1234 - u.e4*v.e123, -u.e123*v.e2 - u.e1234*v.e23 - u.e134*v.e3 - u.e2*v.e123 - u.e23*v.e1234 - u.e3*v.e134, u.e1234*v.e24 - u.e124*v.e2 + u.e134*v.e4 - u.e2*v.e124 + u.e24*v.e1234 + u.e4*v.e134, u.e1*v.e123 + u.e123*v.e1 + u.e1234*v.e13 + u.e13*v.e1234 - u.e234*v.e3 - u.e3*v.e234, u.e1*v.e124 - u.e1234*v.e14 + u.e124*v.e1 - u.e14*v.e1234 + u.e234*v.e4 + u.e4*v.e234, u.e1*v.e134 - u.e12*v.e1234 - u.e1234*v.e12 + u.e134*v.e1 + u.e2*v.e234 + u.e234*v.e2, -u.e1234*v.e3 + u.e3*v.e1234, u.e1234*v.e4 - u.e4*v.e1234, u.e1234*v.e2 - u.e2*v.e1234, u.e1*v.e1234 - u.e1234*v.e1, 0.0);
}

CGA2 lcontract(CGA2 u, CGA2 v){
    return CGA2(u.e1*v.e1 - u.e12*v.e12 + u.e123*v.e124 - u.e1234*v.e1234 + u.e124*v.e123 + u.e13*v.e14 + u.e134*v.e134 + u.e14*v.e13 + u.e2*v.e2 + u.e23*v.e24 + u.e234*v.e234 + u.e24*v.e23 - u.e3*v.e4 + u.e34*v.e34 - u.e4*v.e3 + u.scalar*v.scalar, -u.e2*v.e12 + u.e23*v.e124 - u.e234*v.e1234 + u.e24*v.e123 + u.e3*v.e14 + u.e34*v.e134 + u.e4*v.e13 + u.scalar*v.e1, u.e1*v.e12 - u.e13*v.e124 + u.e134*v.e1234 - u.e14*v.e123 + u.e3*v.e24 + u.e34*v.e234 + u.e4*v.e23 + u.scalar*v.e2, u.e1*v.e13 - u.e12*v.e123 - u.e123*v.e1234 - u.e13*v.e134 + u.e2*v.e23 - u.e23*v.e234 + u.e3*v.e34 + u.scalar*v.e3, u.e1*v.e14 - u.e12*v.e124 + u.e124*v.e1234 + u.e14*v.e134 + u.e2*v.e24 + u.e24*v.e234 - u.e4*v.e34 + u.scalar*v.e4, -u.e3*v.e124 + u.e34*v.e1234 - u.e4*v.e123 + u.scalar*v.e12, -u.e2*v.e123 - u.e23*v.e1234 - u.e3*v.e134 + u.scalar*v.e13, -u.e2*v.e124 + u.e24*v.e1234 + u.e4*v.e134 + u.scalar*v.e14, u.e1*v.e123 + u.e13*v.e1234 - u.e3*v.e234 + u.scalar*v.e23, u.e1*v.e124 - u.e14*v.e1234 + u.e4*v.e234 + u.scalar*v.e24, u.e1*v.e134 - u.e12*v.e1234 + u.e2*v.e234 + u.scalar*v.e34, u.e3*v.e1234 + u.scalar*v.e123, -u.e4*v.e1234 + u.scalar*v.e124, -u.e2*v.e1234 + u.scalar*v.e134, u.e1*v.e1234 + u.scalar*v.e234, u.scalar*v.e1234);
}

CGA2 outer(CGA2 u, CGA2 v){
    return CGA2(u.scalar*v.scalar, u.e1*v.scalar + u.scalar*v.e1, u.e2*v.scalar + u.scalar*v.e2, u.e3*v.scalar + u.scalar*v.e3, u.e4*v.scalar + u.scalar*v.e4, u.e1*v.e2 + u.e12*v.scalar - u.e2*v.e1 + u.scalar*v.e12, u.e1*v.e3 + u.e13*v.scalar - u.e3*v.e1 + u.scalar*v.e13, u.e1*v.e4 + u.e14*v.scalar - u.e4*v.e1 + u.scalar*v.e14, u.e2*v.e3 + u.e23*v.scalar - u.e3*v.e2 + u.scalar*v.e23, u.e2*v.e4 + u.e24*v.scalar - u.e4*v.e2 + u.scalar*v.e24, u.e3*v.e4 + u.e34*v.scalar - u.e4*v.e3 + u.scalar*v.e34, u.e1*v.e23 + u.e12*v.e3 + u.e123*v.scalar - u.e13*v.e2 - u.e2*v.e13 + u.e23*v.e1 + u.e3*v.e12 + u.scalar*v.e123, u.e1*v.e24 + u.e12*v.e4 + u.e124*v.scalar - u.e14*v.e2 - u.e2*v.e14 + u.e24*v.e1 + u.e4*v.e12 + u.scalar*v.e124, u.e1*v.e34 + u.e13*v.e4 + u.e134*v.scalar - u.e14*v.e3 - u.e3*v.e14 + u.e34*v.e1 + u.e4*v.e13 + u.scalar*v.e134, u.e2*v.e34 + u.e23*v.e4 + u.e234*v.scalar - u.e24*v.e3 - u.e3*v.e24 + u.e34*v.e2 + u.e4*v.e23 + u.scalar*v.e234, u.e1*v.e234 + u.e12*v.e34 + u.e123*v.e4 + u.e1234*v.scalar - u.e124*v.e3 - u.e13*v.e24 + u.e134*v.e2 + u.e14*v.e23 - u.e2*v.e134 + u.e23*v.e14 - u.e234*v.e1 - u.e24*v.e13 + u.e3*v.e124 + u.e34*v.e12 - u.e4*v.e123 + u.scalar*v.e1234);
}

CGA2 I(){
    return CGA2(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0);
}

CGA2 rcontract(CGA2 u, CGA2 v){
    return CGA2(u.e1*v.e1 - u.e12*v.e12 + u.e123*v.e124 - u.e1234*v.e1234 + u.e124*v.e123 + u.e13*v.e14 + u.e134*v.e134 + u.e14*v.e13 + u.e2*v.e2 + u.e23*v.e24 + u.e234*v.e234 + u.e24*v.e23 - u.e3*v.e4 + u.e34*v.e34 - u.e4*v.e3 + u.scalar*v.scalar, u.e1*v.scalar + u.e12*v.e2 + u.e123*v.e24 + u.e1234*v.e234 + u.e124*v.e23 - u.e13*v.e4 + u.e134*v.e34 - u.e14*v.e3, -u.e12*v.e1 - u.e123*v.e14 - u.e1234*v.e134 - u.e124*v.e13 + u.e2*v.scalar - u.e23*v.e4 + u.e234*v.e34 - u.e24*v.e3, -u.e123*v.e12 + u.e1234*v.e123 - u.e13*v.e1 - u.e134*v.e13 - u.e23*v.e2 - u.e234*v.e23 + u.e3*v.scalar - u.e34*v.e3, -u.e1234*v.e124 - u.e124*v.e12 + u.e134*v.e14 - u.e14*v.e1 + u.e234*v.e24 - u.e24*v.e2 + u.e34*v.e4 + u.e4*v.scalar, u.e12*v.scalar - u.e123*v.e4 + u.e1234*v.e34 - u.e124*v.e3, -u.e123*v.e2 - u.e1234*v.e23 + u.e13*v.scalar - u.e134*v.e3, u.e1234*v.e24 - u.e124*v.e2 + u.e134*v.e4 + u.e14*v.scalar, u.e123*v.e1 + u.e1234*v.e13 + u.e23*v.scalar - u.e234*v.e3, -u.e1234*v.e14 + u.e124*v.e1 + u.e234*v.e4 + u.e24*v.scalar, -u.e1234*v.e12 + u.e134*v.e1 + u.e234*v.e2 + u.e34*v.scalar, u.e123*v.scalar - u.e1234*v.e3, u.e1234*v.e4 + u.e124*v.scalar, u.e1234*v.e2 + u.e134*v.scalar, -u.e1234*v.e1 + u.e234*v.scalar, u.e1234*v.scalar);
}

CGA2 reverse(CGA2 u){
    return CGA2(u.scalar, u.e1, u.e2, u.e3, u.e4, -u.e12, -u.e13, -u.e14, -u.e23, -u.e24, -u.e34, -u.e123, -u.e124, -u.e134, -u.e234, u.e1234);
}

CGA2 conjugate(CGA2 u){
    return reverse(involve(u));
}
'''

snapshots['TestCliffordAlgebra::test_big_clifford_algebra_product 1'] = '''ComplexCl4 mul(ComplexCl4 u, ComplexCl4 v){
    return ComplexCl4(u.ONE*v.ONE + u.e1*v.e1 - u.e12*v.e12 - u.e123*v.e123 + u.e1234*v.e1234 - u.e124*v.e124 - u.e13*v.e13 - u.e134*v.e134 - u.e14*v.e14 + u.e2*v.e2 - u.e23*v.e23 - u.e234*v.e234 - u.e24*v.e24 + u.e3*v.e3 - u.e34*v.e34 + u.e4*v.e4, u.ONE*v.e1 + u.e1*v.ONE + u.e12*v.e2 - u.e123*v.e23 - u.e1234*v.e234 - u.e124*v.e24 + u.e13*v.e3 - u.e134*v.e34 + u.e14*v.e4 - u.e2*v.e12 - u.e23*v.e123 + u.e234*v.e1234 - u.e24*v.e124 - u.e3*v.e13 - u.e34*v.e134 - u.e4*v.e14, u.ONE*v.e2 + u.e1*v.e12 - u.e12*v.e1 + u.e123*v.e13 + u.e1234*v.e134 + u.e124*v.e14 + u.e13*v.e123 - u.e134*v.e1234 + u.e14*v.e124 + u.e2*v.ONE + u.e23*v.e3 - u.e234*v.e34 + u.e24*v.e4 - u.e3*v.e23 - u.e34*v.e234 - u.e4*v.e24, u.ONE*v.e3 + u.e1*v.e13 - u.e12*v.e123 - u.e123*v.e12 - u.e1234*v.e124 + u.e124*v.e1234 - u.e13*v.e1 + u.e134*v.e14 + u.e14*v.e134 + u.e2*v.e23 - u.e23*v.e2 + u.e234*v.e24 + u.e24*v.e234 + u.e3*v.ONE + u.e34*v.e4 - u.e4*v.e34, u.ONE*v.e4 + u.e1*v.e14 - u.e12*v.e124 - u.e123*v.e1234 + u.e1234*v.e123 - u.e124*v.e12 - u.e13*v.e134 - u.e134*v.e13 - u.e14*v.e1 + u.e2*v.e24 - u.e23*v.e234 - u.e234*v.e23 - u.e24*v.e2 + u.e3*v.e34 - u.e34*v.e3 + u.e4*v.ONE, u.ONE*v.e12 + u.e1*v.e2 + u.e12*v.ONE + u.e123*v.e3 - u.e1234*v.e34 + u.e124*v.e4 - u.e13*v.e23 - u.e134*v.e234 - u.e14*v.e24 - u.e2*v.e1 + u.e23*v.e13 + u.e234*v.e134 + u.e24*v.e14 + u.e3*v.e123 - u.e34*v.e1234 + u.e4*v.e124, u.ONE*v.e13 + u.e1*v.e3 + u.e12*v.e23 - u.e123*v.e2 + u.e1234*v.e24 + u.e124*v.e234 + u.e13*v.ONE + u.e134*v.e4 - u.e14*v.e34 - u.e2*v.e123 - u.e23*v.e12 - u.e234*v.e124 + u.e24*v.e1234 - u.e3*v.e1 + u.e34*v.e14 + u.e4*v.e134, u.ONE*v.e14 + u.e1*v.e4 + u.e12*v.e24 - u.e123*v.e234 - u.e1234*v.e23 - u.e124*v.e2 + u.e13*v.e34 - u.e134*v.e3 + u.e14*v.ONE - u.e2*v.e124 - u.e23*v.e1234 + u.e234*v.e123 - u.e24*v.e12 - u.e3*v.e134 - u.e34*v.e13 - u.e4*v.e1, u.ONE*v.e23 + u.e1*v.e123 - u.e12*v.e13 + u.e123*v.e1 - u.e1234*v.e14 - u.e124*v.e134 + u.e13*v.e12 + u.e134*v.e124 - u.e14*v.e1234 + u.e2*v.e3 + u.e23*v.ONE + u.e234*v.e4 - u.e24*v.e34 - u.e3*v.e2 + u.e34*v.e24 + u.e4*v.e234, u.ONE*v.e24 + u.e1*v.e124 - u.e12*v.e14 + u.e123*v.e134 + u.e1234*v.e13 + u.e124*v.e1 + u.e13*v.e1234 - u.e134*v.e123 + u.e14*v.e12 + u.e2*v.e4 + u.e23*v.e34 - u.e234*v.e3 + u.e24*v.ONE - u.e3*v.e234 - u.e34*v.e23 - u.e4*v.e2, u.ONE*v.e34 + u.e1*v.e134 - u.e12*v.e1234 - u.e123*v.e124 - u.e1234*v.e12 + u.e124*v.e123 - u.e13*v.e14 + u.e134*v.e1 + u.e14*v.e13 + u.e2*v.e234 - u.e23*v.e24 + u.e234*v.e2 + u.e24*v.e23 + u.e3*v.e4 + u.e34*v.ONE - u.e4*v.e3, u.ONE*v.e123 + u.e1*v.e23 + u.e12*v.e3 + u.e123*v.ONE + u.e1234*v.e4 - u.e124*v.e34 - u.e13*v.e2 + u.e134*v.e24 + u.e14*v.e234 - u.e2*v.e13 + u.e23*v.e1 - u.e234*v.e14 - u.e24*v.e134 + u.e3*v.e12 + u.e34*v.e124 - u.e4*v.e1234, u.ONE*v.e124 + u.e1*v.e24 + u.e12*v.e4 + u.e123*v.e34 - u.e1234*v.e3 + u.e124*v.ONE - u.e13*v.e234 - u.e134*v.e23 - u.e14*v.e2 - u.e2*v.e14 + u.e23*v.e134 + u.e234*v.e13 + u.e24*v.e1 + u.e3*v.e1234 - u.e34*v.e123 + u.e4*v.e12, u.ONE*v.e134 + u.e1*v.e34 + u.e12*v.e234 - u.e123*v.e24 + u.e1234*v.e2 + u.e124*v.e23 + u.e13*v.e4 + u.e134*v.ONE - u.e14*v.e3 - u.e2*v.e1234 - u.e23*v.e124 - u.e234*v.e12 + u.e24*v.e123 - u.e3*v.e14 + u.e34*v.e1 + u.e4*v.e13, u.ONE*v.e234 + u.e1*v.e1234 - u.e12*v.e134 + u.e123*v.e14 - u.e1234*v.e1 - u.e124*v.e13 + u.e13*v.e124 + u.e134*v.e12 - u.e14*v.e123 + u.e2*v.e34 + u.e23*v.e4 + u.e234*v.ONE - u.e24*v.e3 - u.e3*v.e24 + u.e34*v.e2 + u.e4*v.e23, u.ONE*v.e1234 + u.e1*v.e234 + u.e12*v.e34 + u.e123*v.e4 + u.e1234*v.ONE - u.e124*v.e3 - u.e13*v.e24 + u.e134*v.e2 + u.e14*v.e23 - u.e2*v.e134 + u.e23*v.e14 - u.e234*v.e1 - u.e24*v.e13 + u.e3*v.e124 + u.e34*v.e12 - u.e4*v.e123);
}'''

snapshots['TestCliffordAlgebra::test_clifford_algebra_bundle 1'] = '''struct ComplexCl1_1 {
    C ONE; C e1; C e2; C e12;
}

ComplexCl1_1 fromArray(C x[4]){
    return ComplexCl1_1(x[0], x[1], x[2], x[3]);
}

C[4] toArray(ComplexCl1_1 x){
    return C[4](x.ONE, x.e1, x.e2, x.e12);
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

ComplexCl1_1 mul(int a, ComplexCl1_1 x){
    return mul(float(a), x);
}

ComplexCl1_1 mul(ComplexCl1_1 u, ComplexCl1_1 v){
    return ComplexCl1_1(sub(add(add(mul(u.ONE, v.ONE), mul(u.e12, v.e12)), mul(u.e2, v.e2)), mul(u.e1, v.e1)), sub(add(add(mul(u.ONE, v.e1), mul(u.e1, v.ONE)), mul(u.e12, v.e2)), mul(u.e2, v.e12)), sub(add(add(mul(u.ONE, v.e2), mul(u.e12, v.e1)), mul(u.e2, v.ONE)), mul(u.e1, v.e12)), sub(add(add(mul(u.ONE, v.e12), mul(u.e1, v.e2)), mul(u.e12, v.ONE)), mul(u.e2, v.e1)));
}

ComplexCl1_1 dual(){
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
