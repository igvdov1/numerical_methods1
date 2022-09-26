from math import exp
from matplotlib import pyplot as plt
def secant_method(x0, x1, eps, f, kol_op_in_f):
    count = 0
    countop = 0
    x = []
    y = []
    while (abs(x0-x1) > eps):

        x2 = x1 - (x1 - x0)/(f(x1)-f(x0))*f(x1)
        x0 = x1
        x1 = x2
        countop += 5 + kol_op_in_f*3
        count += 1
        x.append(x2)
        y.append(f(x2))
    plt.plot(x, y)
    plt.scatter(x, y)
    for i in range(len(x)):
        plt.annotate((x[i], y[i]), (x[i], y[i]))

    plt.show()
    return (x1+x2)/2, count, countop
def f(x):
    return exp(-x)-x

if __name__ == '__main__':
    x0 = 0
    x1 = 1+x0
    x2 = 10000+x1
    eps = 0.01

    print(secant_method(x0, x1, eps, f))