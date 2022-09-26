
from Stefanson_method import Stefanson
from nuton_method import nuton_method
from secant_method import secant_method
from ex2_nuthon import exact_nuton
from math import exp
def f(x):
    return 4*(1 - x**2)-exp(x)
def f2(x):
    return pow(x, 2)*exp(x)
if __name__ == '__main__':
    x0 = 0
    x1 = 1
    dx = 1e-8
    eps = 0.00000000001
    print("Тут 1ое уравнение и идет сравненме:")
    print("Ньютон:", nuton_method(x0, dx, f, eps, 5))
    print("Секущие:", secant_method(x0,x1, eps, f, 5))
    print("Стефансон:", Stefanson(x0, x1, eps, f, 5))
    print("\n \n Тут 2 уравнение:")
    print("Ньютон:", nuton_method(x1, dx, f2, eps, 3))
    print("Точный Ньютон:", exact_nuton(x1, dx, f2, eps, 3, 2))