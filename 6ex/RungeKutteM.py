import numpy as np
import math
# def Runge_for_h(f, start, fstart, x2, h):
#     k = f(start, fstart)
#     mas = np.linspace(start, x2, h)
#     h1 = (x2-start)/(h-1)
#     k1 = f(start, fstart)
#     k2 = f(start+h1/2, fstart + h1/2*k1)
#     k3 = f(start + h1/2, fstart + h1/2*k2)
#     k4 = f(start + h1, fstart + h1 * k3)
#     dy = h1/6*(k1 + 2 * k2 + 2 * k3 + k4)
#     y1 = fstart + dy
#     ans = []
#     ans.append([start, fstart, k1, k2, k3, k4, y1])
#     for i in range(1, h):
#         k1 = f(mas[i], ans[i-1][6])
#         k2 = f(mas[i] + h1/2, ans[i-1][6] + h1/2 * k1)
#         k3 = f(mas[i] + h1/2, ans[i-1][6] + h1/2 * k2)
#         k4 = f(mas[i] + h1, ans[i-1][6] + h1 * k3)
#         dy = h1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
#         y1 = ans[i-1][6] + dy
        
#         ans.append([mas[i], ans[i-1][6], k1, k2, k3, k4, y1])
    
#     return ans
def Runge_Kutte_for_4(f,g , start, xstart, ystart, mas, h1):
    ans = []
    ans.append([xstart, ystart])
    for i in range(1, 4):
        k1 = f(mas[i], ans[i - 1][0], ans[i - 1][1]) 
        m1 = g(mas[i], ans[i - 1][0], ans[i - 1][1]) 
        k2 = f(mas[i] + h1 / 2, ans[i - 1][0] + h1 *k1 / 2, ans[i -1 ][1] + h1 * m1 / 2) 
        m2 = g(mas[i] + h1 / 2, ans[i - 1][0] + h1 *k1 / 2, ans[i - 1][1] + h1 * m1 / 2) 
        k3 = f(mas[i] + h1 / 2, ans[i - 1][0] + h1 * k2 / 2, ans[i - 1][1] + h1 * m2 / 2) 
        m3 = g(mas[i] + h1 / 2, ans[i - 1][0] + h1 * k2 / 2, ans[i - 1][1] + h1 * m2 / 2) 
        k4 = f(mas[i] + h1, ans[i -1][0] + h1 * k3, ans[i - 1][1] + h1 * m3) 
        m4 = g(mas[i] + h1, ans[i - 1][0] + h1 * k3, ans[i - 1][1] + h1 * m3) 
        dx = h1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        dy = h1/6 * (m1 + 2 * m2 + 2 * m3 + m4)
        ans.append([ans[i - 1][0] + dx, ans[i - 1][1] + dy])
    return ans

def RungeKutteMethod(f, g, start, xstart, ystart, t2, eps, orig, orig2):
    h = 2
    a = []
    j = 0
    while True:
        ans = []
    
        mas = np.linspace(start, t2, h)
        ans.append([xstart, ystart, h])
        h1 = (t2 - start) / (h-1) 

        for i in range(1, h):
            k1 = f(mas[i], ans[i - 1][0], ans[i - 1][1]) 
            m1 = g(mas[i], ans[i - 1][0], ans[i - 1][1]) 
            k2 = f(mas[i] + h1 / 2, ans[i - 1][0] + h1 *k1 / 2, ans[i -1 ][1] + h1 * m1 / 2) 
            m2 = g(mas[i] + h1 / 2, ans[i - 1][0] + h1 *k1 / 2, ans[i - 1][1] + h1 * m1 / 2) 
            k3 = f(mas[i] + h1 / 2, ans[i - 1][0] + h1 * k2 / 2, ans[i - 1][1] + h1 * m2 / 2) 
            m3 = g(mas[i] + h1 / 2, ans[i - 1][0] + h1 * k2 / 2, ans[i - 1][1] + h1 * m2 / 2) 
            k4 = f(mas[i] + h1, ans[i -1][0] + h1 * k3, ans[i - 1][1] + h1 * m3) 
            m4 = g(mas[i] + h1, ans[i - 1][0] + h1 * k3, ans[i - 1][1] + h1 * m3) 
            dx = h1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
            dy = h1/6 * (m1 + 2 * m2 + 2 * m3 + m4)
            ans.append([ans[i - 1][0] + dx, ans[i - 1][1] + dy, h])
        
    
        if(h != 2):
            print(i)
            a.append([ans[h - 1][0], ans[h - 1][1], ans[h - 1][0] / a[j - 1][0], ans[h - 1][1] / a[j - 1][1],  abs(ans[h - 1][0] - orig(mas[h - 1])), abs(ans[h - 1][1] - orig2(mas[h - 1])), math.log2(abs(ans[h - 1][0] - orig(mas[h - 1]))/(a[j - 1][5])), math.log2(abs(ans[h - 1][1] - orig2(mas[h - 1]))/(a[j - 1][5])), max(math.log2(abs(ans[h - 1][0] - orig(mas[h - 1]))/(a[j - 1][5])), math.log2(abs(ans[h - 1][1] - orig2(mas[h - 1]))/(a[j - 1][5])))])
        else:
            a.append([ans[h - 1][0], ans[h - 1][1], 'null', 'null',  abs(ans[h - 1][0] - orig(mas[h - 1])), abs(ans[h - 1][1] - orig2(mas[h - 1])), 'null', 'null', 'null'])
        if abs(ans[h - 1][0] - orig(mas[h - 1])) < eps and abs(ans[h - 1][1] - orig2(mas[h - 1])) < eps:
            return {'ans': ans, 'a': a}
        j += 1    
        h *= 2
