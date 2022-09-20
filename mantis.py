#Bisection method
from math import exp
from method_of_half_divide import method_of_half_divide

def func(v, g, m, t, c2, c1):
    c3 = (c2 + c1) / 2
    return v - g * m / c3 * (1 - exp(-1 * (c3 / m) * t))


# def method_of_half_divide(func, v, g, m, t, c2, c1, exp):
#     c3 = (c2 + c1) / 2
#     k = func(v,g,m,t,c2,c1)
#     while abs(k) > eps:
#         if k > 0:
#             c2 = c3
#             c3 = (c2 + c1) / 2
#         else:
#             c1 = c3
#             c3 = (c2 + c1) / 2
#         k = func(v, g, m, t, c2, c1)
#     return c1, c2, k

if __name__ == '__main__':
    c1 = 1
    c2 = 100
    c3 = (c2 + c1) / 2
    v = 40
    g = 9.8
    m = 68.1
    t = 10
    k = func(v, g, m, t, c2, c1)
    eps = 0.01

    print(method_of_half_divide(func, c2, c1, eps, v, g, m, t))

