from math import exp
from differential import derivative
def f(x):
    return exp(-x)-x
def f2(x):
    return x**10 - 1
def nuton_method(x0, x2, dx, f, eps):
    while (abs(x0 - x2) > eps):
        x1 = x0 - f(x0) / derivative(f, x0, dx)
        x2 = x0
        x0 = x1
    return x2, x0
if __name__ == "__main__":

    dx = 1e-8
    x0 = 0
    eps = 0.01
    x2 = x0 + 1

    print(nuton_method(x0, x2,dx,f,eps))