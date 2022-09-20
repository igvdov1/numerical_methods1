
def Stefanson(x1, eps, f):
    while ((f(x1 + f(x1)) - f(x1)) > eps):
        x2 = x1 - f(x1) / (f(x1 + f(x1)) - f(x1)) * f(x1)
        x1 = x2
    return x1, x2
