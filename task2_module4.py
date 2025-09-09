
from math import sqrt
from math import sin
from math import log
val =input("enter a number ")
try:
    a=float(val)
    print(f" square root of {val} is {sqrt(a)}")
    print(f" Sine of {val} is {sin(a)}")
    print(f" log base e of {val} is {log(a)}")
except Exception as e:
    print(e)

