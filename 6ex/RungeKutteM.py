import numpy as np
def RungeKutteMethod(f, start, fstart, x2, eps, orig):
    h = 11
    k = f(start, fstart)
    a = []
    mas = np.linspace(start, x2, h)
    h1 = (x2-start)/(h-1)
    k1 = f(start, fstart)
    k2 = f(start+h1/2, fstart + h1/2*k1)
    k3 = f(start + h1/2, fstart + h1/2*k2)
    k4 = f(start + h1, fstart + h1 * k3)
    dy = h1/6*(k1 + 2 * k2 + 2 * k3 + k4)
    y1 = fstart + dy
    ans = []
    ans.append(start, fstart, y1, k1, k2, k3, k4)
    
        
    print(start+h1/2, fstart + h1/2*k1)
    return k1, k2, k3, k4