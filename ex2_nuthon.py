from differential import derivative
from nuton_method import nuton_method
def f2(x):
    return x**10 - 1
def exact_nuton(x0, x2, dx, f, eps):
    while (abs(x0 - x2) > eps):
        x1 = x0 - 9*f2(x0) / derivative(f2, x0, dx)
        x2 = x0
        x0 = x1
    return x2, x0
if __name__ == '__main__':
    dx = 1e-8
    x0 = 0.5
    eps = 0.01
    x2 = x0 + 1
    print(nuton_method(x0, x2, dx, f2, eps))
    print(new_nuton(x0, x2, dx, f2, eps))