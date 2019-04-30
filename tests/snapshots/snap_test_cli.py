# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCLI::test_complex_numbers 1'] = '''const int I_C_real = 0;
const int I_C_imag = 1;

struct C {
    float real;
    float imag;
};

C fromArray(float x[2]){
    return C(x[0], x[1]);
}

void toArray(C x, inout float x_ary[2]){
    x_ary[0] = x.real;
    x_ary[1] = x.imag;
}

void zero(inout float x[2]){
    x[0] = 0.0;
    x[1] = 0.0;
}

C add(C u, C v){
    return C(u.real + v.real, u.imag + v.imag);
}

C one(){
    return C(1.0, 0.0);
}



C sub(C u, C v){
    return C(u.real - v.real, u.imag - v.imag);
}

C zero(){
    return C(0.0, 0.0);
}

C mul(float a, C x){
    return C(a*x.real, a*x.imag);
}

C mul(C u, C v){
    return C(-u.imag*v.imag + u.real*v.real, u.imag*v.real + u.real*v.imag);
}

C mul(int a, C x){
    return mul(float(a), x);
}

C dual(C u){
    return C(u.imag, -u.real);
}

C involve(C u){
    return C(u.real, -u.imag);
}

C inner(C u, C v){
    return C(-u.imag*v.imag, 0.0);
}

C lcontract(C u, C v){
    return C(-u.imag*v.imag + u.real*v.real, u.real*v.imag);
}

C outer(C u, C v){
    return C(u.real*v.real, u.imag*v.real + u.real*v.imag);
}

C I(){
    return C(0.0, 1.0);
}

C rcontract(C u, C v){
    return C(-u.imag*v.imag + u.real*v.real, u.imag*v.real);
}

C reverse(C u){
    return C(u.real, u.imag);
}

C conjugate(C u){
    return reverse(involve(u));
}

'''

snapshots['TestCLI::test_dual_numbers 1'] = '''const int I_Dual_real = 0;
const int I_Dual_nilpotent = 1;

struct Dual {
    float real;
    float nilpotent;
};

Dual fromArray(float x[2]){
    return Dual(x[0], x[1]);
}

void toArray(Dual x, inout float x_ary[2]){
    x_ary[0] = x.real;
    x_ary[1] = x.nilpotent;
}

void zero(inout float x[2]){
    x[0] = 0.0;
    x[1] = 0.0;
}

Dual add(Dual u, Dual v){
    return Dual(u.real + v.real, u.nilpotent + v.nilpotent);
}

Dual one(){
    return Dual(1.0, 0.0);
}



Dual sub(Dual u, Dual v){
    return Dual(u.real - v.real, u.nilpotent - v.nilpotent);
}

Dual zero(){
    return Dual(0.0, 0.0);
}

Dual mul(float a, Dual x){
    return Dual(a*x.real, a*x.nilpotent);
}

Dual mul(Dual u, Dual v){
    return Dual(u.real*v.real, u.nilpotent*v.real + u.real*v.nilpotent);
}

Dual mul(int a, Dual x){
    return mul(float(a), x);
}

Dual dual(Dual u){
    return Dual(0.0, 0.0);
}

Dual involve(Dual u){
    return Dual(u.real, -u.nilpotent);
}

Dual inner(Dual u, Dual v){
    return Dual(0.0, 0.0);
}

Dual lcontract(Dual u, Dual v){
    return Dual(u.real*v.real, u.real*v.nilpotent);
}

Dual outer(Dual u, Dual v){
    return Dual(u.real*v.real, u.nilpotent*v.real + u.real*v.nilpotent);
}

Dual rcontract(Dual u, Dual v){
    return Dual(u.real*v.real, u.nilpotent*v.real);
}

Dual reverse(Dual u){
    return Dual(u.real, u.nilpotent);
}

Dual I(){
    return Dual(0.0, 1.0);
}

Dual conjugate(Dual u){
    return reverse(involve(u));
}

'''
