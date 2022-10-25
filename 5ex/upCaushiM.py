import numpy as np
def upEilerMethod(f, start, fstart, x2, eps, orig):
    h = 2
    while True:
        a = []
        k = np.linspace(start, x2, h)
        h1 = (x2-start)/(h)
    
        a.append([start, fstart, f(start, fstart)])
        flag = 0 
        for i in range(1, h):
            xi = a[i-1][0]
            yi = a[i-1][1]
         
            dy = h1*f(xi+h1/2, yi + h1/2*f(xi, yi))
            y = yi + dy

            a.append([k[i], y, f(xi + h1/2 , y)])
        print(abs(a[h-1][1] - orig(k[h-1])))
        if abs(a[h-1][1] - orig(k[h-1])) < eps:
            print('notsth')
            break
        h *= 2

    return a