from matplotlib import pyplot as plt
def Stefanson(x1, x2, eps, f, kol_op_in_f):
    count = 0
    countop = 0
    x = []
    y = []
    while (abs(f(x1 + f(x1)) - f(x1)) > eps):
        x2 = x1 - f(x1) / (f(x1 + f(x1)) - f(x1)) * f(x1)
        x1 = x2
        count += 1
        countop += 5 + kol_op_in_f
        x.append(x2)
        y.append(f(x2))
    plt.plot(x, y)
    plt.scatter(x, y)
    for i in range(len(x)):
        plt.annotate((x[i], y[i]), (x[i], y[i]))

    plt.show()
    return (x1+ x2)/2, count, countop
