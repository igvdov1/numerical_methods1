import numpy as np


def RungeKutteMethod(f, start, fstart, x2, eps, orig):
    h = 200
    
    k = f(start, fstart)
    mas = np.linspace(start, x2, h)
    h1 = (x2-start)/(h-1)
    k1 = f(start, fstart)
    k2 = f(start+h1/2, fstart + h1/2*k1)
    k3 = f(start + h1/2, fstart + h1/2*k2)
    k4 = f(start + h1, fstart + h1 * k3)
    dy = h1/6*(k1 + 2 * k2 + 2 * k3 + k4)
    y1 = fstart + dy
    ans = []
    ans.append([start, fstart, k1, k2, k3, k4, y1])
    for i in range(1, 200):
        k1 = f(mas[i], ans[i-1][6])
        k2 = f(mas[i] + h1/2, ans[i-1][6] + h1/2 * k1)
        k3 = f(mas[i] + h1/2, ans[i-1][6] + h1/2 * k2)
        k4 = f(mas[i] + h1, ans[i-1][6] + h1 * k3)
        dy = h1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        y1 = ans[i-1][6] + dy
        
        ans.append([mas[i], ans[i-1][6], k1, k2, k3, k4, y1])
    
    return ans