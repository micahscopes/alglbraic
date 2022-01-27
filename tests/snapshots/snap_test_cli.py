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

C fromArray(float X[2]){
    return C(X[0], X[1]);
}

void toArray(C X, inout float X_ary[2]){
    X_ary[0] = X.real;
    X_ary[1] = X.imag;
}

void zero(inout float X[2]){
    X[0] = 0.0;
    X[1] = 0.0;
}

C add(C X, C Y){
    return C(X.real + Y.real, X.imag + Y.imag);
}

C add(C X, C Y, C Z){
    return add(add(X, Y), Z);
}

C add(C X, C Y, C Z, C P){
    return add(add(add(X, Y), Z), P);
}

C one(){
    return C(1.0, 0.0);
}



C sub(C X, C Y){
    return C(X.real - Y.real, X.imag - Y.imag);
}

C zero(){
    return C(0.0, 0.0);
}

C mul(float a, C X){
    return C(X.real*a, X.imag*a);
}

C mul(C X, C Y){
    return C(-X.imag*Y.imag + X.real*Y.real, X.imag*Y.real + X.real*Y.imag);
}

C mul(int a, C X){
    return mul(float(a), X);
}

C mul(C X, C Y, C Z){
    return mul(mul(X, Y), Z);
}

C dual(C X){
    return C(X.imag, -X.real);
}

C involve(C X){
    return C(X.real, -X.imag);
}

C inner(C X, C Y){
    return C(-X.imag*Y.imag, 0.0);
}

C lcontract(C X, C Y){
    return C(-X.imag*Y.imag + X.real*Y.real, X.real*Y.imag);
}

C outer(C X, C Y){
    return C(X.real*Y.real, X.imag*Y.real + X.real*Y.imag);
}

C I(){
    return C(0.0, 1.0);
}

C rcontract(C X, C Y){
    return C(-X.imag*Y.imag + X.real*Y.real, X.imag*Y.real);
}

C reverse(C X){
    return C(X.real, X.imag);
}

C conjugate(C X){
    return reverse(involve(X));
}

C outer(C X, C Y, C Z){
    return outer(outer(X, Y), Z);
}

'''

snapshots['TestCLI::test_dual_numbers 1'] = '''const int I_Dual_real = 0;
const int I_Dual_nil = 1;

struct Dual {
    float real;
    float nil;
};

Dual fromArray(float X[2]){
    return Dual(X[0], X[1]);
}

void toArray(Dual X, inout float X_ary[2]){
    X_ary[0] = X.real;
    X_ary[1] = X.nil;
}

void zero(inout float X[2]){
    X[0] = 0.0;
    X[1] = 0.0;
}

Dual add(Dual X, Dual Y){
    return Dual(X.real + Y.real, X.nil + Y.nil);
}

Dual add(Dual X, Dual Y, Dual Z){
    return add(add(X, Y), Z);
}

Dual add(Dual X, Dual Y, Dual Z, Dual P){
    return add(add(add(X, Y), Z), P);
}

Dual one(){
    return Dual(1.0, 0.0);
}



Dual sub(Dual X, Dual Y){
    return Dual(X.real - Y.real, X.nil - Y.nil);
}

Dual zero(){
    return Dual(0.0, 0.0);
}

Dual mul(float a, Dual X){
    return Dual(X.real*a, X.nil*a);
}

Dual mul(Dual X, Dual Y){
    return Dual(X.real*Y.real, X.nil*Y.real + X.real*Y.nil);
}

Dual mul(int a, Dual X){
    return mul(float(a), X);
}

Dual mul(Dual X, Dual Y, Dual Z){
    return mul(mul(X, Y), Z);
}

Dual dual(Dual X){
    return Dual(0.0, 0.0);
}

Dual involve(Dual X){
    return Dual(X.real, -X.nil);
}

Dual inner(Dual X, Dual Y){
    return Dual(0.0, 0.0);
}

Dual lcontract(Dual X, Dual Y){
    return Dual(X.real*Y.real, X.real*Y.nil);
}

Dual outer(Dual X, Dual Y){
    return Dual(X.real*Y.real, X.nil*Y.real + X.real*Y.nil);
}

Dual rcontract(Dual X, Dual Y){
    return Dual(X.real*Y.real, X.nil*Y.real);
}

Dual reverse(Dual X){
    return Dual(X.real, X.nil);
}

Dual I(){
    return Dual(0.0, 1.0);
}

Dual conjugate(Dual X){
    return reverse(involve(X));
}

Dual outer(Dual X, Dual Y, Dual Z){
    return outer(outer(X, Y), Z);
}

'''
