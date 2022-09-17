
from math import exp
from differential import derivative
def f(x):
    return exp(-x)-x
def f2(x):
    return x**10 - 1
if __name__ == "__main__":

    dx = 1e-8
    x0 = 0
    eps = 0.01
    x1 = x0 - f(x0)/derivative(f,x0,dx)
    x2 = x1 - f(x1)/derivative(f,x1, dx)
    print(x1, f(x1), f(x0), derivative(f, x0, dx))