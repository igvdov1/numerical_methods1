from math import exp
def secant_method(x0, x1, eps, f):
    while (abs(x0-x1) > eps):

        x2 = x1 - (x1 - x0)/(f(x1)-f(x0))*f(x1)
        x0 = x1
        x1 = x2
    return x1, x2
def f(x):
    return exp(-x)-x

if __name__ == '__main__':
    x0 = 0
    x1 = 1+x0
    x2 = 10000+x1
    eps = 0.01

    print(secant_method(x0, x1, eps, f))