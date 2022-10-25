from email import header
from math import exp
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from CaushiM import eilerMethod
from upCaushiM import upEilerMethod
from tabulate import tabulate
def f(x, y):
    return x**2 - 2 * y


def answer(x):
    return 3/4*exp(-2*x) + 1/2 * (x**2) - 1/2 * x+ 1/4
    
if __name__ == '__main__':
    
    b = []
    eps = 1
    d = []
    head = ['N', 'eps', 'y', 'yi/y(i-1)']
    while eps > 0.000001:
        k = upEilerMethod(f, 0, 1, 1, eps, answer)
        eps /= 10
        d.append([len(k), eps, k[len(k)-1][1], k[len(k)-1][1]/answer(1)])

    print(tabulate(d, headers = head, tablefmt = 'grid'))
    # k = eilerMethod(f, 0, 1, 1, 0.000001, answer)
    # print(pd.DataFrame(k, columns= ['xi', 'yi','f(xi, yi)']))

    # c = []
    # a = np.linspace(0, 1, len(k))
    # for i in range (len(k)):
    #     b.append(answer(a[i]))
    #     c.append(k[i][1])
    
        
        
    # plt.plot(a, c, color = 'black')
    # plt.plot(a, b, color = 'blue')
    # plt.scatter(a, c, color = 'green')
    # plt.scatter(a, b, color = 'red')
    # plt.show()
    
    # print(pd.DataFrame(k))
    