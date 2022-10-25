import numpy as np
def eilerMethod(f, start, fstart, x2, eps, orig):
    h = 2

    while True:
        a = []
        k = np.linspace(start, x2, h)
        h1 = (x2-start)/(h)

        a.append([start, fstart, f(start, fstart)])
    
        for i in range(1, h):
            y = a[i-1][1] + h1 * f(a[i-1][0], a[i-1][1])
            a.append([k[i], y, f(k[i], y)])
        
        if abs(a[h-1][1] - orig(k[h-1])) < eps:
      
            break

        h *= 2

    return a