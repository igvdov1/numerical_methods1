#Bisection method
from math import exp
from method_of_half_divide import method_of_half_divide

def func(v, g, m, t, c2, c1):
    c3 = (c2 + c1) / 2
    return v - g * m / c3 * (1 - exp(-1 * (c3 / m) * t))



if __name__ == '__main__':
    a = 1
    b = 100
    c3 = (b + a) / 2
    v = 40
    g = 9.8
    m = 68.1
    t = 10
    k = func(v, g, m, t, b, a)
    eps = 0.00000001

    print(method_of_half_divide(func, b, a, eps, v, g, m, t))

