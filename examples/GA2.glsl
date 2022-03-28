const int Idx_GA2_scalar = 0;
const int Idx_GA2_e1 = 1;
const int Idx_GA2_e2 = 2;
const int Idx_GA2_e12 = 3;

struct GA2 {
    float scalar;
    float e1;
    float e2;
    float e12;
};

GA2 fromArray(float X[4]){
    return GA2(X[0], X[1], X[2], X[3]);
}

void toArray(GA2 X, inout float X_ary[4]){
    X_ary[0] = X.scalar;
    X_ary[1] = X.e1;
    X_ary[2] = X.e2;
    X_ary[3] = X.e12;
}

void zero(inout float X[4]){
    X[0] = 0.0;
    X[1] = 0.0;
    X[2] = 0.0;
    X[3] = 0.0;
}

GA2 add(GA2 X, GA2 Y){
    return GA2(X.scalar + Y.scalar, X.e1 + Y.e1, X.e2 + Y.e2, X.e12 + Y.e12);
}

GA2 add(GA2 X, GA2 Y, GA2 Z){
    return add(add(X, Y), Z);
}

GA2 add(GA2 X, GA2 Y, GA2 Z, GA2 P){
    return add(add(add(X, Y), Z), P);
}

#define ONE_GA2 GA2(1.0, 0.0, 0.0, 0.0)

GA2 mul(float a, GA2 X){
    return GA2(X.scalar*a, X.e1*a, X.e2*a, X.e12*a);
}

GA2 sub(GA2 X, GA2 Y){
    return GA2(X.scalar - Y.scalar, X.e1 - Y.e1, X.e2 - Y.e2, X.e12 - Y.e12);
}

#define ZERO_GA2 GA2(0.0, 0.0, 0.0, 0.0)



GA2 mul(int a, GA2 X){
    return mul(float(a), X);
}

GA2 mul(GA2 X, GA2 Y){
    return GA2(X.e1*Y.e1 - X.e12*Y.e12 + X.e2*Y.e2 + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2 - X.e2*Y.e12 + X.scalar*Y.e1, X.e1*Y.e12 - X.e12*Y.e1 + X.e2*Y.scalar + X.scalar*Y.e2, X.e1*Y.e2 + X.e12*Y.scalar - X.e2*Y.e1 + X.scalar*Y.e12);
}

GA2 scalar_GA2(float a){
    return mul(a, ONE_GA2);
}

GA2 mul(GA2 X, GA2 Y, GA2 Z){
    return mul(mul(X, Y), Z);
}

GA2 involve(GA2 X){
    return GA2(X.scalar, -X.e1, -X.e2, X.e12);
}

GA2 inner(GA2 X, GA2 Y){
    return GA2(X.e1*Y.e1 - X.e12*Y.e12 + X.e2*Y.e2, X.e12*Y.e2 - X.e2*Y.e12, X.e1*Y.e12 - X.e12*Y.e1, 0.0);
}

GA2 lcontract(GA2 X, GA2 Y){
    return GA2(X.e1*Y.e1 - X.e12*Y.e12 + X.e2*Y.e2 + X.scalar*Y.scalar, -X.e2*Y.e12 + X.scalar*Y.e1, X.e1*Y.e12 + X.scalar*Y.e2, X.scalar*Y.e12);
}

GA2 outer(GA2 X, GA2 Y){
    return GA2(X.scalar*Y.scalar, X.e1*Y.scalar + X.scalar*Y.e1, X.e2*Y.scalar + X.scalar*Y.e2, X.e1*Y.e2 + X.e12*Y.scalar - X.e2*Y.e1 + X.scalar*Y.e12);
}

#define I_GA2 GA2(0.0, 0.0, 0.0, 1.0)

GA2 rcontract(GA2 X, GA2 Y){
    return GA2(X.e1*Y.e1 - X.e12*Y.e12 + X.e2*Y.e2 + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2, -X.e12*Y.e1 + X.e2*Y.scalar, X.e12*Y.scalar);
}

GA2 reverse(GA2 X){
    return GA2(X.scalar, X.e1, X.e2, -X.e12);
}



GA2 conjugate(GA2 X){
    return reverse(involve(X));
}

GA2 outer(GA2 X, GA2 Y, GA2 Z){
    return outer(outer(X, Y), Z);
}

GA2 invert(GA2 X){
    return mul(1.0/lcontract(X,conjugate(X)).scalar, conjugate(X));
}

GA2 div(GA2 X, GA2 Y){
    return mul(X, invert(Y));
}

GA2 dual(GA2 X){
    return div(X, I_GA2);
}
