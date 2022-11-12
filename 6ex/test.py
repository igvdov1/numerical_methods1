from RungeKutteM import RungeKutteMethod
from math import exp
def f(x, y): 
    return x**2 - 2 * y
def answer(x, y):
      return 3/4*exp(-2*x) + 1/2 * (x**2) - 1/2 * x+ 1/4
if __name__ == '__main__':
    start = 1
    eps = 1
    print(RungeKutteMethod(f, 0, 1, 1, eps, answer))
