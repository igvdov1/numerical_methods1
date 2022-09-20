from Stefanson_method import Stefanson
from nuton_method import nuton_method
from secant_method import secant_method
from ex2_nuthon import exact_nuton
from math import exp
def f(x):
    return 4*(1 - x^2)-exp(x)

if __name__ == '__main__':
    x0 = 0
    x1 = 1
    dx = 1e-8
    eps = 0.01
    print(nuton_method(x0,x1, dx, f, eps))
    print(secant_method(x0,x1, eps, f))
    print()