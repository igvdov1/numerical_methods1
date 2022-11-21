
from RungeKutteM import RungeKutteMethod
from math import exp
import math
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from CaushiM import eilerMethod
from tabulate import tabulate
def xfunc(t, x, y): 
    return 2 * x - 5 * y + 3
def yfunc(t, x, y):
    return 5 * x - 6 * y + 1
def answerx(t):
      return 5 * exp(-2 * t) * math.cos(3 * t) + 1
def answery(t):
    return exp(-2 * t) * (4 * math.cos(3 * t) + 3 * math.sin(3 * t)) + 1
if __name__ == '__main__':
    start = 1
    eps = 1e-14
    xstart = 6
    ystart = 5
    d = []
    head = ['N', 'eps', 'y', 'yi/y(i-1)']
    # while eps >= 1e-12:
    #     k = RungeKutteMethod(xfunc, yfunc, 0, xstart, ystart, 10, eps, answerx, answery)['ans']
    #     eps /= 10
    #     d.append([len(k), eps, k[len(k)-1][1], k[len(k)-1][1]/answerx(10)])
    # print(tabulate(d, headers = head, tablefmt = 'grid'))
    k = RungeKutteMethod(xfunc, yfunc, 0, xstart, ystart, 1, eps, answerx, answery)['ans']
    print(pd.DataFrame(k))
    b = RungeKutteMethod(xfunc, yfunc, 0, xstart, ystart, 1, eps, answerx, answery)['a']
    print(pd.DataFrame(b))
    a = np.linspace(0, 1, k[len(k) - 1][2])
    

    my = []
    my1 = []
    orig = []
    orig1 = []
    for i in range(len(k)): 
        my.append(k[i][1])
        my1.append(k[i][0])
        orig.append(answery(a[i]))
        orig1.append(answerx(a[i]))
    plt.plot(a,orig1 , color = 'blue')
    plt.plot(a, orig, color = "red")
    plt.plot(a, my, color = 'orange')
    plt.plot(a, my1, color = 'green')
    plt.scatter(a,my, color = "green")
    plt.scatter(a, my1, color = 'black')
    plt.show()
    
 