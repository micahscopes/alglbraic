const int Idx_PGA2_scalar = 0;
const int Idx_PGA2_e1 = 1;
const int Idx_PGA2_e2 = 2;
const int Idx_PGA2_e3 = 3;
const int Idx_PGA2_e12 = 4;
const int Idx_PGA2_e13 = 5;
const int Idx_PGA2_e23 = 6;
const int Idx_PGA2_e123 = 7;

struct PGA2 {
    float scalar;
    float e1;
    float e2;
    float e3;
    float e12;
    float e13;
    float e23;
    float e123;
};

PGA2 fromArray(float X[8]){
    return PGA2(X[0], X[1], X[2], X[3], X[4], X[5], X[6], X[7]);
}

void toArray(PGA2 X, inout float X_ary[8]){
    X_ary[0] = X.scalar;
    X_ary[1] = X.e1;
    X_ary[2] = X.e2;
    X_ary[3] = X.e3;
    X_ary[4] = X.e12;
    X_ary[5] = X.e13;
    X_ary[6] = X.e23;
    X_ary[7] = X.e123;
}

void zero(inout float X[8]){
    X[0] = 0.0;
    X[1] = 0.0;
    X[2] = 0.0;
    X[3] = 0.0;
    X[4] = 0.0;
    X[5] = 0.0;
    X[6] = 0.0;
    X[7] = 0.0;
}

PGA2 add(PGA2 X, PGA2 Y){
    return PGA2(X.scalar + Y.scalar, X.e1 + Y.e1, X.e2 + Y.e2, X.e3 + Y.e3, X.e12 + Y.e12, X.e13 + Y.e13, X.e23 + Y.e23, X.e123 + Y.e123);
}

PGA2 add(PGA2 X, PGA2 Y, PGA2 Z){
    return add(add(X, Y), Z);
}

PGA2 add(PGA2 X, PGA2 Y, PGA2 Z, PGA2 P){
    return add(add(add(X, Y), Z), P);
}

#define ONE_PGA2 PGA2(1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

PGA2 mul(float a, PGA2 X){
    return PGA2(X.scalar*a, X.e1*a, X.e2*a, X.e3*a, X.e12*a, X.e13*a, X.e23*a, X.e123*a);
}

PGA2 sub(PGA2 X, PGA2 Y){
    return PGA2(X.scalar - Y.scalar, X.e1 - Y.e1, X.e2 - Y.e2, X.e3 - Y.e3, X.e12 - Y.e12, X.e13 - Y.e13, X.e23 - Y.e23, X.e123 - Y.e123);
}

#define ZERO_PGA2 PGA2(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)



PGA2 mul(int a, PGA2 X){
    return mul(float(a), X);
}

PGA2 mul(PGA2 X, PGA2 Y){
    return PGA2(X.e1*Y.e1 - X.e12*Y.e12 + X.e2*Y.e2 + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2 - X.e2*Y.e12 + X.scalar*Y.e1, X.e1*Y.e12 - X.e12*Y.e1 + X.e2*Y.scalar + X.scalar*Y.e2, X.e1*Y.e13 - X.e12*Y.e123 - X.e123*Y.e12 - X.e13*Y.e1 + X.e2*Y.e23 - X.e23*Y.e2 + X.e3*Y.scalar + X.scalar*Y.e3, X.e1*Y.e2 + X.e12*Y.scalar - X.e2*Y.e1 + X.scalar*Y.e12, X.e1*Y.e3 + X.e12*Y.e23 - X.e123*Y.e2 + X.e13*Y.scalar - X.e2*Y.e123 - X.e23*Y.e12 - X.e3*Y.e1 + X.scalar*Y.e13, X.e1*Y.e123 - X.e12*Y.e13 + X.e123*Y.e1 + X.e13*Y.e12 + X.e2*Y.e3 + X.e23*Y.scalar - X.e3*Y.e2 + X.scalar*Y.e23, X.e1*Y.e23 + X.e12*Y.e3 + X.e123*Y.scalar - X.e13*Y.e2 - X.e2*Y.e13 + X.e23*Y.e1 + X.e3*Y.e12 + X.scalar*Y.e123);
}

PGA2 scalar_PGA2(float a){
    return mul(a, ONE_PGA2);
}

PGA2 mul(PGA2 X, PGA2 Y, PGA2 Z){
    return mul(mul(X, Y), Z);
}

PGA2 involve(PGA2 X){
    return PGA2(X.scalar, -X.e1, -X.e2, -X.e3, X.e12, X.e13, X.e23, -X.e123);
}

PGA2 inner(PGA2 X, PGA2 Y){
    return PGA2(X.e1*Y.e1 - X.e12*Y.e12 + X.e2*Y.e2, X.e12*Y.e2 - X.e2*Y.e12, X.e1*Y.e12 - X.e12*Y.e1, X.e1*Y.e13 - X.e12*Y.e123 - X.e123*Y.e12 - X.e13*Y.e1 + X.e2*Y.e23 - X.e23*Y.e2, 0.0, -X.e123*Y.e2 - X.e2*Y.e123, X.e1*Y.e123 + X.e123*Y.e1, 0.0);
}

PGA2 lcontract(PGA2 X, PGA2 Y){
    return PGA2(X.e1*Y.e1 - X.e12*Y.e12 + X.e2*Y.e2 + X.scalar*Y.scalar, -X.e2*Y.e12 + X.scalar*Y.e1, X.e1*Y.e12 + X.scalar*Y.e2, X.e1*Y.e13 - X.e12*Y.e123 + X.e2*Y.e23 + X.scalar*Y.e3, X.scalar*Y.e12, -X.e2*Y.e123 + X.scalar*Y.e13, X.e1*Y.e123 + X.scalar*Y.e23, X.scalar*Y.e123);
}

PGA2 outer(PGA2 X, PGA2 Y){
    return PGA2(X.scalar*Y.scalar, X.e1*Y.scalar + X.scalar*Y.e1, X.e2*Y.scalar + X.scalar*Y.e2, X.e3*Y.scalar + X.scalar*Y.e3, X.e1*Y.e2 + X.e12*Y.scalar - X.e2*Y.e1 + X.scalar*Y.e12, X.e1*Y.e3 + X.e13*Y.scalar - X.e3*Y.e1 + X.scalar*Y.e13, X.e2*Y.e3 + X.e23*Y.scalar - X.e3*Y.e2 + X.scalar*Y.e23, X.e1*Y.e23 + X.e12*Y.e3 + X.e123*Y.scalar - X.e13*Y.e2 - X.e2*Y.e13 + X.e23*Y.e1 + X.e3*Y.e12 + X.scalar*Y.e123);
}

#define I_PGA2 PGA2(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)

PGA2 rcontract(PGA2 X, PGA2 Y){
    return PGA2(X.e1*Y.e1 - X.e12*Y.e12 + X.e2*Y.e2 + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2, -X.e12*Y.e1 + X.e2*Y.scalar, -X.e123*Y.e12 - X.e13*Y.e1 - X.e23*Y.e2 + X.e3*Y.scalar, X.e12*Y.scalar, -X.e123*Y.e2 + X.e13*Y.scalar, X.e123*Y.e1 + X.e23*Y.scalar, X.e123*Y.scalar);
}

PGA2 reverse(PGA2 X){
    return PGA2(X.scalar, X.e1, X.e2, X.e3, -X.e12, -X.e13, -X.e23, -X.e123);
}



PGA2 conjugate(PGA2 X){
    return reverse(involve(X));
}

PGA2 outer(PGA2 X, PGA2 Y, PGA2 Z){
    return outer(outer(X, Y), Z);
}

PGA2 invert(PGA2 X){
    return mul(1.0/lcontract(X,conjugate(X)).scalar, conjugate(X));
}

PGA2 div(PGA2 X, PGA2 Y){
    return mul(X, invert(Y));
}

PGA2 dual(PGA2 X){
    return div(X, I_PGA2);
}
