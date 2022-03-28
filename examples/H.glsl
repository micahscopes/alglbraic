const int Idx_H_real = 0;
const int Idx_H_i = 1;
const int Idx_H_j = 2;
const int Idx_H_k = 3;

struct H {
    float real;
    float i;
    float j;
    float k;
};

H fromArray(float X[4]){
    return H(X[0], X[1], X[2], X[3]);
}

void toArray(H X, inout float X_ary[4]){
    X_ary[0] = X.real;
    X_ary[1] = X.i;
    X_ary[2] = X.j;
    X_ary[3] = X.k;
}

void zero(inout float X[4]){
    X[0] = 0.0;
    X[1] = 0.0;
    X[2] = 0.0;
    X[3] = 0.0;
}

H add(H X, H Y){
    return H(X.real + Y.real, X.i + Y.i, X.j + Y.j, X.k + Y.k);
}

H add(H X, H Y, H Z){
    return add(add(X, Y), Z);
}

H add(H X, H Y, H Z, H P){
    return add(add(add(X, Y), Z), P);
}

#define ONE_H H(1.0, 0.0, 0.0, 0.0)

H mul(float a, H X){
    return H(X.real*a, X.i*a, X.j*a, X.k*a);
}

H sub(H X, H Y){
    return H(X.real - Y.real, X.i - Y.i, X.j - Y.j, X.k - Y.k);
}

#define ZERO_H H(0.0, 0.0, 0.0, 0.0)



H mul(int a, H X){
    return mul(float(a), X);
}

H mul(H X, H Y){
    return H(-X.i*Y.i - X.j*Y.j - X.k*Y.k + X.real*Y.real, X.i*Y.real + X.j*Y.k - X.k*Y.j + X.real*Y.i, -X.i*Y.k + X.j*Y.real + X.k*Y.i + X.real*Y.j, X.i*Y.j - X.j*Y.i + X.k*Y.real + X.real*Y.k);
}

H scalar_H(float a){
    return mul(a, ONE_H);
}

H mul(H X, H Y, H Z){
    return mul(mul(X, Y), Z);
}

H involve(H X){
    return H(X.real, -X.i, -X.j, X.k);
}

H inner(H X, H Y){
    return H(-X.i*Y.i - X.j*Y.j - X.k*Y.k, X.j*Y.k - X.k*Y.j, -X.i*Y.k + X.k*Y.i, 0.0);
}

H lcontract(H X, H Y){
    return H(-X.i*Y.i - X.j*Y.j - X.k*Y.k + X.real*Y.real, X.j*Y.k + X.real*Y.i, -X.i*Y.k + X.real*Y.j, X.real*Y.k);
}

H outer(H X, H Y){
    return H(X.real*Y.real, X.i*Y.real + X.real*Y.i, X.j*Y.real + X.real*Y.j, X.i*Y.j - X.j*Y.i + X.k*Y.real + X.real*Y.k);
}

#define I_H H(0.0, 0.0, 0.0, 1.0)

H rcontract(H X, H Y){
    return H(-X.i*Y.i - X.j*Y.j - X.k*Y.k + X.real*Y.real, X.i*Y.real - X.k*Y.j, X.j*Y.real + X.k*Y.i, X.k*Y.real);
}

H reverse(H X){
    return H(X.real, X.i, X.j, -X.k);
}



H conjugate(H X){
    return reverse(involve(X));
}

H outer(H X, H Y, H Z){
    return outer(outer(X, Y), Z);
}

H invert(H X){
    return mul(1.0/lcontract(X,conjugate(X)).real, conjugate(X));
}

H div(H X, H Y){
    return mul(X, invert(Y));
}

H dual(H X){
    return div(X, I_H);
}
