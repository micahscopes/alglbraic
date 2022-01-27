# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestFiniteModule::test_algebraic_product 1'] = '''ComplexCl2 mul(ComplexCl2 X, ComplexCl2 Y){
    return ComplexCl2(X.ONE*Y.ONE + X.e1*Y.e1 - X.e12*Y.e12 + X.e2*Y.e2, X.ONE*Y.e1 + X.e1*Y.ONE + X.e12*Y.e2 - X.e2*Y.e12, X.ONE*Y.e2 + X.e1*Y.e12 - X.e12*Y.e1 + X.e2*Y.ONE, X.ONE*Y.e12 + X.e1*Y.e2 + X.e12*Y.ONE - X.e2*Y.e1);
}'''

snapshots['TestFiniteModule::test_finite_module 1'] = '''const int I_ComplexCl2_ONE = 0;
const int I_ComplexCl2_e1 = 1;
const int I_ComplexCl2_e2 = 2;
const int I_ComplexCl2_e12 = 3;

struct ComplexCl2 {
    C ONE;
    C e1;
    C e2;
    C e12;
};'''

snapshots['TestFiniteModule::test_finite_module 2'] = '''ComplexCl2 zero(){
    return ComplexCl2(zero(), zero(), zero(), zero());
}'''

snapshots['TestFiniteModule::test_finite_module 3'] = '''ComplexCl2 one(){
    return ComplexCl2(one(), zero(), zero(), zero());
}'''

snapshots['TestFiniteModule::test_finite_module 4'] = '''ComplexCl2 add(ComplexCl2 X, ComplexCl2 Y){
    return ComplexCl2(add(X.ONE, Y.ONE), add(X.e1, Y.e1), add(X.e2, Y.e2), add(X.e12, Y.e12));
}'''

snapshots['TestFiniteModule::test_finite_module 5'] = '''ComplexCl2 sub(ComplexCl2 X, ComplexCl2 Y){
    return ComplexCl2(sub(X.ONE, Y.ONE), sub(X.e1, Y.e1), sub(X.e2, Y.e2), sub(X.e12, Y.e12));
}'''

snapshots['TestFiniteModule::test_finite_module 6'] = '''ComplexCl2 mul(C a, ComplexCl2 X){
    return ComplexCl2(mul(X.ONE, a), mul(X.e1, a), mul(X.e2, a), mul(X.e12, a));
}'''

snapshots['TestFiniteModule::test_finite_module 7'] = '''ComplexCl2 mul(int a, ComplexCl2 X){
    return mul(float(a), X);
}'''

snapshots['TestFiniteModule::test_finite_module 8'] = '''ComplexCl2 mul(float a, ComplexCl2 x){
    return mul(mul(a, one()), x);
}'''
