const int Idx_CGA3_scalar = 0;
const int Idx_CGA3_e1 = 1;
const int Idx_CGA3_e2 = 2;
const int Idx_CGA3_e3 = 3;
const int Idx_CGA3_e4 = 4;
const int Idx_CGA3_e5 = 5;
const int Idx_CGA3_e12 = 6;
const int Idx_CGA3_e13 = 7;
const int Idx_CGA3_e14 = 8;
const int Idx_CGA3_e15 = 9;
const int Idx_CGA3_e23 = 10;
const int Idx_CGA3_e24 = 11;
const int Idx_CGA3_e25 = 12;
const int Idx_CGA3_e34 = 13;
const int Idx_CGA3_e35 = 14;
const int Idx_CGA3_e45 = 15;
const int Idx_CGA3_e123 = 16;
const int Idx_CGA3_e124 = 17;
const int Idx_CGA3_e125 = 18;
const int Idx_CGA3_e134 = 19;
const int Idx_CGA3_e135 = 20;
const int Idx_CGA3_e145 = 21;
const int Idx_CGA3_e234 = 22;
const int Idx_CGA3_e235 = 23;
const int Idx_CGA3_e245 = 24;
const int Idx_CGA3_e345 = 25;
const int Idx_CGA3_e1234 = 26;
const int Idx_CGA3_e1235 = 27;
const int Idx_CGA3_e1245 = 28;
const int Idx_CGA3_e1345 = 29;
const int Idx_CGA3_e2345 = 30;
const int Idx_CGA3_e12345 = 31;

struct CGA3 {
    float scalar;
    float e1;
    float e2;
    float e3;
    float e4;
    float e5;
    float e12;
    float e13;
    float e14;
    float e15;
    float e23;
    float e24;
    float e25;
    float e34;
    float e35;
    float e45;
    float e123;
    float e124;
    float e125;
    float e134;
    float e135;
    float e145;
    float e234;
    float e235;
    float e245;
    float e345;
    float e1234;
    float e1235;
    float e1245;
    float e1345;
    float e2345;
    float e12345;
};

CGA3 fromArray(float X[32]){
    return CGA3(X[0], X[1], X[2], X[3], X[4], X[5], X[6], X[7], X[8], X[9], X[10], X[11], X[12], X[13], X[14], X[15], X[16], X[17], X[18], X[19], X[20], X[21], X[22], X[23], X[24], X[25], X[26], X[27], X[28], X[29], X[30], X[31]);
}

void toArray(CGA3 X, inout float X_ary[32]){
    X_ary[0] = X.scalar;
    X_ary[1] = X.e1;
    X_ary[2] = X.e2;
    X_ary[3] = X.e3;
    X_ary[4] = X.e4;
    X_ary[5] = X.e5;
    X_ary[6] = X.e12;
    X_ary[7] = X.e13;
    X_ary[8] = X.e14;
    X_ary[9] = X.e15;
    X_ary[10] = X.e23;
    X_ary[11] = X.e24;
    X_ary[12] = X.e25;
    X_ary[13] = X.e34;
    X_ary[14] = X.e35;
    X_ary[15] = X.e45;
    X_ary[16] = X.e123;
    X_ary[17] = X.e124;
    X_ary[18] = X.e125;
    X_ary[19] = X.e134;
    X_ary[20] = X.e135;
    X_ary[21] = X.e145;
    X_ary[22] = X.e234;
    X_ary[23] = X.e235;
    X_ary[24] = X.e245;
    X_ary[25] = X.e345;
    X_ary[26] = X.e1234;
    X_ary[27] = X.e1235;
    X_ary[28] = X.e1245;
    X_ary[29] = X.e1345;
    X_ary[30] = X.e2345;
    X_ary[31] = X.e12345;
}

void zero(inout float X[32]){
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
    X[16] = 0.0;
    X[17] = 0.0;
    X[18] = 0.0;
    X[19] = 0.0;
    X[20] = 0.0;
    X[21] = 0.0;
    X[22] = 0.0;
    X[23] = 0.0;
    X[24] = 0.0;
    X[25] = 0.0;
    X[26] = 0.0;
    X[27] = 0.0;
    X[28] = 0.0;
    X[29] = 0.0;
    X[30] = 0.0;
    X[31] = 0.0;
}

CGA3 add(CGA3 X, CGA3 Y){
    return CGA3(X.scalar + Y.scalar, X.e1 + Y.e1, X.e2 + Y.e2, X.e3 + Y.e3, X.e4 + Y.e4, X.e5 + Y.e5, X.e12 + Y.e12, X.e13 + Y.e13, X.e14 + Y.e14, X.e15 + Y.e15, X.e23 + Y.e23, X.e24 + Y.e24, X.e25 + Y.e25, X.e34 + Y.e34, X.e35 + Y.e35, X.e45 + Y.e45, X.e123 + Y.e123, X.e124 + Y.e124, X.e125 + Y.e125, X.e134 + Y.e134, X.e135 + Y.e135, X.e145 + Y.e145, X.e234 + Y.e234, X.e235 + Y.e235, X.e245 + Y.e245, X.e345 + Y.e345, X.e1234 + Y.e1234, X.e1235 + Y.e1235, X.e1245 + Y.e1245, X.e1345 + Y.e1345, X.e2345 + Y.e2345, X.e12345 + Y.e12345);
}

CGA3 add(CGA3 X, CGA3 Y, CGA3 Z){
    return add(add(X, Y), Z);
}

CGA3 add(CGA3 X, CGA3 Y, CGA3 Z, CGA3 P){
    return add(add(add(X, Y), Z), P);
}

#define ONE_CGA3 CGA3(1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

CGA3 mul(float a, CGA3 X){
    return CGA3(X.scalar*a, X.e1*a, X.e2*a, X.e3*a, X.e4*a, X.e5*a, X.e12*a, X.e13*a, X.e14*a, X.e15*a, X.e23*a, X.e24*a, X.e25*a, X.e34*a, X.e35*a, X.e45*a, X.e123*a, X.e124*a, X.e125*a, X.e134*a, X.e135*a, X.e145*a, X.e234*a, X.e235*a, X.e245*a, X.e345*a, X.e1234*a, X.e1235*a, X.e1245*a, X.e1345*a, X.e2345*a, X.e12345*a);
}

CGA3 sub(CGA3 X, CGA3 Y){
    return CGA3(X.scalar - Y.scalar, X.e1 - Y.e1, X.e2 - Y.e2, X.e3 - Y.e3, X.e4 - Y.e4, X.e5 - Y.e5, X.e12 - Y.e12, X.e13 - Y.e13, X.e14 - Y.e14, X.e15 - Y.e15, X.e23 - Y.e23, X.e24 - Y.e24, X.e25 - Y.e25, X.e34 - Y.e34, X.e35 - Y.e35, X.e45 - Y.e45, X.e123 - Y.e123, X.e124 - Y.e124, X.e125 - Y.e125, X.e134 - Y.e134, X.e135 - Y.e135, X.e145 - Y.e145, X.e234 - Y.e234, X.e235 - Y.e235, X.e245 - Y.e245, X.e345 - Y.e345, X.e1234 - Y.e1234, X.e1235 - Y.e1235, X.e1245 - Y.e1245, X.e1345 - Y.e1345, X.e2345 - Y.e2345, X.e12345 - Y.e12345);
}

#define ZERO_CGA3 CGA3(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)



CGA3 mul(int a, CGA3 X){
    return mul(float(a), X);
}

CGA3 mul(CGA3 X, CGA3 Y){
    return CGA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 + X.e1234*Y.e1234 - X.e12345*Y.e12345 - X.e1235*Y.e1235 - X.e124*Y.e124 - X.e1245*Y.e1245 + X.e125*Y.e125 - X.e13*Y.e13 - X.e134*Y.e134 - X.e1345*Y.e1345 + X.e135*Y.e135 - X.e14*Y.e14 + X.e145*Y.e145 + X.e15*Y.e15 + X.e2*Y.e2 - X.e23*Y.e23 - X.e234*Y.e234 - X.e2345*Y.e2345 + X.e235*Y.e235 - X.e24*Y.e24 + X.e245*Y.e245 + X.e25*Y.e25 + X.e3*Y.e3 - X.e34*Y.e34 + X.e345*Y.e345 + X.e35*Y.e35 + X.e4*Y.e4 + X.e45*Y.e45 - X.e5*Y.e5 + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2 - X.e123*Y.e23 - X.e1234*Y.e234 - X.e12345*Y.e2345 + X.e1235*Y.e235 - X.e124*Y.e24 + X.e1245*Y.e245 + X.e125*Y.e25 + X.e13*Y.e3 - X.e134*Y.e34 + X.e1345*Y.e345 + X.e135*Y.e35 + X.e14*Y.e4 + X.e145*Y.e45 - X.e15*Y.e5 - X.e2*Y.e12 - X.e23*Y.e123 + X.e234*Y.e1234 - X.e2345*Y.e12345 - X.e235*Y.e1235 - X.e24*Y.e124 - X.e245*Y.e1245 + X.e25*Y.e125 - X.e3*Y.e13 - X.e34*Y.e134 - X.e345*Y.e1345 + X.e35*Y.e135 - X.e4*Y.e14 + X.e45*Y.e145 + X.e5*Y.e15 + X.scalar*Y.e1, X.e1*Y.e12 - X.e12*Y.e1 + X.e123*Y.e13 + X.e1234*Y.e134 + X.e12345*Y.e1345 - X.e1235*Y.e135 + X.e124*Y.e14 - X.e1245*Y.e145 - X.e125*Y.e15 + X.e13*Y.e123 - X.e134*Y.e1234 + X.e1345*Y.e12345 + X.e135*Y.e1235 + X.e14*Y.e124 + X.e145*Y.e1245 - X.e15*Y.e125 + X.e2*Y.scalar + X.e23*Y.e3 - X.e234*Y.e34 + X.e2345*Y.e345 + X.e235*Y.e35 + X.e24*Y.e4 + X.e245*Y.e45 - X.e25*Y.e5 - X.e3*Y.e23 - X.e34*Y.e234 - X.e345*Y.e2345 + X.e35*Y.e235 - X.e4*Y.e24 + X.e45*Y.e245 + X.e5*Y.e25 + X.scalar*Y.e2, X.e1*Y.e13 - X.e12*Y.e123 - X.e123*Y.e12 - X.e1234*Y.e124 - X.e12345*Y.e1245 + X.e1235*Y.e125 + X.e124*Y.e1234 - X.e1245*Y.e12345 - X.e125*Y.e1235 - X.e13*Y.e1 + X.e134*Y.e14 - X.e1345*Y.e145 - X.e135*Y.e15 + X.e14*Y.e134 + X.e145*Y.e1345 - X.e15*Y.e135 + X.e2*Y.e23 - X.e23*Y.e2 + X.e234*Y.e24 - X.e2345*Y.e245 - X.e235*Y.e25 + X.e24*Y.e234 + X.e245*Y.e2345 - X.e25*Y.e235 + X.e3*Y.scalar + X.e34*Y.e4 + X.e345*Y.e45 - X.e35*Y.e5 - X.e4*Y.e34 + X.e45*Y.e345 + X.e5*Y.e35 + X.scalar*Y.e3, X.e1*Y.e14 - X.e12*Y.e124 - X.e123*Y.e1234 + X.e1234*Y.e123 + X.e12345*Y.e1235 + X.e1235*Y.e12345 - X.e124*Y.e12 + X.e1245*Y.e125 - X.e125*Y.e1245 - X.e13*Y.e134 - X.e134*Y.e13 + X.e1345*Y.e135 - X.e135*Y.e1345 - X.e14*Y.e1 - X.e145*Y.e15 - X.e15*Y.e145 + X.e2*Y.e24 - X.e23*Y.e234 - X.e234*Y.e23 + X.e2345*Y.e235 - X.e235*Y.e2345 - X.e24*Y.e2 - X.e245*Y.e25 - X.e25*Y.e245 + X.e3*Y.e34 - X.e34*Y.e3 - X.e345*Y.e35 - X.e35*Y.e345 + X.e4*Y.scalar - X.e45*Y.e5 + X.e5*Y.e45 + X.scalar*Y.e4, X.e1*Y.e15 - X.e12*Y.e125 - X.e123*Y.e1235 + X.e1234*Y.e12345 + X.e12345*Y.e1234 + X.e1235*Y.e123 - X.e124*Y.e1245 + X.e1245*Y.e124 - X.e125*Y.e12 - X.e13*Y.e135 - X.e134*Y.e1345 + X.e1345*Y.e134 - X.e135*Y.e13 - X.e14*Y.e145 - X.e145*Y.e14 - X.e15*Y.e1 + X.e2*Y.e25 - X.e23*Y.e235 - X.e234*Y.e2345 + X.e2345*Y.e234 - X.e235*Y.e23 - X.e24*Y.e245 - X.e245*Y.e24 - X.e25*Y.e2 + X.e3*Y.e35 - X.e34*Y.e345 - X.e345*Y.e34 - X.e35*Y.e3 + X.e4*Y.e45 - X.e45*Y.e4 + X.e5*Y.scalar + X.scalar*Y.e5, X.e1*Y.e2 + X.e12*Y.scalar + X.e123*Y.e3 - X.e1234*Y.e34 + X.e12345*Y.e345 + X.e1235*Y.e35 + X.e124*Y.e4 + X.e1245*Y.e45 - X.e125*Y.e5 - X.e13*Y.e23 - X.e134*Y.e234 - X.e1345*Y.e2345 + X.e135*Y.e235 - X.e14*Y.e24 + X.e145*Y.e245 + X.e15*Y.e25 - X.e2*Y.e1 + X.e23*Y.e13 + X.e234*Y.e134 + X.e2345*Y.e1345 - X.e235*Y.e135 + X.e24*Y.e14 - X.e245*Y.e145 - X.e25*Y.e15 + X.e3*Y.e123 - X.e34*Y.e1234 + X.e345*Y.e12345 + X.e35*Y.e1235 + X.e4*Y.e124 + X.e45*Y.e1245 - X.e5*Y.e125 + X.scalar*Y.e12, X.e1*Y.e3 + X.e12*Y.e23 - X.e123*Y.e2 + X.e1234*Y.e24 - X.e12345*Y.e245 - X.e1235*Y.e25 + X.e124*Y.e234 + X.e1245*Y.e2345 - X.e125*Y.e235 + X.e13*Y.scalar + X.e134*Y.e4 + X.e1345*Y.e45 - X.e135*Y.e5 - X.e14*Y.e34 + X.e145*Y.e345 + X.e15*Y.e35 - X.e2*Y.e123 - X.e23*Y.e12 - X.e234*Y.e124 - X.e2345*Y.e1245 + X.e235*Y.e125 + X.e24*Y.e1234 - X.e245*Y.e12345 - X.e25*Y.e1235 - X.e3*Y.e1 + X.e34*Y.e14 - X.e345*Y.e145 - X.e35*Y.e15 + X.e4*Y.e134 + X.e45*Y.e1345 - X.e5*Y.e135 + X.scalar*Y.e13, X.e1*Y.e4 + X.e12*Y.e24 - X.e123*Y.e234 - X.e1234*Y.e23 + X.e12345*Y.e235 - X.e1235*Y.e2345 - X.e124*Y.e2 - X.e1245*Y.e25 - X.e125*Y.e245 + X.e13*Y.e34 - X.e134*Y.e3 - X.e1345*Y.e35 - X.e135*Y.e345 + X.e14*Y.scalar - X.e145*Y.e5 + X.e15*Y.e45 - X.e2*Y.e124 - X.e23*Y.e1234 + X.e234*Y.e123 + X.e2345*Y.e1235 + X.e235*Y.e12345 - X.e24*Y.e12 + X.e245*Y.e125 - X.e25*Y.e1245 - X.e3*Y.e134 - X.e34*Y.e13 + X.e345*Y.e135 - X.e35*Y.e1345 - X.e4*Y.e1 - X.e45*Y.e15 - X.e5*Y.e145 + X.scalar*Y.e14, X.e1*Y.e5 + X.e12*Y.e25 - X.e123*Y.e235 - X.e1234*Y.e2345 + X.e12345*Y.e234 - X.e1235*Y.e23 - X.e124*Y.e245 - X.e1245*Y.e24 - X.e125*Y.e2 + X.e13*Y.e35 - X.e134*Y.e345 - X.e1345*Y.e34 - X.e135*Y.e3 + X.e14*Y.e45 - X.e145*Y.e4 + X.e15*Y.scalar - X.e2*Y.e125 - X.e23*Y.e1235 + X.e234*Y.e12345 + X.e2345*Y.e1234 + X.e235*Y.e123 - X.e24*Y.e1245 + X.e245*Y.e124 - X.e25*Y.e12 - X.e3*Y.e135 - X.e34*Y.e1345 + X.e345*Y.e134 - X.e35*Y.e13 - X.e4*Y.e145 - X.e45*Y.e14 - X.e5*Y.e1 + X.scalar*Y.e15, X.e1*Y.e123 - X.e12*Y.e13 + X.e123*Y.e1 - X.e1234*Y.e14 + X.e12345*Y.e145 + X.e1235*Y.e15 - X.e124*Y.e134 - X.e1245*Y.e1345 + X.e125*Y.e135 + X.e13*Y.e12 + X.e134*Y.e124 + X.e1345*Y.e1245 - X.e135*Y.e125 - X.e14*Y.e1234 + X.e145*Y.e12345 + X.e15*Y.e1235 + X.e2*Y.e3 + X.e23*Y.scalar + X.e234*Y.e4 + X.e2345*Y.e45 - X.e235*Y.e5 - X.e24*Y.e34 + X.e245*Y.e345 + X.e25*Y.e35 - X.e3*Y.e2 + X.e34*Y.e24 - X.e345*Y.e245 - X.e35*Y.e25 + X.e4*Y.e234 + X.e45*Y.e2345 - X.e5*Y.e235 + X.scalar*Y.e23, X.e1*Y.e124 - X.e12*Y.e14 + X.e123*Y.e134 + X.e1234*Y.e13 - X.e12345*Y.e135 + X.e1235*Y.e1345 + X.e124*Y.e1 + X.e1245*Y.e15 + X.e125*Y.e145 + X.e13*Y.e1234 - X.e134*Y.e123 - X.e1345*Y.e1235 - X.e135*Y.e12345 + X.e14*Y.e12 - X.e145*Y.e125 + X.e15*Y.e1245 + X.e2*Y.e4 + X.e23*Y.e34 - X.e234*Y.e3 - X.e2345*Y.e35 - X.e235*Y.e345 + X.e24*Y.scalar - X.e245*Y.e5 + X.e25*Y.e45 - X.e3*Y.e234 - X.e34*Y.e23 + X.e345*Y.e235 - X.e35*Y.e2345 - X.e4*Y.e2 - X.e45*Y.e25 - X.e5*Y.e245 + X.scalar*Y.e24, X.e1*Y.e125 - X.e12*Y.e15 + X.e123*Y.e135 + X.e1234*Y.e1345 - X.e12345*Y.e134 + X.e1235*Y.e13 + X.e124*Y.e145 + X.e1245*Y.e14 + X.e125*Y.e1 + X.e13*Y.e1235 - X.e134*Y.e12345 - X.e1345*Y.e1234 - X.e135*Y.e123 + X.e14*Y.e1245 - X.e145*Y.e124 + X.e15*Y.e12 + X.e2*Y.e5 + X.e23*Y.e35 - X.e234*Y.e345 - X.e2345*Y.e34 - X.e235*Y.e3 + X.e24*Y.e45 - X.e245*Y.e4 + X.e25*Y.scalar - X.e3*Y.e235 - X.e34*Y.e2345 + X.e345*Y.e234 - X.e35*Y.e23 - X.e4*Y.e245 - X.e45*Y.e24 - X.e5*Y.e2 + X.scalar*Y.e25, X.e1*Y.e134 - X.e12*Y.e1234 - X.e123*Y.e124 - X.e1234*Y.e12 + X.e12345*Y.e125 - X.e1235*Y.e1245 + X.e124*Y.e123 + X.e1245*Y.e1235 + X.e125*Y.e12345 - X.e13*Y.e14 + X.e134*Y.e1 + X.e1345*Y.e15 + X.e135*Y.e145 + X.e14*Y.e13 - X.e145*Y.e135 + X.e15*Y.e1345 + X.e2*Y.e234 - X.e23*Y.e24 + X.e234*Y.e2 + X.e2345*Y.e25 + X.e235*Y.e245 + X.e24*Y.e23 - X.e245*Y.e235 + X.e25*Y.e2345 + X.e3*Y.e4 + X.e34*Y.scalar - X.e345*Y.e5 + X.e35*Y.e45 - X.e4*Y.e3 - X.e45*Y.e35 - X.e5*Y.e345 + X.scalar*Y.e34, X.e1*Y.e135 - X.e12*Y.e1235 - X.e123*Y.e125 - X.e1234*Y.e1245 + X.e12345*Y.e124 - X.e1235*Y.e12 + X.e124*Y.e12345 + X.e1245*Y.e1234 + X.e125*Y.e123 - X.e13*Y.e15 + X.e134*Y.e145 + X.e1345*Y.e14 + X.e135*Y.e1 + X.e14*Y.e1345 - X.e145*Y.e134 + X.e15*Y.e13 + X.e2*Y.e235 - X.e23*Y.e25 + X.e234*Y.e245 + X.e2345*Y.e24 + X.e235*Y.e2 + X.e24*Y.e2345 - X.e245*Y.e234 + X.e25*Y.e23 + X.e3*Y.e5 + X.e34*Y.e45 - X.e345*Y.e4 + X.e35*Y.scalar - X.e4*Y.e345 - X.e45*Y.e34 - X.e5*Y.e3 + X.scalar*Y.e35, X.e1*Y.e145 - X.e12*Y.e1245 - X.e123*Y.e12345 + X.e1234*Y.e1235 - X.e12345*Y.e123 - X.e1235*Y.e1234 - X.e124*Y.e125 - X.e1245*Y.e12 + X.e125*Y.e124 - X.e13*Y.e1345 - X.e134*Y.e135 - X.e1345*Y.e13 + X.e135*Y.e134 - X.e14*Y.e15 + X.e145*Y.e1 + X.e15*Y.e14 + X.e2*Y.e245 - X.e23*Y.e2345 - X.e234*Y.e235 - X.e2345*Y.e23 + X.e235*Y.e234 - X.e24*Y.e25 + X.e245*Y.e2 + X.e25*Y.e24 + X.e3*Y.e345 - X.e34*Y.e35 + X.e345*Y.e3 + X.e35*Y.e34 + X.e4*Y.e5 + X.e45*Y.scalar - X.e5*Y.e4 + X.scalar*Y.e45, X.e1*Y.e23 + X.e12*Y.e3 + X.e123*Y.scalar + X.e1234*Y.e4 + X.e12345*Y.e45 - X.e1235*Y.e5 - X.e124*Y.e34 + X.e1245*Y.e345 + X.e125*Y.e35 - X.e13*Y.e2 + X.e134*Y.e24 - X.e1345*Y.e245 - X.e135*Y.e25 + X.e14*Y.e234 + X.e145*Y.e2345 - X.e15*Y.e235 - X.e2*Y.e13 + X.e23*Y.e1 - X.e234*Y.e14 + X.e2345*Y.e145 + X.e235*Y.e15 - X.e24*Y.e134 - X.e245*Y.e1345 + X.e25*Y.e135 + X.e3*Y.e12 + X.e34*Y.e124 + X.e345*Y.e1245 - X.e35*Y.e125 - X.e4*Y.e1234 + X.e45*Y.e12345 + X.e5*Y.e1235 + X.scalar*Y.e123, X.e1*Y.e24 + X.e12*Y.e4 + X.e123*Y.e34 - X.e1234*Y.e3 - X.e12345*Y.e35 - X.e1235*Y.e345 + X.e124*Y.scalar - X.e1245*Y.e5 + X.e125*Y.e45 - X.e13*Y.e234 - X.e134*Y.e23 + X.e1345*Y.e235 - X.e135*Y.e2345 - X.e14*Y.e2 - X.e145*Y.e25 - X.e15*Y.e245 - X.e2*Y.e14 + X.e23*Y.e134 + X.e234*Y.e13 - X.e2345*Y.e135 + X.e235*Y.e1345 + X.e24*Y.e1 + X.e245*Y.e15 + X.e25*Y.e145 + X.e3*Y.e1234 - X.e34*Y.e123 - X.e345*Y.e1235 - X.e35*Y.e12345 + X.e4*Y.e12 - X.e45*Y.e125 + X.e5*Y.e1245 + X.scalar*Y.e124, X.e1*Y.e25 + X.e12*Y.e5 + X.e123*Y.e35 - X.e1234*Y.e345 - X.e12345*Y.e34 - X.e1235*Y.e3 + X.e124*Y.e45 - X.e1245*Y.e4 + X.e125*Y.scalar - X.e13*Y.e235 - X.e134*Y.e2345 + X.e1345*Y.e234 - X.e135*Y.e23 - X.e14*Y.e245 - X.e145*Y.e24 - X.e15*Y.e2 - X.e2*Y.e15 + X.e23*Y.e135 + X.e234*Y.e1345 - X.e2345*Y.e134 + X.e235*Y.e13 + X.e24*Y.e145 + X.e245*Y.e14 + X.e25*Y.e1 + X.e3*Y.e1235 - X.e34*Y.e12345 - X.e345*Y.e1234 - X.e35*Y.e123 + X.e4*Y.e1245 - X.e45*Y.e124 + X.e5*Y.e12 + X.scalar*Y.e125, X.e1*Y.e34 + X.e12*Y.e234 - X.e123*Y.e24 + X.e1234*Y.e2 + X.e12345*Y.e25 + X.e1235*Y.e245 + X.e124*Y.e23 - X.e1245*Y.e235 + X.e125*Y.e2345 + X.e13*Y.e4 + X.e134*Y.scalar - X.e1345*Y.e5 + X.e135*Y.e45 - X.e14*Y.e3 - X.e145*Y.e35 - X.e15*Y.e345 - X.e2*Y.e1234 - X.e23*Y.e124 - X.e234*Y.e12 + X.e2345*Y.e125 - X.e235*Y.e1245 + X.e24*Y.e123 + X.e245*Y.e1235 + X.e25*Y.e12345 - X.e3*Y.e14 + X.e34*Y.e1 + X.e345*Y.e15 + X.e35*Y.e145 + X.e4*Y.e13 - X.e45*Y.e135 + X.e5*Y.e1345 + X.scalar*Y.e134, X.e1*Y.e35 + X.e12*Y.e235 - X.e123*Y.e25 + X.e1234*Y.e245 + X.e12345*Y.e24 + X.e1235*Y.e2 + X.e124*Y.e2345 - X.e1245*Y.e234 + X.e125*Y.e23 + X.e13*Y.e5 + X.e134*Y.e45 - X.e1345*Y.e4 + X.e135*Y.scalar - X.e14*Y.e345 - X.e145*Y.e34 - X.e15*Y.e3 - X.e2*Y.e1235 - X.e23*Y.e125 - X.e234*Y.e1245 + X.e2345*Y.e124 - X.e235*Y.e12 + X.e24*Y.e12345 + X.e245*Y.e1234 + X.e25*Y.e123 - X.e3*Y.e15 + X.e34*Y.e145 + X.e345*Y.e14 + X.e35*Y.e1 + X.e4*Y.e1345 - X.e45*Y.e134 + X.e5*Y.e13 + X.scalar*Y.e135, X.e1*Y.e45 + X.e12*Y.e245 - X.e123*Y.e2345 - X.e1234*Y.e235 - X.e12345*Y.e23 + X.e1235*Y.e234 - X.e124*Y.e25 + X.e1245*Y.e2 + X.e125*Y.e24 + X.e13*Y.e345 - X.e134*Y.e35 + X.e1345*Y.e3 + X.e135*Y.e34 + X.e14*Y.e5 + X.e145*Y.scalar - X.e15*Y.e4 - X.e2*Y.e1245 - X.e23*Y.e12345 + X.e234*Y.e1235 - X.e2345*Y.e123 - X.e235*Y.e1234 - X.e24*Y.e125 - X.e245*Y.e12 + X.e25*Y.e124 - X.e3*Y.e1345 - X.e34*Y.e135 - X.e345*Y.e13 + X.e35*Y.e134 - X.e4*Y.e15 + X.e45*Y.e1 + X.e5*Y.e14 + X.scalar*Y.e145, X.e1*Y.e1234 - X.e12*Y.e134 + X.e123*Y.e14 - X.e1234*Y.e1 - X.e12345*Y.e15 - X.e1235*Y.e145 - X.e124*Y.e13 + X.e1245*Y.e135 - X.e125*Y.e1345 + X.e13*Y.e124 + X.e134*Y.e12 - X.e1345*Y.e125 + X.e135*Y.e1245 - X.e14*Y.e123 - X.e145*Y.e1235 - X.e15*Y.e12345 + X.e2*Y.e34 + X.e23*Y.e4 + X.e234*Y.scalar - X.e2345*Y.e5 + X.e235*Y.e45 - X.e24*Y.e3 - X.e245*Y.e35 - X.e25*Y.e345 - X.e3*Y.e24 + X.e34*Y.e2 + X.e345*Y.e25 + X.e35*Y.e245 + X.e4*Y.e23 - X.e45*Y.e235 + X.e5*Y.e2345 + X.scalar*Y.e234, X.e1*Y.e1235 - X.e12*Y.e135 + X.e123*Y.e15 - X.e1234*Y.e145 - X.e12345*Y.e14 - X.e1235*Y.e1 - X.e124*Y.e1345 + X.e1245*Y.e134 - X.e125*Y.e13 + X.e13*Y.e125 + X.e134*Y.e1245 - X.e1345*Y.e124 + X.e135*Y.e12 - X.e14*Y.e12345 - X.e145*Y.e1234 - X.e15*Y.e123 + X.e2*Y.e35 + X.e23*Y.e5 + X.e234*Y.e45 - X.e2345*Y.e4 + X.e235*Y.scalar - X.e24*Y.e345 - X.e245*Y.e34 - X.e25*Y.e3 - X.e3*Y.e25 + X.e34*Y.e245 + X.e345*Y.e24 + X.e35*Y.e2 + X.e4*Y.e2345 - X.e45*Y.e234 + X.e5*Y.e23 + X.scalar*Y.e235, X.e1*Y.e1245 - X.e12*Y.e145 + X.e123*Y.e1345 + X.e1234*Y.e135 + X.e12345*Y.e13 - X.e1235*Y.e134 + X.e124*Y.e15 - X.e1245*Y.e1 - X.e125*Y.e14 + X.e13*Y.e12345 - X.e134*Y.e1235 + X.e1345*Y.e123 + X.e135*Y.e1234 + X.e14*Y.e125 + X.e145*Y.e12 - X.e15*Y.e124 + X.e2*Y.e45 + X.e23*Y.e345 - X.e234*Y.e35 + X.e2345*Y.e3 + X.e235*Y.e34 + X.e24*Y.e5 + X.e245*Y.scalar - X.e25*Y.e4 - X.e3*Y.e2345 - X.e34*Y.e235 - X.e345*Y.e23 + X.e35*Y.e234 - X.e4*Y.e25 + X.e45*Y.e2 + X.e5*Y.e24 + X.scalar*Y.e245, X.e1*Y.e1345 - X.e12*Y.e12345 - X.e123*Y.e1245 - X.e1234*Y.e125 - X.e12345*Y.e12 + X.e1235*Y.e124 + X.e124*Y.e1235 - X.e1245*Y.e123 - X.e125*Y.e1234 - X.e13*Y.e145 + X.e134*Y.e15 - X.e1345*Y.e1 - X.e135*Y.e14 + X.e14*Y.e135 + X.e145*Y.e13 - X.e15*Y.e134 + X.e2*Y.e2345 - X.e23*Y.e245 + X.e234*Y.e25 - X.e2345*Y.e2 - X.e235*Y.e24 + X.e24*Y.e235 + X.e245*Y.e23 - X.e25*Y.e234 + X.e3*Y.e45 + X.e34*Y.e5 + X.e345*Y.scalar - X.e35*Y.e4 - X.e4*Y.e35 + X.e45*Y.e3 + X.e5*Y.e34 + X.scalar*Y.e345, X.e1*Y.e234 + X.e12*Y.e34 + X.e123*Y.e4 + X.e1234*Y.scalar - X.e12345*Y.e5 + X.e1235*Y.e45 - X.e124*Y.e3 - X.e1245*Y.e35 - X.e125*Y.e345 - X.e13*Y.e24 + X.e134*Y.e2 + X.e1345*Y.e25 + X.e135*Y.e245 + X.e14*Y.e23 - X.e145*Y.e235 + X.e15*Y.e2345 - X.e2*Y.e134 + X.e23*Y.e14 - X.e234*Y.e1 - X.e2345*Y.e15 - X.e235*Y.e145 - X.e24*Y.e13 + X.e245*Y.e135 - X.e25*Y.e1345 + X.e3*Y.e124 + X.e34*Y.e12 - X.e345*Y.e125 + X.e35*Y.e1245 - X.e4*Y.e123 - X.e45*Y.e1235 - X.e5*Y.e12345 + X.scalar*Y.e1234, X.e1*Y.e235 + X.e12*Y.e35 + X.e123*Y.e5 + X.e1234*Y.e45 - X.e12345*Y.e4 + X.e1235*Y.scalar - X.e124*Y.e345 - X.e1245*Y.e34 - X.e125*Y.e3 - X.e13*Y.e25 + X.e134*Y.e245 + X.e1345*Y.e24 + X.e135*Y.e2 + X.e14*Y.e2345 - X.e145*Y.e234 + X.e15*Y.e23 - X.e2*Y.e135 + X.e23*Y.e15 - X.e234*Y.e145 - X.e2345*Y.e14 - X.e235*Y.e1 - X.e24*Y.e1345 + X.e245*Y.e134 - X.e25*Y.e13 + X.e3*Y.e125 + X.e34*Y.e1245 - X.e345*Y.e124 + X.e35*Y.e12 - X.e4*Y.e12345 - X.e45*Y.e1234 - X.e5*Y.e123 + X.scalar*Y.e1235, X.e1*Y.e245 + X.e12*Y.e45 + X.e123*Y.e345 - X.e1234*Y.e35 + X.e12345*Y.e3 + X.e1235*Y.e34 + X.e124*Y.e5 + X.e1245*Y.scalar - X.e125*Y.e4 - X.e13*Y.e2345 - X.e134*Y.e235 - X.e1345*Y.e23 + X.e135*Y.e234 - X.e14*Y.e25 + X.e145*Y.e2 + X.e15*Y.e24 - X.e2*Y.e145 + X.e23*Y.e1345 + X.e234*Y.e135 + X.e2345*Y.e13 - X.e235*Y.e134 + X.e24*Y.e15 - X.e245*Y.e1 - X.e25*Y.e14 + X.e3*Y.e12345 - X.e34*Y.e1235 + X.e345*Y.e123 + X.e35*Y.e1234 + X.e4*Y.e125 + X.e45*Y.e12 - X.e5*Y.e124 + X.scalar*Y.e1245, X.e1*Y.e345 + X.e12*Y.e2345 - X.e123*Y.e245 + X.e1234*Y.e25 - X.e12345*Y.e2 - X.e1235*Y.e24 + X.e124*Y.e235 + X.e1245*Y.e23 - X.e125*Y.e234 + X.e13*Y.e45 + X.e134*Y.e5 + X.e1345*Y.scalar - X.e135*Y.e4 - X.e14*Y.e35 + X.e145*Y.e3 + X.e15*Y.e34 - X.e2*Y.e12345 - X.e23*Y.e1245 - X.e234*Y.e125 - X.e2345*Y.e12 + X.e235*Y.e124 + X.e24*Y.e1235 - X.e245*Y.e123 - X.e25*Y.e1234 - X.e3*Y.e145 + X.e34*Y.e15 - X.e345*Y.e1 - X.e35*Y.e14 + X.e4*Y.e135 + X.e45*Y.e13 - X.e5*Y.e134 + X.scalar*Y.e1345, X.e1*Y.e12345 - X.e12*Y.e1345 + X.e123*Y.e145 - X.e1234*Y.e15 + X.e12345*Y.e1 + X.e1235*Y.e14 - X.e124*Y.e135 - X.e1245*Y.e13 + X.e125*Y.e134 + X.e13*Y.e1245 + X.e134*Y.e125 + X.e1345*Y.e12 - X.e135*Y.e124 - X.e14*Y.e1235 + X.e145*Y.e123 + X.e15*Y.e1234 + X.e2*Y.e345 + X.e23*Y.e45 + X.e234*Y.e5 + X.e2345*Y.scalar - X.e235*Y.e4 - X.e24*Y.e35 + X.e245*Y.e3 + X.e25*Y.e34 - X.e3*Y.e245 + X.e34*Y.e25 - X.e345*Y.e2 - X.e35*Y.e24 + X.e4*Y.e235 + X.e45*Y.e23 - X.e5*Y.e234 + X.scalar*Y.e2345, X.e1*Y.e2345 + X.e12*Y.e345 + X.e123*Y.e45 + X.e1234*Y.e5 + X.e12345*Y.scalar - X.e1235*Y.e4 - X.e124*Y.e35 + X.e1245*Y.e3 + X.e125*Y.e34 - X.e13*Y.e245 + X.e134*Y.e25 - X.e1345*Y.e2 - X.e135*Y.e24 + X.e14*Y.e235 + X.e145*Y.e23 - X.e15*Y.e234 - X.e2*Y.e1345 + X.e23*Y.e145 - X.e234*Y.e15 + X.e2345*Y.e1 + X.e235*Y.e14 - X.e24*Y.e135 - X.e245*Y.e13 + X.e25*Y.e134 + X.e3*Y.e1245 + X.e34*Y.e125 + X.e345*Y.e12 - X.e35*Y.e124 - X.e4*Y.e1235 + X.e45*Y.e123 + X.e5*Y.e1234 + X.scalar*Y.e12345);
}

CGA3 scalar_CGA3(float a){
    return mul(a, ONE_CGA3);
}

CGA3 mul(CGA3 X, CGA3 Y, CGA3 Z){
    return mul(mul(X, Y), Z);
}

CGA3 involve(CGA3 X){
    return CGA3(X.scalar, -X.e1, -X.e2, -X.e3, -X.e4, -X.e5, X.e12, X.e13, X.e14, X.e15, X.e23, X.e24, X.e25, X.e34, X.e35, X.e45, -X.e123, -X.e124, -X.e125, -X.e134, -X.e135, -X.e145, -X.e234, -X.e235, -X.e245, -X.e345, X.e1234, X.e1235, X.e1245, X.e1345, X.e2345, -X.e12345);
}

CGA3 inner(CGA3 X, CGA3 Y){
    return CGA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 + X.e1234*Y.e1234 - X.e12345*Y.e12345 - X.e1235*Y.e1235 - X.e124*Y.e124 - X.e1245*Y.e1245 + X.e125*Y.e125 - X.e13*Y.e13 - X.e134*Y.e134 - X.e1345*Y.e1345 + X.e135*Y.e135 - X.e14*Y.e14 + X.e145*Y.e145 + X.e15*Y.e15 + X.e2*Y.e2 - X.e23*Y.e23 - X.e234*Y.e234 - X.e2345*Y.e2345 + X.e235*Y.e235 - X.e24*Y.e24 + X.e245*Y.e245 + X.e25*Y.e25 + X.e3*Y.e3 - X.e34*Y.e34 + X.e345*Y.e345 + X.e35*Y.e35 + X.e4*Y.e4 + X.e45*Y.e45 - X.e5*Y.e5, X.e12*Y.e2 - X.e123*Y.e23 - X.e1234*Y.e234 - X.e12345*Y.e2345 + X.e1235*Y.e235 - X.e124*Y.e24 + X.e1245*Y.e245 + X.e125*Y.e25 + X.e13*Y.e3 - X.e134*Y.e34 + X.e1345*Y.e345 + X.e135*Y.e35 + X.e14*Y.e4 + X.e145*Y.e45 - X.e15*Y.e5 - X.e2*Y.e12 - X.e23*Y.e123 + X.e234*Y.e1234 - X.e2345*Y.e12345 - X.e235*Y.e1235 - X.e24*Y.e124 - X.e245*Y.e1245 + X.e25*Y.e125 - X.e3*Y.e13 - X.e34*Y.e134 - X.e345*Y.e1345 + X.e35*Y.e135 - X.e4*Y.e14 + X.e45*Y.e145 + X.e5*Y.e15, X.e1*Y.e12 - X.e12*Y.e1 + X.e123*Y.e13 + X.e1234*Y.e134 + X.e12345*Y.e1345 - X.e1235*Y.e135 + X.e124*Y.e14 - X.e1245*Y.e145 - X.e125*Y.e15 + X.e13*Y.e123 - X.e134*Y.e1234 + X.e1345*Y.e12345 + X.e135*Y.e1235 + X.e14*Y.e124 + X.e145*Y.e1245 - X.e15*Y.e125 + X.e23*Y.e3 - X.e234*Y.e34 + X.e2345*Y.e345 + X.e235*Y.e35 + X.e24*Y.e4 + X.e245*Y.e45 - X.e25*Y.e5 - X.e3*Y.e23 - X.e34*Y.e234 - X.e345*Y.e2345 + X.e35*Y.e235 - X.e4*Y.e24 + X.e45*Y.e245 + X.e5*Y.e25, X.e1*Y.e13 - X.e12*Y.e123 - X.e123*Y.e12 - X.e1234*Y.e124 - X.e12345*Y.e1245 + X.e1235*Y.e125 + X.e124*Y.e1234 - X.e1245*Y.e12345 - X.e125*Y.e1235 - X.e13*Y.e1 + X.e134*Y.e14 - X.e1345*Y.e145 - X.e135*Y.e15 + X.e14*Y.e134 + X.e145*Y.e1345 - X.e15*Y.e135 + X.e2*Y.e23 - X.e23*Y.e2 + X.e234*Y.e24 - X.e2345*Y.e245 - X.e235*Y.e25 + X.e24*Y.e234 + X.e245*Y.e2345 - X.e25*Y.e235 + X.e34*Y.e4 + X.e345*Y.e45 - X.e35*Y.e5 - X.e4*Y.e34 + X.e45*Y.e345 + X.e5*Y.e35, X.e1*Y.e14 - X.e12*Y.e124 - X.e123*Y.e1234 + X.e1234*Y.e123 + X.e12345*Y.e1235 + X.e1235*Y.e12345 - X.e124*Y.e12 + X.e1245*Y.e125 - X.e125*Y.e1245 - X.e13*Y.e134 - X.e134*Y.e13 + X.e1345*Y.e135 - X.e135*Y.e1345 - X.e14*Y.e1 - X.e145*Y.e15 - X.e15*Y.e145 + X.e2*Y.e24 - X.e23*Y.e234 - X.e234*Y.e23 + X.e2345*Y.e235 - X.e235*Y.e2345 - X.e24*Y.e2 - X.e245*Y.e25 - X.e25*Y.e245 + X.e3*Y.e34 - X.e34*Y.e3 - X.e345*Y.e35 - X.e35*Y.e345 - X.e45*Y.e5 + X.e5*Y.e45, X.e1*Y.e15 - X.e12*Y.e125 - X.e123*Y.e1235 + X.e1234*Y.e12345 + X.e12345*Y.e1234 + X.e1235*Y.e123 - X.e124*Y.e1245 + X.e1245*Y.e124 - X.e125*Y.e12 - X.e13*Y.e135 - X.e134*Y.e1345 + X.e1345*Y.e134 - X.e135*Y.e13 - X.e14*Y.e145 - X.e145*Y.e14 - X.e15*Y.e1 + X.e2*Y.e25 - X.e23*Y.e235 - X.e234*Y.e2345 + X.e2345*Y.e234 - X.e235*Y.e23 - X.e24*Y.e245 - X.e245*Y.e24 - X.e25*Y.e2 + X.e3*Y.e35 - X.e34*Y.e345 - X.e345*Y.e34 - X.e35*Y.e3 + X.e4*Y.e45 - X.e45*Y.e4, X.e123*Y.e3 - X.e1234*Y.e34 + X.e12345*Y.e345 + X.e1235*Y.e35 + X.e124*Y.e4 + X.e1245*Y.e45 - X.e125*Y.e5 + X.e3*Y.e123 - X.e34*Y.e1234 + X.e345*Y.e12345 + X.e35*Y.e1235 + X.e4*Y.e124 + X.e45*Y.e1245 - X.e5*Y.e125, -X.e123*Y.e2 + X.e1234*Y.e24 - X.e12345*Y.e245 - X.e1235*Y.e25 + X.e134*Y.e4 + X.e1345*Y.e45 - X.e135*Y.e5 - X.e2*Y.e123 + X.e24*Y.e1234 - X.e245*Y.e12345 - X.e25*Y.e1235 + X.e4*Y.e134 + X.e45*Y.e1345 - X.e5*Y.e135, -X.e1234*Y.e23 + X.e12345*Y.e235 - X.e124*Y.e2 - X.e1245*Y.e25 - X.e134*Y.e3 - X.e1345*Y.e35 - X.e145*Y.e5 - X.e2*Y.e124 - X.e23*Y.e1234 + X.e235*Y.e12345 - X.e25*Y.e1245 - X.e3*Y.e134 - X.e35*Y.e1345 - X.e5*Y.e145, X.e12345*Y.e234 - X.e1235*Y.e23 - X.e1245*Y.e24 - X.e125*Y.e2 - X.e1345*Y.e34 - X.e135*Y.e3 - X.e145*Y.e4 - X.e2*Y.e125 - X.e23*Y.e1235 + X.e234*Y.e12345 - X.e24*Y.e1245 - X.e3*Y.e135 - X.e34*Y.e1345 - X.e4*Y.e145, X.e1*Y.e123 + X.e123*Y.e1 - X.e1234*Y.e14 + X.e12345*Y.e145 + X.e1235*Y.e15 - X.e14*Y.e1234 + X.e145*Y.e12345 + X.e15*Y.e1235 + X.e234*Y.e4 + X.e2345*Y.e45 - X.e235*Y.e5 + X.e4*Y.e234 + X.e45*Y.e2345 - X.e5*Y.e235, X.e1*Y.e124 + X.e1234*Y.e13 - X.e12345*Y.e135 + X.e124*Y.e1 + X.e1245*Y.e15 + X.e13*Y.e1234 - X.e135*Y.e12345 + X.e15*Y.e1245 - X.e234*Y.e3 - X.e2345*Y.e35 - X.e245*Y.e5 - X.e3*Y.e234 - X.e35*Y.e2345 - X.e5*Y.e245, X.e1*Y.e125 - X.e12345*Y.e134 + X.e1235*Y.e13 + X.e1245*Y.e14 + X.e125*Y.e1 + X.e13*Y.e1235 - X.e134*Y.e12345 + X.e14*Y.e1245 - X.e2345*Y.e34 - X.e235*Y.e3 - X.e245*Y.e4 - X.e3*Y.e235 - X.e34*Y.e2345 - X.e4*Y.e245, X.e1*Y.e134 - X.e12*Y.e1234 - X.e1234*Y.e12 + X.e12345*Y.e125 + X.e125*Y.e12345 + X.e134*Y.e1 + X.e1345*Y.e15 + X.e15*Y.e1345 + X.e2*Y.e234 + X.e234*Y.e2 + X.e2345*Y.e25 + X.e25*Y.e2345 - X.e345*Y.e5 - X.e5*Y.e345, X.e1*Y.e135 - X.e12*Y.e1235 + X.e12345*Y.e124 - X.e1235*Y.e12 + X.e124*Y.e12345 + X.e1345*Y.e14 + X.e135*Y.e1 + X.e14*Y.e1345 + X.e2*Y.e235 + X.e2345*Y.e24 + X.e235*Y.e2 + X.e24*Y.e2345 - X.e345*Y.e4 - X.e4*Y.e345, X.e1*Y.e145 - X.e12*Y.e1245 - X.e123*Y.e12345 - X.e12345*Y.e123 - X.e1245*Y.e12 - X.e13*Y.e1345 - X.e1345*Y.e13 + X.e145*Y.e1 + X.e2*Y.e245 - X.e23*Y.e2345 - X.e2345*Y.e23 + X.e245*Y.e2 + X.e3*Y.e345 + X.e345*Y.e3, X.e1234*Y.e4 + X.e12345*Y.e45 - X.e1235*Y.e5 - X.e4*Y.e1234 + X.e45*Y.e12345 + X.e5*Y.e1235, -X.e1234*Y.e3 - X.e12345*Y.e35 - X.e1245*Y.e5 + X.e3*Y.e1234 - X.e35*Y.e12345 + X.e5*Y.e1245, -X.e12345*Y.e34 - X.e1235*Y.e3 - X.e1245*Y.e4 + X.e3*Y.e1235 - X.e34*Y.e12345 + X.e4*Y.e1245, X.e1234*Y.e2 + X.e12345*Y.e25 - X.e1345*Y.e5 - X.e2*Y.e1234 + X.e25*Y.e12345 + X.e5*Y.e1345, X.e12345*Y.e24 + X.e1235*Y.e2 - X.e1345*Y.e4 - X.e2*Y.e1235 + X.e24*Y.e12345 + X.e4*Y.e1345, -X.e12345*Y.e23 + X.e1245*Y.e2 + X.e1345*Y.e3 - X.e2*Y.e1245 - X.e23*Y.e12345 - X.e3*Y.e1345, X.e1*Y.e1234 - X.e1234*Y.e1 - X.e12345*Y.e15 - X.e15*Y.e12345 - X.e2345*Y.e5 + X.e5*Y.e2345, X.e1*Y.e1235 - X.e12345*Y.e14 - X.e1235*Y.e1 - X.e14*Y.e12345 - X.e2345*Y.e4 + X.e4*Y.e2345, X.e1*Y.e1245 + X.e12345*Y.e13 - X.e1245*Y.e1 + X.e13*Y.e12345 + X.e2345*Y.e3 - X.e3*Y.e2345, X.e1*Y.e1345 - X.e12*Y.e12345 - X.e12345*Y.e12 - X.e1345*Y.e1 + X.e2*Y.e2345 - X.e2345*Y.e2, -X.e12345*Y.e5 - X.e5*Y.e12345, -X.e12345*Y.e4 - X.e4*Y.e12345, X.e12345*Y.e3 + X.e3*Y.e12345, -X.e12345*Y.e2 - X.e2*Y.e12345, X.e1*Y.e12345 + X.e12345*Y.e1, 0.0);
}

CGA3 lcontract(CGA3 X, CGA3 Y){
    return CGA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 + X.e1234*Y.e1234 - X.e12345*Y.e12345 - X.e1235*Y.e1235 - X.e124*Y.e124 - X.e1245*Y.e1245 + X.e125*Y.e125 - X.e13*Y.e13 - X.e134*Y.e134 - X.e1345*Y.e1345 + X.e135*Y.e135 - X.e14*Y.e14 + X.e145*Y.e145 + X.e15*Y.e15 + X.e2*Y.e2 - X.e23*Y.e23 - X.e234*Y.e234 - X.e2345*Y.e2345 + X.e235*Y.e235 - X.e24*Y.e24 + X.e245*Y.e245 + X.e25*Y.e25 + X.e3*Y.e3 - X.e34*Y.e34 + X.e345*Y.e345 + X.e35*Y.e35 + X.e4*Y.e4 + X.e45*Y.e45 - X.e5*Y.e5 + X.scalar*Y.scalar, -X.e2*Y.e12 - X.e23*Y.e123 + X.e234*Y.e1234 - X.e2345*Y.e12345 - X.e235*Y.e1235 - X.e24*Y.e124 - X.e245*Y.e1245 + X.e25*Y.e125 - X.e3*Y.e13 - X.e34*Y.e134 - X.e345*Y.e1345 + X.e35*Y.e135 - X.e4*Y.e14 + X.e45*Y.e145 + X.e5*Y.e15 + X.scalar*Y.e1, X.e1*Y.e12 + X.e13*Y.e123 - X.e134*Y.e1234 + X.e1345*Y.e12345 + X.e135*Y.e1235 + X.e14*Y.e124 + X.e145*Y.e1245 - X.e15*Y.e125 - X.e3*Y.e23 - X.e34*Y.e234 - X.e345*Y.e2345 + X.e35*Y.e235 - X.e4*Y.e24 + X.e45*Y.e245 + X.e5*Y.e25 + X.scalar*Y.e2, X.e1*Y.e13 - X.e12*Y.e123 + X.e124*Y.e1234 - X.e1245*Y.e12345 - X.e125*Y.e1235 + X.e14*Y.e134 + X.e145*Y.e1345 - X.e15*Y.e135 + X.e2*Y.e23 + X.e24*Y.e234 + X.e245*Y.e2345 - X.e25*Y.e235 - X.e4*Y.e34 + X.e45*Y.e345 + X.e5*Y.e35 + X.scalar*Y.e3, X.e1*Y.e14 - X.e12*Y.e124 - X.e123*Y.e1234 + X.e1235*Y.e12345 - X.e125*Y.e1245 - X.e13*Y.e134 - X.e135*Y.e1345 - X.e15*Y.e145 + X.e2*Y.e24 - X.e23*Y.e234 - X.e235*Y.e2345 - X.e25*Y.e245 + X.e3*Y.e34 - X.e35*Y.e345 + X.e5*Y.e45 + X.scalar*Y.e4, X.e1*Y.e15 - X.e12*Y.e125 - X.e123*Y.e1235 + X.e1234*Y.e12345 - X.e124*Y.e1245 - X.e13*Y.e135 - X.e134*Y.e1345 - X.e14*Y.e145 + X.e2*Y.e25 - X.e23*Y.e235 - X.e234*Y.e2345 - X.e24*Y.e245 + X.e3*Y.e35 - X.e34*Y.e345 + X.e4*Y.e45 + X.scalar*Y.e5, X.e3*Y.e123 - X.e34*Y.e1234 + X.e345*Y.e12345 + X.e35*Y.e1235 + X.e4*Y.e124 + X.e45*Y.e1245 - X.e5*Y.e125 + X.scalar*Y.e12, -X.e2*Y.e123 + X.e24*Y.e1234 - X.e245*Y.e12345 - X.e25*Y.e1235 + X.e4*Y.e134 + X.e45*Y.e1345 - X.e5*Y.e135 + X.scalar*Y.e13, -X.e2*Y.e124 - X.e23*Y.e1234 + X.e235*Y.e12345 - X.e25*Y.e1245 - X.e3*Y.e134 - X.e35*Y.e1345 - X.e5*Y.e145 + X.scalar*Y.e14, -X.e2*Y.e125 - X.e23*Y.e1235 + X.e234*Y.e12345 - X.e24*Y.e1245 - X.e3*Y.e135 - X.e34*Y.e1345 - X.e4*Y.e145 + X.scalar*Y.e15, X.e1*Y.e123 - X.e14*Y.e1234 + X.e145*Y.e12345 + X.e15*Y.e1235 + X.e4*Y.e234 + X.e45*Y.e2345 - X.e5*Y.e235 + X.scalar*Y.e23, X.e1*Y.e124 + X.e13*Y.e1234 - X.e135*Y.e12345 + X.e15*Y.e1245 - X.e3*Y.e234 - X.e35*Y.e2345 - X.e5*Y.e245 + X.scalar*Y.e24, X.e1*Y.e125 + X.e13*Y.e1235 - X.e134*Y.e12345 + X.e14*Y.e1245 - X.e3*Y.e235 - X.e34*Y.e2345 - X.e4*Y.e245 + X.scalar*Y.e25, X.e1*Y.e134 - X.e12*Y.e1234 + X.e125*Y.e12345 + X.e15*Y.e1345 + X.e2*Y.e234 + X.e25*Y.e2345 - X.e5*Y.e345 + X.scalar*Y.e34, X.e1*Y.e135 - X.e12*Y.e1235 + X.e124*Y.e12345 + X.e14*Y.e1345 + X.e2*Y.e235 + X.e24*Y.e2345 - X.e4*Y.e345 + X.scalar*Y.e35, X.e1*Y.e145 - X.e12*Y.e1245 - X.e123*Y.e12345 - X.e13*Y.e1345 + X.e2*Y.e245 - X.e23*Y.e2345 + X.e3*Y.e345 + X.scalar*Y.e45, -X.e4*Y.e1234 + X.e45*Y.e12345 + X.e5*Y.e1235 + X.scalar*Y.e123, X.e3*Y.e1234 - X.e35*Y.e12345 + X.e5*Y.e1245 + X.scalar*Y.e124, X.e3*Y.e1235 - X.e34*Y.e12345 + X.e4*Y.e1245 + X.scalar*Y.e125, -X.e2*Y.e1234 + X.e25*Y.e12345 + X.e5*Y.e1345 + X.scalar*Y.e134, -X.e2*Y.e1235 + X.e24*Y.e12345 + X.e4*Y.e1345 + X.scalar*Y.e135, -X.e2*Y.e1245 - X.e23*Y.e12345 - X.e3*Y.e1345 + X.scalar*Y.e145, X.e1*Y.e1234 - X.e15*Y.e12345 + X.e5*Y.e2345 + X.scalar*Y.e234, X.e1*Y.e1235 - X.e14*Y.e12345 + X.e4*Y.e2345 + X.scalar*Y.e235, X.e1*Y.e1245 + X.e13*Y.e12345 - X.e3*Y.e2345 + X.scalar*Y.e245, X.e1*Y.e1345 - X.e12*Y.e12345 + X.e2*Y.e2345 + X.scalar*Y.e345, -X.e5*Y.e12345 + X.scalar*Y.e1234, -X.e4*Y.e12345 + X.scalar*Y.e1235, X.e3*Y.e12345 + X.scalar*Y.e1245, -X.e2*Y.e12345 + X.scalar*Y.e1345, X.e1*Y.e12345 + X.scalar*Y.e2345, X.scalar*Y.e12345);
}

CGA3 outer(CGA3 X, CGA3 Y){
    return CGA3(X.scalar*Y.scalar, X.e1*Y.scalar + X.scalar*Y.e1, X.e2*Y.scalar + X.scalar*Y.e2, X.e3*Y.scalar + X.scalar*Y.e3, X.e4*Y.scalar + X.scalar*Y.e4, X.e5*Y.scalar + X.scalar*Y.e5, X.e1*Y.e2 + X.e12*Y.scalar - X.e2*Y.e1 + X.scalar*Y.e12, X.e1*Y.e3 + X.e13*Y.scalar - X.e3*Y.e1 + X.scalar*Y.e13, X.e1*Y.e4 + X.e14*Y.scalar - X.e4*Y.e1 + X.scalar*Y.e14, X.e1*Y.e5 + X.e15*Y.scalar - X.e5*Y.e1 + X.scalar*Y.e15, X.e2*Y.e3 + X.e23*Y.scalar - X.e3*Y.e2 + X.scalar*Y.e23, X.e2*Y.e4 + X.e24*Y.scalar - X.e4*Y.e2 + X.scalar*Y.e24, X.e2*Y.e5 + X.e25*Y.scalar - X.e5*Y.e2 + X.scalar*Y.e25, X.e3*Y.e4 + X.e34*Y.scalar - X.e4*Y.e3 + X.scalar*Y.e34, X.e3*Y.e5 + X.e35*Y.scalar - X.e5*Y.e3 + X.scalar*Y.e35, X.e4*Y.e5 + X.e45*Y.scalar - X.e5*Y.e4 + X.scalar*Y.e45, X.e1*Y.e23 + X.e12*Y.e3 + X.e123*Y.scalar - X.e13*Y.e2 - X.e2*Y.e13 + X.e23*Y.e1 + X.e3*Y.e12 + X.scalar*Y.e123, X.e1*Y.e24 + X.e12*Y.e4 + X.e124*Y.scalar - X.e14*Y.e2 - X.e2*Y.e14 + X.e24*Y.e1 + X.e4*Y.e12 + X.scalar*Y.e124, X.e1*Y.e25 + X.e12*Y.e5 + X.e125*Y.scalar - X.e15*Y.e2 - X.e2*Y.e15 + X.e25*Y.e1 + X.e5*Y.e12 + X.scalar*Y.e125, X.e1*Y.e34 + X.e13*Y.e4 + X.e134*Y.scalar - X.e14*Y.e3 - X.e3*Y.e14 + X.e34*Y.e1 + X.e4*Y.e13 + X.scalar*Y.e134, X.e1*Y.e35 + X.e13*Y.e5 + X.e135*Y.scalar - X.e15*Y.e3 - X.e3*Y.e15 + X.e35*Y.e1 + X.e5*Y.e13 + X.scalar*Y.e135, X.e1*Y.e45 + X.e14*Y.e5 + X.e145*Y.scalar - X.e15*Y.e4 - X.e4*Y.e15 + X.e45*Y.e1 + X.e5*Y.e14 + X.scalar*Y.e145, X.e2*Y.e34 + X.e23*Y.e4 + X.e234*Y.scalar - X.e24*Y.e3 - X.e3*Y.e24 + X.e34*Y.e2 + X.e4*Y.e23 + X.scalar*Y.e234, X.e2*Y.e35 + X.e23*Y.e5 + X.e235*Y.scalar - X.e25*Y.e3 - X.e3*Y.e25 + X.e35*Y.e2 + X.e5*Y.e23 + X.scalar*Y.e235, X.e2*Y.e45 + X.e24*Y.e5 + X.e245*Y.scalar - X.e25*Y.e4 - X.e4*Y.e25 + X.e45*Y.e2 + X.e5*Y.e24 + X.scalar*Y.e245, X.e3*Y.e45 + X.e34*Y.e5 + X.e345*Y.scalar - X.e35*Y.e4 - X.e4*Y.e35 + X.e45*Y.e3 + X.e5*Y.e34 + X.scalar*Y.e345, X.e1*Y.e234 + X.e12*Y.e34 + X.e123*Y.e4 + X.e1234*Y.scalar - X.e124*Y.e3 - X.e13*Y.e24 + X.e134*Y.e2 + X.e14*Y.e23 - X.e2*Y.e134 + X.e23*Y.e14 - X.e234*Y.e1 - X.e24*Y.e13 + X.e3*Y.e124 + X.e34*Y.e12 - X.e4*Y.e123 + X.scalar*Y.e1234, X.e1*Y.e235 + X.e12*Y.e35 + X.e123*Y.e5 + X.e1235*Y.scalar - X.e125*Y.e3 - X.e13*Y.e25 + X.e135*Y.e2 + X.e15*Y.e23 - X.e2*Y.e135 + X.e23*Y.e15 - X.e235*Y.e1 - X.e25*Y.e13 + X.e3*Y.e125 + X.e35*Y.e12 - X.e5*Y.e123 + X.scalar*Y.e1235, X.e1*Y.e245 + X.e12*Y.e45 + X.e124*Y.e5 + X.e1245*Y.scalar - X.e125*Y.e4 - X.e14*Y.e25 + X.e145*Y.e2 + X.e15*Y.e24 - X.e2*Y.e145 + X.e24*Y.e15 - X.e245*Y.e1 - X.e25*Y.e14 + X.e4*Y.e125 + X.e45*Y.e12 - X.e5*Y.e124 + X.scalar*Y.e1245, X.e1*Y.e345 + X.e13*Y.e45 + X.e134*Y.e5 + X.e1345*Y.scalar - X.e135*Y.e4 - X.e14*Y.e35 + X.e145*Y.e3 + X.e15*Y.e34 - X.e3*Y.e145 + X.e34*Y.e15 - X.e345*Y.e1 - X.e35*Y.e14 + X.e4*Y.e135 + X.e45*Y.e13 - X.e5*Y.e134 + X.scalar*Y.e1345, X.e2*Y.e345 + X.e23*Y.e45 + X.e234*Y.e5 + X.e2345*Y.scalar - X.e235*Y.e4 - X.e24*Y.e35 + X.e245*Y.e3 + X.e25*Y.e34 - X.e3*Y.e245 + X.e34*Y.e25 - X.e345*Y.e2 - X.e35*Y.e24 + X.e4*Y.e235 + X.e45*Y.e23 - X.e5*Y.e234 + X.scalar*Y.e2345, X.e1*Y.e2345 + X.e12*Y.e345 + X.e123*Y.e45 + X.e1234*Y.e5 + X.e12345*Y.scalar - X.e1235*Y.e4 - X.e124*Y.e35 + X.e1245*Y.e3 + X.e125*Y.e34 - X.e13*Y.e245 + X.e134*Y.e25 - X.e1345*Y.e2 - X.e135*Y.e24 + X.e14*Y.e235 + X.e145*Y.e23 - X.e15*Y.e234 - X.e2*Y.e1345 + X.e23*Y.e145 - X.e234*Y.e15 + X.e2345*Y.e1 + X.e235*Y.e14 - X.e24*Y.e135 - X.e245*Y.e13 + X.e25*Y.e134 + X.e3*Y.e1245 + X.e34*Y.e125 + X.e345*Y.e12 - X.e35*Y.e124 - X.e4*Y.e1235 + X.e45*Y.e123 + X.e5*Y.e1234 + X.scalar*Y.e12345);
}

#define I_CGA3 CGA3(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0)

CGA3 rcontract(CGA3 X, CGA3 Y){
    return CGA3(X.e1*Y.e1 - X.e12*Y.e12 - X.e123*Y.e123 + X.e1234*Y.e1234 - X.e12345*Y.e12345 - X.e1235*Y.e1235 - X.e124*Y.e124 - X.e1245*Y.e1245 + X.e125*Y.e125 - X.e13*Y.e13 - X.e134*Y.e134 - X.e1345*Y.e1345 + X.e135*Y.e135 - X.e14*Y.e14 + X.e145*Y.e145 + X.e15*Y.e15 + X.e2*Y.e2 - X.e23*Y.e23 - X.e234*Y.e234 - X.e2345*Y.e2345 + X.e235*Y.e235 - X.e24*Y.e24 + X.e245*Y.e245 + X.e25*Y.e25 + X.e3*Y.e3 - X.e34*Y.e34 + X.e345*Y.e345 + X.e35*Y.e35 + X.e4*Y.e4 + X.e45*Y.e45 - X.e5*Y.e5 + X.scalar*Y.scalar, X.e1*Y.scalar + X.e12*Y.e2 - X.e123*Y.e23 - X.e1234*Y.e234 - X.e12345*Y.e2345 + X.e1235*Y.e235 - X.e124*Y.e24 + X.e1245*Y.e245 + X.e125*Y.e25 + X.e13*Y.e3 - X.e134*Y.e34 + X.e1345*Y.e345 + X.e135*Y.e35 + X.e14*Y.e4 + X.e145*Y.e45 - X.e15*Y.e5, -X.e12*Y.e1 + X.e123*Y.e13 + X.e1234*Y.e134 + X.e12345*Y.e1345 - X.e1235*Y.e135 + X.e124*Y.e14 - X.e1245*Y.e145 - X.e125*Y.e15 + X.e2*Y.scalar + X.e23*Y.e3 - X.e234*Y.e34 + X.e2345*Y.e345 + X.e235*Y.e35 + X.e24*Y.e4 + X.e245*Y.e45 - X.e25*Y.e5, -X.e123*Y.e12 - X.e1234*Y.e124 - X.e12345*Y.e1245 + X.e1235*Y.e125 - X.e13*Y.e1 + X.e134*Y.e14 - X.e1345*Y.e145 - X.e135*Y.e15 - X.e23*Y.e2 + X.e234*Y.e24 - X.e2345*Y.e245 - X.e235*Y.e25 + X.e3*Y.scalar + X.e34*Y.e4 + X.e345*Y.e45 - X.e35*Y.e5, X.e1234*Y.e123 + X.e12345*Y.e1235 - X.e124*Y.e12 + X.e1245*Y.e125 - X.e134*Y.e13 + X.e1345*Y.e135 - X.e14*Y.e1 - X.e145*Y.e15 - X.e234*Y.e23 + X.e2345*Y.e235 - X.e24*Y.e2 - X.e245*Y.e25 - X.e34*Y.e3 - X.e345*Y.e35 + X.e4*Y.scalar - X.e45*Y.e5, X.e12345*Y.e1234 + X.e1235*Y.e123 + X.e1245*Y.e124 - X.e125*Y.e12 + X.e1345*Y.e134 - X.e135*Y.e13 - X.e145*Y.e14 - X.e15*Y.e1 + X.e2345*Y.e234 - X.e235*Y.e23 - X.e245*Y.e24 - X.e25*Y.e2 - X.e345*Y.e34 - X.e35*Y.e3 - X.e45*Y.e4 + X.e5*Y.scalar, X.e12*Y.scalar + X.e123*Y.e3 - X.e1234*Y.e34 + X.e12345*Y.e345 + X.e1235*Y.e35 + X.e124*Y.e4 + X.e1245*Y.e45 - X.e125*Y.e5, -X.e123*Y.e2 + X.e1234*Y.e24 - X.e12345*Y.e245 - X.e1235*Y.e25 + X.e13*Y.scalar + X.e134*Y.e4 + X.e1345*Y.e45 - X.e135*Y.e5, -X.e1234*Y.e23 + X.e12345*Y.e235 - X.e124*Y.e2 - X.e1245*Y.e25 - X.e134*Y.e3 - X.e1345*Y.e35 + X.e14*Y.scalar - X.e145*Y.e5, X.e12345*Y.e234 - X.e1235*Y.e23 - X.e1245*Y.e24 - X.e125*Y.e2 - X.e1345*Y.e34 - X.e135*Y.e3 - X.e145*Y.e4 + X.e15*Y.scalar, X.e123*Y.e1 - X.e1234*Y.e14 + X.e12345*Y.e145 + X.e1235*Y.e15 + X.e23*Y.scalar + X.e234*Y.e4 + X.e2345*Y.e45 - X.e235*Y.e5, X.e1234*Y.e13 - X.e12345*Y.e135 + X.e124*Y.e1 + X.e1245*Y.e15 - X.e234*Y.e3 - X.e2345*Y.e35 + X.e24*Y.scalar - X.e245*Y.e5, -X.e12345*Y.e134 + X.e1235*Y.e13 + X.e1245*Y.e14 + X.e125*Y.e1 - X.e2345*Y.e34 - X.e235*Y.e3 - X.e245*Y.e4 + X.e25*Y.scalar, -X.e1234*Y.e12 + X.e12345*Y.e125 + X.e134*Y.e1 + X.e1345*Y.e15 + X.e234*Y.e2 + X.e2345*Y.e25 + X.e34*Y.scalar - X.e345*Y.e5, X.e12345*Y.e124 - X.e1235*Y.e12 + X.e1345*Y.e14 + X.e135*Y.e1 + X.e2345*Y.e24 + X.e235*Y.e2 - X.e345*Y.e4 + X.e35*Y.scalar, -X.e12345*Y.e123 - X.e1245*Y.e12 - X.e1345*Y.e13 + X.e145*Y.e1 - X.e2345*Y.e23 + X.e245*Y.e2 + X.e345*Y.e3 + X.e45*Y.scalar, X.e123*Y.scalar + X.e1234*Y.e4 + X.e12345*Y.e45 - X.e1235*Y.e5, -X.e1234*Y.e3 - X.e12345*Y.e35 + X.e124*Y.scalar - X.e1245*Y.e5, -X.e12345*Y.e34 - X.e1235*Y.e3 - X.e1245*Y.e4 + X.e125*Y.scalar, X.e1234*Y.e2 + X.e12345*Y.e25 + X.e134*Y.scalar - X.e1345*Y.e5, X.e12345*Y.e24 + X.e1235*Y.e2 - X.e1345*Y.e4 + X.e135*Y.scalar, -X.e12345*Y.e23 + X.e1245*Y.e2 + X.e1345*Y.e3 + X.e145*Y.scalar, -X.e1234*Y.e1 - X.e12345*Y.e15 + X.e234*Y.scalar - X.e2345*Y.e5, -X.e12345*Y.e14 - X.e1235*Y.e1 - X.e2345*Y.e4 + X.e235*Y.scalar, X.e12345*Y.e13 - X.e1245*Y.e1 + X.e2345*Y.e3 + X.e245*Y.scalar, -X.e12345*Y.e12 - X.e1345*Y.e1 - X.e2345*Y.e2 + X.e345*Y.scalar, X.e1234*Y.scalar - X.e12345*Y.e5, -X.e12345*Y.e4 + X.e1235*Y.scalar, X.e12345*Y.e3 + X.e1245*Y.scalar, -X.e12345*Y.e2 + X.e1345*Y.scalar, X.e12345*Y.e1 + X.e2345*Y.scalar, X.e12345*Y.scalar);
}

CGA3 reverse(CGA3 X){
    return CGA3(X.scalar, X.e1, X.e2, X.e3, X.e4, X.e5, -X.e12, -X.e13, -X.e14, -X.e15, -X.e23, -X.e24, -X.e25, -X.e34, -X.e35, -X.e45, -X.e123, -X.e124, -X.e125, -X.e134, -X.e135, -X.e145, -X.e234, -X.e235, -X.e245, -X.e345, X.e1234, X.e1235, X.e1245, X.e1345, X.e2345, X.e12345);
}



CGA3 conjugate(CGA3 X){
    return reverse(involve(X));
}

CGA3 outer(CGA3 X, CGA3 Y, CGA3 Z){
    return outer(outer(X, Y), Z);
}

CGA3 invert(CGA3 X){
    return mul(1.0/lcontract(X,conjugate(X)).scalar, conjugate(X));
}

CGA3 div(CGA3 X, CGA3 Y){
    return mul(X, invert(Y));
}

CGA3 dual(CGA3 X){
    return div(X, I_CGA3);
}
