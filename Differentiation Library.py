from sympy import *
x = Symbol('x')

f = cos(x)
print(diff(f, x))