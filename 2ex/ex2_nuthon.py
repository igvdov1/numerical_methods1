from differential import derivative

from matplotlib import pyplot as plt
def f2(x):
    return x**10 - 1
# def exact_nuton(x0, dx, f, eps, kol_op_in_f):
#     x2 = x0+1
#     count = 0
#     countop = 0
#     x = []
#     y = []
#     while (abs(x0 - x2) > eps):
#         x1 = x0 - 2*f2(x0)/derivative(f2, x0, dx)
#         x2 = x0
#         x0 = x1
#         count+= 1
#         countop += kol_op_in_f * 3 + 5
#         x.append(x2)
#         y.append(f(x2))
#     plt.plot(x, y)
#     plt.scatter(x, y)
#     for i in range(len(x)):
#         plt.annotate((x[i], y[i]), (x[i], y[i]))
#     plt.show()
#     return x2, count, countop
def exact_nuton(x0, dx, f, eps, kol_op_in_f, krat_root):
    x2 = x0+1
    count = 0
    countop = 0
    x = []
    y = []
    while (abs(x0 - x2) > eps):

        x1 = x0 - krat_root*f(x0) / derivative(f, x0, dx)
        x2 = x0
        x0 = x1
        count += 1
        countop += kol_op_in_f * 3 + 4
        x.append(x2)
        y.append(f(x2))
    plt.plot(x,y)
    plt.scatter(x,y)
    for i in range(len(x)):
        plt.annotate((x[i], y[i]), (x[i], y[i]))
    plt.show()
    return x2, count, countop
if __name__ == '__main__':
    dx = 1e-8
    x0 = 0.5
    eps = 0.0001
    x2 = x0 + 1

    print(exact_nuton(x0, dx, f2, eps, 2, 10))