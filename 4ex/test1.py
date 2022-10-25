from recM import rectangleMethod
from math import cos
from trapeseM import trapeseMethod
from sympsonM import sympsonMethod
from tabulate import tabulate
from differential import derivative
import pandas as pd
from oldRecM import rectangleMethod1
from matplotlib import pyplot as plt
def f(x):
    return cos(x)/(x+2)
def f2(x):
    return x**2
def f3(x):
    return x**3/cos(x)
if __name__ == '__main__':
    
    # x1 = 0.4
    # x2 = 1.2
    dx =  1e-8
    # head = ['N', 'eps', 'p', 'integral']
    head = ['f', 'eps']
    data = derivative(f2, 1, dx, 2)
    print(tabulate(data, headers = head, tablefmt='grid'))
    c = []
    for i in range(1, 27):
        c.append(data[i][1])
    plt.plot(c)
    plt.show()
    # data1 = sympsonMethod(x1, x2, dx, f3)
     
    # print(tabulate(data1, headers=head, tablefmt="grid"))
    # data2 = trapeseMethod(x1, x2, dx, f)
     
    # print(tabulate(data2, headers=head, tablefmt='grid'))
 
    # data = rectangleMethod(x1, x2, dx, f)

    # print(tabulate(data, headers=head, tablefmt = 'grid'))

    