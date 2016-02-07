import pytest
from alglbraic import *
from sympy import symbols

A = symbols('a b c d')
B = symbols('x y z w')
a,b,c,d = A
x,y,z,w = B

printer = GLSLPrinter({"use_operators":True})

expr = [a*b,b*x*y,z*w,a-b+c-d*z**2]
# product = printer.formatBinaryOperation(A,B,expr)
u = VectorOperation("funktion",[A],a*b*c)
v = VectorOperation("product",[A,B],expr)

print u.lower()
print v.gl(printer)

print (u+v).gl(printer)
