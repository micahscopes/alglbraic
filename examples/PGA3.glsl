const int Idx_PGA3_scalar = 0;
const int Idx_PGA3_e1 = 1;
const int Idx_PGA3_e2 = 2;
const int Idx_PGA3_e3 = 3;
const int Idx_PGA3_e4 = 4;
const int Idx_PGA3_e12 = 5;
const int Idx_PGA3_e13 = 6;
const int Idx_PGA3_e14 = 7;
const int Idx_PGA3_e23 = 8;
const int Idx_PGA3_e24 = 9;
const int Idx_PGA3_e34 = 10;
const int Idx_PGA3_e123 = 11;
const int Idx_PGA3_e124 = 12;
const int Idx_PGA3_e134 = 13;
const int Idx_PGA3_e234 = 14;
const int Idx_PGA3_e1234 = 15;

struct PGA3 {
    float scalar;
    float e1;
    float e2;
    float e3;
    float e4;
    float e12;
    float e13;
    float e14;
    float e23;
    float e24;
    float e34;
    float e123;
    float e124;
    float e134;
    float e234;
    float e1234;
};

PGA3 fromArray(float X[16]){
    return PGA3(X[0], X[1], X[2], X[3], X[4], X[5], X[6], X[7], X[8], X[9], X[10], X[11], X[12], X[13], X[14], X[15]);
}

void toArray(PGA3 X, inout float X_ary[16]){
    X_ary[0] = X.scalar;
    X_ary[1] = X.e1;
    X_ary[2] = X.e2;
    X_ary[3] = X.e3;
    X_ary[4] = X.e4;
    X_ary[5] = X.e12;
    X_ary[6] = X.e13;
    X_ary[7] = X.e14;
    X_ary[8] = X.e23;
    X_ary[9] = X.e24;
    X_ary[10] = X.e34;
    X_ary[11] = X.e123;
    X_ary[12] = X.e124;
    X_ary[13] = X.e134;
    X_ary[14] = X.e234;
    X_ary[15] = X.e1234;
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

PGA3 add(PGA3 X, PGA3 Y){
    return PGA3(X.scalar + Y.scalar, X.e1 + Y.e1, X.e2 + Y.e2, X.e3 + Y.e3, X.e4 + Y.e4, X.e12 + Y.e12, X.e13 + Y.e13, X.e14 + Y.e14, X.e23 + Y.e23, X.e24 + Y.e24, X.e34 + Y.e34, X.e123 + Y.e123, X.e124 + Y.e124, X.e134 + Y.e134, X.e234 + Y.e234, X.e1234 + Y.e1234);
}

PGA3 add(PGA3 X, PGA3 Y, PGA3 Z){
    return add(add(X, Y), Z);
}

PGA3 add(PGA3 X, PGA3 Y, PGA3 Z, PGA3 P){
    return add(add(add(X, Y), Z), P);
}

#define ONE_PGA3 PGA3(1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

PGA3 mul(float a, PGA3 X){
    return PGA3(X.scalar*a, X.e1*a, X.e2*a, X.e3*a, X.e4*a, X.e12*a, X.e13*a, X.e14*a, X.e23*a, X.e24*a, X.e34*a, X.e123*a, X.e124*a, X.e134*a, X.e234*a, X.e1234*a);
}

PGA3 sub(PGA3 X, PGA3 Y){
    return PGA3(X.scalar - Y.scalar, X.e1 - Y.e1, X.e2 - Y.e2, X.e3 - Y.e3, X.e4 - Y.e4, X.e12 - Y.e12, X.e13 - Y.e13, X.e14 - Y.e14, X.e23 - Y.e23, X.e24 - Y.e24, X.e34 - Y.e34, X.e123 - Y.e123, X.e124 - Y.e124, X.e134 - Y.e134, X.e234 - Y.e234, X.e1234 - Y.e1234);
}

#define ZERO_PGA3 PGA3(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)



PGA3 mul(int a, PGA3 X){
    return mul(float(a), X);
}

PGA3 mul(PGA3 X, PGA3 Y){
    return PGA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 - X.e13*Y.e13 + X.e2*Y.e2 - X.e23*Y.e23 + X.e3*Y.e3 + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2 - X.e123*Y.e23 + X.e13*Y.e3 - X.e2*Y.e12 - X.e23*Y.e123 - X.e3*Y.e13 + X.scalar*Y.e1, X.e1*Y.e12 - X.e12*Y.e1 + X.e123*Y.e13 + X.e13*Y.e123 + X.e2*Y.scalar + X.e23*Y.e3 - X.e3*Y.e23 + X.scalar*Y.e2, X.e1*Y.e13 - X.e12*Y.e123 - X.e123*Y.e12 - X.e13*Y.e1 + X.e2*Y.e23 - X.e23*Y.e2 + X.e3*Y.scalar + X.scalar*Y.e3, X.e1*Y.e14 - X.e12*Y.e124 - X.e123*Y.e1234 + X.e1234*Y.e123 - X.e124*Y.e12 - X.e13*Y.e134 - X.e134*Y.e13 - X.e14*Y.e1 + X.e2*Y.e24 - X.e23*Y.e234 - X.e234*Y.e23 - X.e24*Y.e2 + X.e3*Y.e34 - X.e34*Y.e3 + X.e4*Y.scalar + X.scalar*Y.e4, X.e1*Y.e2 + X.e12*Y.scalar + X.e123*Y.e3 - X.e13*Y.e23 - X.e2*Y.e1 + X.e23*Y.e13 + X.e3*Y.e123 + X.scalar*Y.e12, X.e1*Y.e3 + X.e12*Y.e23 - X.e123*Y.e2 + X.e13*Y.scalar - X.e2*Y.e123 - X.e23*Y.e12 - X.e3*Y.e1 + X.scalar*Y.e13, X.e1*Y.e4 + X.e12*Y.e24 - X.e123*Y.e234 - X.e1234*Y.e23 - X.e124*Y.e2 + X.e13*Y.e34 - X.e134*Y.e3 + X.e14*Y.scalar - X.e2*Y.e124 - X.e23*Y.e1234 + X.e234*Y.e123 - X.e24*Y.e12 - X.e3*Y.e134 - X.e34*Y.e13 - X.e4*Y.e1 + X.scalar*Y.e14, X.e1*Y.e123 - X.e12*Y.e13 + X.e123*Y.e1 + X.e13*Y.e12 + X.e2*Y.e3 + X.e23*Y.scalar - X.e3*Y.e2 + X.scalar*Y.e23, X.e1*Y.e124 - X.e12*Y.e14 + X.e123*Y.e134 + X.e1234*Y.e13 + X.e124*Y.e1 + X.e13*Y.e1234 - X.e134*Y.e123 + X.e14*Y.e12 + X.e2*Y.e4 + X.e23*Y.e34 - X.e234*Y.e3 + X.e24*Y.scalar - X.e3*Y.e234 - X.e34*Y.e23 - X.e4*Y.e2 + X.scalar*Y.e24, X.e1*Y.e134 - X.e12*Y.e1234 - X.e123*Y.e124 - X.e1234*Y.e12 + X.e124*Y.e123 - X.e13*Y.e14 + X.e134*Y.e1 + X.e14*Y.e13 + X.e2*Y.e234 - X.e23*Y.e24 + X.e234*Y.e2 + X.e24*Y.e23 + X.e3*Y.e4 + X.e34*Y.scalar - X.e4*Y.e3 + X.scalar*Y.e34, X.e1*Y.e23 + X.e12*Y.e3 + X.e123*Y.scalar - X.e13*Y.e2 - X.e2*Y.e13 + X.e23*Y.e1 + X.e3*Y.e12 + X.scalar*Y.e123, X.e1*Y.e24 + X.e12*Y.e4 + X.e123*Y.e34 - X.e1234*Y.e3 + X.e124*Y.scalar - X.e13*Y.e234 - X.e134*Y.e23 - X.e14*Y.e2 - X.e2*Y.e14 + X.e23*Y.e134 + X.e234*Y.e13 + X.e24*Y.e1 + X.e3*Y.e1234 - X.e34*Y.e123 + X.e4*Y.e12 + X.scalar*Y.e124, X.e1*Y.e34 + X.e12*Y.e234 - X.e123*Y.e24 + X.e1234*Y.e2 + X.e124*Y.e23 + X.e13*Y.e4 + X.e134*Y.scalar - X.e14*Y.e3 - X.e2*Y.e1234 - X.e23*Y.e124 - X.e234*Y.e12 + X.e24*Y.e123 - X.e3*Y.e14 + X.e34*Y.e1 + X.e4*Y.e13 + X.scalar*Y.e134, X.e1*Y.e1234 - X.e12*Y.e134 + X.e123*Y.e14 - X.e1234*Y.e1 - X.e124*Y.e13 + X.e13*Y.e124 + X.e134*Y.e12 - X.e14*Y.e123 + X.e2*Y.e34 + X.e23*Y.e4 + X.e234*Y.scalar - X.e24*Y.e3 - X.e3*Y.e24 + X.e34*Y.e2 + X.e4*Y.e23 + X.scalar*Y.e234, X.e1*Y.e234 + X.e12*Y.e34 + X.e123*Y.e4 + X.e1234*Y.scalar - X.e124*Y.e3 - X.e13*Y.e24 + X.e134*Y.e2 + X.e14*Y.e23 - X.e2*Y.e134 + X.e23*Y.e14 - X.e234*Y.e1 - X.e24*Y.e13 + X.e3*Y.e124 + X.e34*Y.e12 - X.e4*Y.e123 + X.scalar*Y.e1234);
}

PGA3 scalar_PGA3(float a){
    return mul(a, ONE_PGA3);
}

PGA3 mul(PGA3 X, PGA3 Y, PGA3 Z){
    return mul(mul(X, Y), Z);
}

PGA3 involve(PGA3 X){
    return PGA3(X.scalar, -X.e1, -X.e2, -X.e3, -X.e4, X.e12, X.e13, X.e14, X.e23, X.e24, X.e34, -X.e123, -X.e124, -X.e134, -X.e234, X.e1234);
}

PGA3 inner(PGA3 X, PGA3 Y){
    return PGA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 - X.e13*Y.e13 + X.e2*Y.e2 - X.e23*Y.e23 + X.e3*Y.e3, X.e12*Y.e2 - X.e123*Y.e23 + X.e13*Y.e3 - X.e2*Y.e12 - X.e23*Y.e123 - X.e3*Y.e13, X.e1*Y.e12 - X.e12*Y.e1 + X.e123*Y.e13 + X.e13*Y.e123 + X.e23*Y.e3 - X.e3*Y.e23, X.e1*Y.e13 - X.e12*Y.e123 - X.e123*Y.e12 - X.e13*Y.e1 + X.e2*Y.e23 - X.e23*Y.e2, X.e1*Y.e14 - X.e12*Y.e124 - X.e123*Y.e1234 + X.e1234*Y.e123 - X.e124*Y.e12 - X.e13*Y.e134 - X.e134*Y.e13 - X.e14*Y.e1 + X.e2*Y.e24 - X.e23*Y.e234 - X.e234*Y.e23 - X.e24*Y.e2 + X.e3*Y.e34 - X.e34*Y.e3, X.e123*Y.e3 + X.e3*Y.e123, -X.e123*Y.e2 - X.e2*Y.e123, -X.e1234*Y.e23 - X.e124*Y.e2 - X.e134*Y.e3 - X.e2*Y.e124 - X.e23*Y.e1234 - X.e3*Y.e134, X.e1*Y.e123 + X.e123*Y.e1, X.e1*Y.e124 + X.e1234*Y.e13 + X.e124*Y.e1 + X.e13*Y.e1234 - X.e234*Y.e3 - X.e3*Y.e234, X.e1*Y.e134 - X.e12*Y.e1234 - X.e1234*Y.e12 + X.e134*Y.e1 + X.e2*Y.e234 + X.e234*Y.e2, 0.0, -X.e1234*Y.e3 + X.e3*Y.e1234, X.e1234*Y.e2 - X.e2*Y.e1234, X.e1*Y.e1234 - X.e1234*Y.e1, 0.0);
}

PGA3 lcontract(PGA3 X, PGA3 Y){
    return PGA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 - X.e13*Y.e13 + X.e2*Y.e2 - X.e23*Y.e23 + X.e3*Y.e3 + X.scalar*Y.scalar, -X.e2*Y.e12 - X.e23*Y.e123 - X.e3*Y.e13 + X.scalar*Y.e1, X.e1*Y.e12 + X.e13*Y.e123 - X.e3*Y.e23 + X.scalar*Y.e2, X.e1*Y.e13 - X.e12*Y.e123 + X.e2*Y.e23 + X.scalar*Y.e3, X.e1*Y.e14 - X.e12*Y.e124 - X.e123*Y.e1234 - X.e13*Y.e134 + X.e2*Y.e24 - X.e23*Y.e234 + X.e3*Y.e34 + X.scalar*Y.e4, X.e3*Y.e123 + X.scalar*Y.e12, -X.e2*Y.e123 + X.scalar*Y.e13, -X.e2*Y.e124 - X.e23*Y.e1234 - X.e3*Y.e134 + X.scalar*Y.e14, X.e1*Y.e123 + X.scalar*Y.e23, X.e1*Y.e124 + X.e13*Y.e1234 - X.e3*Y.e234 + X.scalar*Y.e24, X.e1*Y.e134 - X.e12*Y.e1234 + X.e2*Y.e234 + X.scalar*Y.e34, X.scalar*Y.e123, X.e3*Y.e1234 + X.scalar*Y.e124, -X.e2*Y.e1234 + X.scalar*Y.e134, X.e1*Y.e1234 + X.scalar*Y.e234, X.scalar*Y.e1234);
}

PGA3 outer(PGA3 X, PGA3 Y){
    return PGA3(X.scalar*Y.scalar, X.e1*Y.scalar + X.scalar*Y.e1, X.e2*Y.scalar + X.scalar*Y.e2, X.e3*Y.scalar + X.scalar*Y.e3, X.e4*Y.scalar + X.scalar*Y.e4, X.e1*Y.e2 + X.e12*Y.scalar - X.e2*Y.e1 + X.scalar*Y.e12, X.e1*Y.e3 + X.e13*Y.scalar - X.e3*Y.e1 + X.scalar*Y.e13, X.e1*Y.e4 + X.e14*Y.scalar - X.e4*Y.e1 + X.scalar*Y.e14, X.e2*Y.e3 + X.e23*Y.scalar - X.e3*Y.e2 + X.scalar*Y.e23, X.e2*Y.e4 + X.e24*Y.scalar - X.e4*Y.e2 + X.scalar*Y.e24, X.e3*Y.e4 + X.e34*Y.scalar - X.e4*Y.e3 + X.scalar*Y.e34, X.e1*Y.e23 + X.e12*Y.e3 + X.e123*Y.scalar - X.e13*Y.e2 - X.e2*Y.e13 + X.e23*Y.e1 + X.e3*Y.e12 + X.scalar*Y.e123, X.e1*Y.e24 + X.e12*Y.e4 + X.e124*Y.scalar - X.e14*Y.e2 - X.e2*Y.e14 + X.e24*Y.e1 + X.e4*Y.e12 + X.scalar*Y.e124, X.e1*Y.e34 + X.e13*Y.e4 + X.e134*Y.scalar - X.e14*Y.e3 - X.e3*Y.e14 + X.e34*Y.e1 + X.e4*Y.e13 + X.scalar*Y.e134, X.e2*Y.e34 + X.e23*Y.e4 + X.e234*Y.scalar - X.e24*Y.e3 - X.e3*Y.e24 + X.e34*Y.e2 + X.e4*Y.e23 + X.scalar*Y.e234, X.e1*Y.e234 + X.e12*Y.e34 + X.e123*Y.e4 + X.e1234*Y.scalar - X.e124*Y.e3 - X.e13*Y.e24 + X.e134*Y.e2 + X.e14*Y.e23 - X.e2*Y.e134 + X.e23*Y.e14 - X.e234*Y.e1 - X.e24*Y.e13 + X.e3*Y.e124 + X.e34*Y.e12 - X.e4*Y.e123 + X.scalar*Y.e1234);
}

#define I_PGA3 PGA3(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)

PGA3 rcontract(PGA3 X, PGA3 Y){
    return PGA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 - X.e13*Y.e13 + X.e2*Y.e2 - X.e23*Y.e23 + X.e3*Y.e3 + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2 - X.e123*Y.e23 + X.e13*Y.e3, -X.e12*Y.e1 + X.e123*Y.e13 + X.e2*Y.scalar + X.e23*Y.e3, -X.e123*Y.e12 - X.e13*Y.e1 - X.e23*Y.e2 + X.e3*Y.scalar, X.e1234*Y.e123 - X.e124*Y.e12 - X.e134*Y.e13 - X.e14*Y.e1 - X.e234*Y.e23 - X.e24*Y.e2 - X.e34*Y.e3 + X.e4*Y.scalar, X.e12*Y.scalar + X.e123*Y.e3, -X.e123*Y.e2 + X.e13*Y.scalar, -X.e1234*Y.e23 - X.e124*Y.e2 - X.e134*Y.e3 + X.e14*Y.scalar, X.e123*Y.e1 + X.e23*Y.scalar, X.e1234*Y.e13 + X.e124*Y.e1 - X.e234*Y.e3 + X.e24*Y.scalar, -X.e1234*Y.e12 + X.e134*Y.e1 + X.e234*Y.e2 + X.e34*Y.scalar, X.e123*Y.scalar, -X.e1234*Y.e3 + X.e124*Y.scalar, X.e1234*Y.e2 + X.e134*Y.scalar, -X.e1234*Y.e1 + X.e234*Y.scalar, X.e1234*Y.scalar);
}

PGA3 reverse(PGA3 X){
    return PGA3(X.scalar, X.e1, X.e2, X.e3, X.e4, -X.e12, -X.e13, -X.e14, -X.e23, -X.e24, -X.e34, -X.e123, -X.e124, -X.e134, -X.e234, X.e1234);
}



PGA3 conjugate(PGA3 X){
    return reverse(involve(X));
}

PGA3 outer(PGA3 X, PGA3 Y, PGA3 Z){
    return outer(outer(X, Y), Z);
}

PGA3 invert(PGA3 X){
    return mul(1.0/lcontract(X,conjugate(X)).scalar, conjugate(X));
}

PGA3 div(PGA3 X, PGA3 Y){
    return mul(X, invert(Y));
}

PGA3 dual(PGA3 X){
    return div(X, I_PGA3);
}
