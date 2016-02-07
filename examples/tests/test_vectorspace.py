import pytest
from alglbraic import *
from sympy import symbols

printer = GLSLPrinter()
A = symbols('a b c d')
B = symbols('x y z w')
a,b,c,d = A
x,y,z,w = B

expr = [a*b,b*x*y,z*w,a-b+c-d*z**2]
product = printer.formatBinaryOperation(A,B,expr)
v = VectorSpace(len(expr),product)

print v.lower()
