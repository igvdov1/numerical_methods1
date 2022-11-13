from RungeKutteM import RungeKutteMethod
from math import exp
import math
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
def some_tests(x, y): 
    return x ** 2 - 2 * y
def f(x, y): 
    return 2 * x - 5 * y + 3
def f1(x, y):
    return 5 * x - 6 * y + 1
def answerx(t):
      return 5 * exp(-2 * t) * math.cos(3 * t) + 1
def answery(t):
    return exp(-2 * t) * (4 * math.cos(3 * t) + 3 * math.sin(3 * t)) + 1
if __name__ == '__main__':
    start = 1
    eps = 1
    print(pd.DataFrame(RungeKutteMethod(some_tests, 0, 1, 1, eps, answerx)))
    c = []
    b = []
    k = RungeKutteMethod(f, 0, 6, 1, eps, answerx)
    a = np.linspace(0, 1, len(k))
    print(answerx(0))
    for i in range (len(k)):
        b.append(answerx(a[i]))
        c.append(k[i][1])
    
        
        
    plt.plot(a, c, color = 'black')
    plt.plot(a, b, color = 'blue')
    plt.scatter(a, c, color = 'green')
    plt.scatter(a, b, color = 'red')
    plt.show()
    
