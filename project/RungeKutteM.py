import numpy as np
import math

# def Runge_Kutte_for_4(f,g , start, xstart, ystart, mas, h1):
#     ans = []
#     ans.append([xstart, ystart])
#     for i in range(1, 4):
#         k1 = f(mas[i], ans[i - 1][0], ans[i - 1][1]) 
#         m1 = g(mas[i], ans[i - 1][0], ans[i - 1][1]) 
#         k2 = f(mas[i] + h1 / 2, ans[i - 1][0] + h1 *k1 / 2, ans[i -1 ][1] + h1 * m1 / 2) 
#         m2 = g(mas[i] + h1 / 2, ans[i - 1][0] + h1 *k1 / 2, ans[i - 1][1] + h1 * m1 / 2) 
#         k3 = f(mas[i] + h1 / 2, ans[i - 1][0] + h1 * k2 / 2, ans[i - 1][1] + h1 * m2 / 2) 
#         m3 = g(mas[i] + h1 / 2, ans[i - 1][0] + h1 * k2 / 2, ans[i - 1][1] + h1 * m2 / 2) 
#         k4 = f(mas[i] + h1, ans[i -1][0] + h1 * k3, ans[i - 1][1] + h1 * m3) 
#         m4 = g(mas[i] + h1, ans[i - 1][0] + h1 * k3, ans[i - 1][1] + h1 * m3) 
#         dx = h1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
#         dy = h1/6 * (m1 + 2 * m2 + 2 * m3 + m4)
#         ans.append([ans[i - 1][0] + dx, ans[i - 1][1] + dy])
#     return ans

def RungeKutteMethod(func: list, start, end, start_value: list, h):
    
    ans = []
    
    mas = np.linspace(start, end, h)
  
    ans.append([l for l in start_value])
    h1 = (end - start) / (h - 1)
    
    for i in range(1, h):
        
        k1 = np.array([j(mas[i], *[ans[i - 1][l] for l in range(len(func))]) for j in func])
        k2 = np.array([j(mas[i] + h1 / 2, *[ans[i - 1][l] + h1 *k1[l] / 2 for l in range(len(func))]) for j in func])
        k3 = np.array([j(mas[i] + h1 / 2, *[ans[i - 1][l] + h1 *k2[l] / 2 for l in range(len(func))]) for j in func])
        k4 = np.array([j(mas[i] + h1 / 2, *[ans[i - 1][l] + h1 *k3[l] / 2 for l in range(len(func))]) for j in func])
      
        dn = [h1/6 * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j]) for j in range(len(func))]
        
        ans.append([ans[i - 1][j] + dn[j] for j in range(len(func))])

    
    return ans


def rungekutte_norma(values: list):
    return max(values)

