# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestFiniteModule::test_finite_module 1'] = '''struct ComplexCl2 {
    C ONE; C e1; C e2; C e12;
}'''

snapshots['TestFiniteModule::test_finite_module 2'] = '''ComplexCl2 zero(){
    return ComplexCl2(zero_base(), zero_base(), zero_base(), zero_base());
}'''

snapshots['TestFiniteModule::test_finite_module 3'] = '''ComplexCl2 one(){
    return ComplexCl2(one_base(), zero_base(), zero_base(), zero_base());
}'''

snapshots['TestFiniteModule::test_algebraic_product 1'] = '''ComplexCl2 mul(ComplexCl2 u, ComplexCl2 v){
    return ComplexCl2(u.ONE*v.ONE + u.e1*v.e1 - u.e12*v.e12 + u.e2*v.e2, u.ONE*v.e1 + u.e1*v.ONE + u.e12*v.e2 - u.e2*v.e12, u.ONE*v.e2 + u.e1*v.e12 - u.e12*v.e1 + u.e2*v.ONE, u.ONE*v.e12 + u.e1*v.e2 + u.e12*v.ONE - u.e2*v.e1);
}'''

snapshots['TestFiniteModule::test_finite_module 4'] = '''ComplexCl2 add(ComplexCl2 u, ComplexCl2 v){
    return ComplexCl2(add(u.ONE, v.ONE), add(u.e1, v.e1), add(u.e2, v.e2), add(u.e12, v.e12));
}'''

snapshots['TestFiniteModule::test_finite_module 5'] = '''ComplexCl2 sub(ComplexCl2 u, ComplexCl2 v){
    return ComplexCl2(sub(u.ONE, v.ONE), sub(u.e1, v.e1), sub(u.e2, v.e2), sub(u.e12, v.e12));
}'''

snapshots['TestFiniteModule::test_finite_module 6'] = '''ComplexCl2 mul(C a, ComplexCl2 x){
    return ComplexCl2(mul(a, x.ONE), mul(a, x.e1), mul(a, x.e2), mul(a, x.e12));
}'''
