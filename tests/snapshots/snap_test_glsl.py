# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGlslBundler::test_compile_snippet_bundle 1'] = '''struct C {
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

C dual(){
    return C(u.imag, mul(-1, u.real));
}

C involve(C u){
    return C(u.real, mul(-1, u.imag));
}

C inner(C u, C v){
    return C(mul(mul(-1, u.imag), v.imag), 0.0);
}

C lcontract(C u, C v){
    return C(sub(mul(u.real, v.real), mul(u.imag, v.imag)), mul(u.real, v.imag));
}

C outer(C u, C v){
    return C(mul(u.real, v.real), add(mul(u.imag, v.real), mul(u.real, v.imag)));
}

C I(){
    return C(0.0, 1.0);
}

C rcontract(C u, C v){
    return C(sub(mul(u.real, v.real), mul(u.imag, v.imag)), mul(u.imag, v.real));
}

C reverse(C u){
    return C(u.real, u.imag);
}

C conjugate(C u){
    return reverse(involve(u));
}
'''
