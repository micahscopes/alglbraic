# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCLI::test_complex_numbers 1'] = '''struct C {
    float real; float imag;
}

C fromArray(float x[2]){
    return C(x[0], x[1]);
}

float[2] toArray(C x){
    return float[2](x.real, x.imag);
}

C add(C u, C v){
    return C(add(u.real, v.real), add(u.imag, v.imag));
}

C one(){
    return C(one(), zero());
}

C mul(float a, C x){
    return mul(mul(a, one()), x);
}

C sub(C u, C v){
    return C(sub(u.real, v.real), sub(u.imag, v.imag));
}

C zero(){
    return C(zero(), zero());
}

C mul(float a, C x){
    return C(mul(a, x.real), mul(a, x.imag));
}

C mul(int a, C x){
    return mul(float(a), x);
}

C product(C u, C v){
    return C(sub(mul(u.real, v.real), mul(u.imag, v.imag)), add(mul(u.imag, v.real), mul(u.real, v.imag)));
}

C involve(C u){
    return C(u.real, mul(-1, u.imag));
}

C reverse(C u){
    return C(u.real, u.imag);
}

C conjugate(C u){
    return reverse(involve(u));
}
'''

snapshots['TestCLI::test_dual_numbers 1'] = '''struct Dual {
    float real; float nilpotent;
}

Dual fromArray(float x[2]){
    return Dual(x[0], x[1]);
}

float[2] toArray(Dual x){
    return float[2](x.real, x.nilpotent);
}

Dual add(Dual u, Dual v){
    return Dual(add(u.real, v.real), add(u.nilpotent, v.nilpotent));
}

Dual one(){
    return Dual(one(), zero());
}

Dual mul(float a, Dual x){
    return mul(mul(a, one()), x);
}

Dual sub(Dual u, Dual v){
    return Dual(sub(u.real, v.real), sub(u.nilpotent, v.nilpotent));
}

Dual zero(){
    return Dual(zero(), zero());
}

Dual mul(float a, Dual x){
    return Dual(mul(a, x.real), mul(a, x.nilpotent));
}

Dual mul(int a, Dual x){
    return mul(float(a), x);
}

Dual product(Dual u, Dual v){
    return Dual(mul(u.real, v.real), add(mul(u.nilpotent, v.real), mul(u.real, v.nilpotent)));
}

Dual involve(Dual u){
    return Dual(u.real, mul(-1, u.nilpotent));
}

Dual reverse(Dual u){
    return Dual(u.real, u.nilpotent);
}

Dual conjugate(Dual u){
    return reverse(involve(u));
}
'''
