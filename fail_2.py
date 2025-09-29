import math
from fail_1 import safe_nan

@safe_nan
def func_cube(x):
    return x ** 3

@safe_nan
def func_square(x):
    return x ** 2

@safe_nan
def func_circle_area(r):
    return math.pi * r ** 2

@safe_nan
def func_sin(x):
    return math.sin(x)

@safe_nan
def func_cos(x):
    return math.cos(x)

@safe_nan
def func_abs(x):
    return abs(x)

if __name__ == "__main__":
    print("func_cube(3) =", func_cube(3))
    print("func_square(4) =", func_square(4))
    print("func_circle_area(3) =", func_circle_area(3))
    print("func_sin(pi/2) =", func_sin(math.pi/2))
    print("func_cos(0) =", func_cos(0))
    print("func_abs(-7) =", func_abs(-7))