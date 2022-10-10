from interpolationLagr import interpolationLagr
from matplotlib import pyplot as plt
import math
from tabulate import tabulate
import numpy as np
from Chebishev import Chebyshev
def proverka_polinoma(x):
    return x**5 + 2
def f(x):
    return 1 / (1 + 25 * x ** 2)


def newX(kol):
    mas = []
    for i in range(kol + 1):
        mas.append(2 * i / kol - 1)
    return mas



if __name__ == '__main__':
    a = newX(5)
    a3 = Chebyshev(5)
    a2 = Chebyshev(20)
    a1 = newX(20)
    newa = np.linspace(-1, 1, 1000)
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    for i in range(len(a2)):
        data1.append(f(a2[i]))
        data2.append(interpolationLagr(a2[i], a2, f))
    for i in range(len(a3)):
        data3.append(f(a3[i]))
        data4.append(interpolationLagr(a3[i], a3, f))
    x = []
    y = []
    y1 = []
    y2 = []
    data = []
    for i in range(len(newa)):
        y.append(interpolationLagr(newa[i], a2, f))
        y1.append(f(newa[i]))
        y2.append(interpolationLagr(newa[i], a3, f))
        data.append([newa[i], interpolationLagr(newa[i], a3, f), f(newa[i]), interpolationLagr(newa[i], a2, f)])
    plt.plot(newa, y, color='black')
    plt.plot(newa, y1, color='red')
    plt.plot(newa, y2, color='blue')
    plt.scatter(a2, data1, color='black')
    plt.scatter(a2, data2, color = 'red')
    plt.scatter(a3, data3, color = 'red')
    plt.scatter(a3, data4, color = 'blue')
    head = ['x', 'P20', 'orig f', 'P5']
    print(tabulate(data, headers=head, tablefmt="grid"))

    plt.show()

