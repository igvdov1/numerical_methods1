

def runge_rule(method, func: list, start, end, start_value: list, eps):
    a = []
    h = 12000
    i = 0
    k = method(func, start, end, start_value, h)
    a.append([*k[len(k) - 1], 10])
    h *= 2
    k = method(func, start, end, start_value, h)
    print(a)
    a.append([*k[len(k) - 1], max([abs(k[len(k)- 1][j] - a[i][j]) for j in range(len(func))])])
    print(len(func))
    i += 1
    print([k[len(k)- 1][j] for j in range(len(func))])

    while  a[i][len(func)] > eps:
        k = method(func, start, end, start_value, h)
        a.append([*k[len(k) - 1], max([abs(k[len(k)- 1][j] - a[i][j]) for j in range(len(func))])])
        i += 1
        h*= 2
    return a
