
def method_of_half_divide(func, c2, c1, eps, *args):
    c3 = (c2 + c1) / 2
    k = func(*args, c2, c1)
    while abs(k) > eps:
        if k >= 0:
            c2 = c3
            c3 = (c2 + c1) / 2
        else:
            c1 = c3
            c3 = (c2 + c1) / 2
        k = func(*args, c2, c1)
    return c1, c2, k


