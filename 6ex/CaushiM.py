import numpy as np
def eilerMethod(f, g, start, fstart, gstart, x2, eps, orig, orig2):
    h = 2

    while True:
        a = []
        k = np.linspace(start, x2, h)
        h1 = (x2-start)/(h)
        
        a.append([start, fstart, gstart, f(start, fstart, gstart), g(start, fstart, gstart), h])
    
        for i in range(1, h):
            x = a[i-1][1] + h1 * f(a[i-1][0], a[i-1][1], a[i-1][2])
            y = a[i-1][2] + h1 * g(a[i-1][0], a[i-1][1],a[i-1][2])
            a.append([k[i], x, y, f(k[i], x, y), g(k[i], x, y), h])
        
        if abs(a[h-1][1] - orig(k[h-1])) < eps and abs(a[h-1][2] - orig2(k[h-1])) < eps:
      
            break

        h *= 2

    return a