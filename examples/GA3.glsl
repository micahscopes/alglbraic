const int Idx_GA3_scalar = 0;
const int Idx_GA3_e1 = 1;
const int Idx_GA3_e2 = 2;
const int Idx_GA3_e3 = 3;
const int Idx_GA3_e12 = 4;
const int Idx_GA3_e13 = 5;
const int Idx_GA3_e23 = 6;
const int Idx_GA3_e123 = 7;

struct GA3 {
    float scalar;
    float e1;
    float e2;
    float e3;
    float e12;
    float e13;
    float e23;
    float e123;
};

GA3 fromArray(float X[8]){
    return GA3(X[0], X[1], X[2], X[3], X[4], X[5], X[6], X[7]);
}

void toArray(GA3 X, inout float X_ary[8]){
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

GA3 add(GA3 X, GA3 Y){
    return GA3(X.scalar + Y.scalar, X.e1 + Y.e1, X.e2 + Y.e2, X.e3 + Y.e3, X.e12 + Y.e12, X.e13 + Y.e13, X.e23 + Y.e23, X.e123 + Y.e123);
}

GA3 add(GA3 X, GA3 Y, GA3 Z){
    return add(add(X, Y), Z);
}

GA3 add(GA3 X, GA3 Y, GA3 Z, GA3 P){
    return add(add(add(X, Y), Z), P);
}

#define ONE_GA3 GA3(1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

GA3 mul(float a, GA3 X){
    return GA3(X.scalar*a, X.e1*a, X.e2*a, X.e3*a, X.e12*a, X.e13*a, X.e23*a, X.e123*a);
}

GA3 sub(GA3 X, GA3 Y){
    return GA3(X.scalar - Y.scalar, X.e1 - Y.e1, X.e2 - Y.e2, X.e3 - Y.e3, X.e12 - Y.e12, X.e13 - Y.e13, X.e23 - Y.e23, X.e123 - Y.e123);
}

#define ZERO_GA3 GA3(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)



GA3 mul(int a, GA3 X){
    return mul(float(a), X);
}

GA3 mul(GA3 X, GA3 Y){
    return GA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 - X.e13*Y.e13 + X.e2*Y.e2 - X.e23*Y.e23 + X.e3*Y.e3 + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2 - X.e123*Y.e23 + X.e13*Y.e3 - X.e2*Y.e12 - X.e23*Y.e123 - X.e3*Y.e13 + X.scalar*Y.e1, X.e1*Y.e12 - X.e12*Y.e1 + X.e123*Y.e13 + X.e13*Y.e123 + X.e2*Y.scalar + X.e23*Y.e3 - X.e3*Y.e23 + X.scalar*Y.e2, X.e1*Y.e13 - X.e12*Y.e123 - X.e123*Y.e12 - X.e13*Y.e1 + X.e2*Y.e23 - X.e23*Y.e2 + X.e3*Y.scalar + X.scalar*Y.e3, X.e1*Y.e2 + X.e12*Y.scalar + X.e123*Y.e3 - X.e13*Y.e23 - X.e2*Y.e1 + X.e23*Y.e13 + X.e3*Y.e123 + X.scalar*Y.e12, X.e1*Y.e3 + X.e12*Y.e23 - X.e123*Y.e2 + X.e13*Y.scalar - X.e2*Y.e123 - X.e23*Y.e12 - X.e3*Y.e1 + X.scalar*Y.e13, X.e1*Y.e123 - X.e12*Y.e13 + X.e123*Y.e1 + X.e13*Y.e12 + X.e2*Y.e3 + X.e23*Y.scalar - X.e3*Y.e2 + X.scalar*Y.e23, X.e1*Y.e23 + X.e12*Y.e3 + X.e123*Y.scalar - X.e13*Y.e2 - X.e2*Y.e13 + X.e23*Y.e1 + X.e3*Y.e12 + X.scalar*Y.e123);
}

GA3 scalar_GA3(float a){
    return mul(a, ONE_GA3);
}

GA3 mul(GA3 X, GA3 Y, GA3 Z){
    return mul(mul(X, Y), Z);
}

GA3 involve(GA3 X){
    return GA3(X.scalar, -X.e1, -X.e2, -X.e3, X.e12, X.e13, X.e23, -X.e123);
}

GA3 inner(GA3 X, GA3 Y){
    return GA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 - X.e13*Y.e13 + X.e2*Y.e2 - X.e23*Y.e23 + X.e3*Y.e3, X.e12*Y.e2 - X.e123*Y.e23 + X.e13*Y.e3 - X.e2*Y.e12 - X.e23*Y.e123 - X.e3*Y.e13, X.e1*Y.e12 - X.e12*Y.e1 + X.e123*Y.e13 + X.e13*Y.e123 + X.e23*Y.e3 - X.e3*Y.e23, X.e1*Y.e13 - X.e12*Y.e123 - X.e123*Y.e12 - X.e13*Y.e1 + X.e2*Y.e23 - X.e23*Y.e2, X.e123*Y.e3 + X.e3*Y.e123, -X.e123*Y.e2 - X.e2*Y.e123, X.e1*Y.e123 + X.e123*Y.e1, 0.0);
}

GA3 lcontract(GA3 X, GA3 Y){
    return GA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 - X.e13*Y.e13 + X.e2*Y.e2 - X.e23*Y.e23 + X.e3*Y.e3 + X.scalar*Y.scalar, -X.e2*Y.e12 - X.e23*Y.e123 - X.e3*Y.e13 + X.scalar*Y.e1, X.e1*Y.e12 + X.e13*Y.e123 - X.e3*Y.e23 + X.scalar*Y.e2, X.e1*Y.e13 - X.e12*Y.e123 + X.e2*Y.e23 + X.scalar*Y.e3, X.e3*Y.e123 + X.scalar*Y.e12, -X.e2*Y.e123 + X.scalar*Y.e13, X.e1*Y.e123 + X.scalar*Y.e23, X.scalar*Y.e123);
}

GA3 outer(GA3 X, GA3 Y){
    return GA3(X.scalar*Y.scalar, X.e1*Y.scalar + X.scalar*Y.e1, X.e2*Y.scalar + X.scalar*Y.e2, X.e3*Y.scalar + X.scalar*Y.e3, X.e1*Y.e2 + X.e12*Y.scalar - X.e2*Y.e1 + X.scalar*Y.e12, X.e1*Y.e3 + X.e13*Y.scalar - X.e3*Y.e1 + X.scalar*Y.e13, X.e2*Y.e3 + X.e23*Y.scalar - X.e3*Y.e2 + X.scalar*Y.e23, X.e1*Y.e23 + X.e12*Y.e3 + X.e123*Y.scalar - X.e13*Y.e2 - X.e2*Y.e13 + X.e23*Y.e1 + X.e3*Y.e12 + X.scalar*Y.e123);
}

#define I_GA3 GA3(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)

GA3 rcontract(GA3 X, GA3 Y){
    return GA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 - X.e13*Y.e13 + X.e2*Y.e2 - X.e23*Y.e23 + X.e3*Y.e3 + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2 - X.e123*Y.e23 + X.e13*Y.e3, -X.e12*Y.e1 + X.e123*Y.e13 + X.e2*Y.scalar + X.e23*Y.e3, -X.e123*Y.e12 - X.e13*Y.e1 - X.e23*Y.e2 + X.e3*Y.scalar, X.e12*Y.scalar + X.e123*Y.e3, -X.e123*Y.e2 + X.e13*Y.scalar, X.e123*Y.e1 + X.e23*Y.scalar, X.e123*Y.scalar);
}

GA3 reverse(GA3 X){
    return GA3(X.scalar, X.e1, X.e2, X.e3, -X.e12, -X.e13, -X.e23, -X.e123);
}



GA3 conjugate(GA3 X){
    return reverse(involve(X));
}

GA3 outer(GA3 X, GA3 Y, GA3 Z){
    return outer(outer(X, Y), Z);
}

GA3 invert(GA3 X){
    return mul(1.0/lcontract(X,conjugate(X)).scalar, conjugate(X));
}

GA3 div(GA3 X, GA3 Y){
    return mul(X, invert(Y));
}

GA3 dual(GA3 X){
    return div(X, I_GA3);
}
