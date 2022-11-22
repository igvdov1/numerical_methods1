import numpy as np
from RungeKutteM import Runge_Kutte_for_4
import pandas as pd
import math
# def generate_first_3_points(f, g, start, xstart, ystart, array, h1):
#     return Runge_Kutte_for_3(f, g, start, xstart, ystart, mas, h1)


def adams_method(f, g, start, xstart, ystart, t2, eps, orig, orig2):
    h = 8
    a = []
    j = 0
    while True:
        mas = np.linspace(start, t2, h)
        h1 = (t2 - start) / (h-1) 
        ans = []
        ans = Runge_Kutte_for_4(f, g, start, xstart, ystart, mas, h1)
        i = 4
     
        for i in range(4, h):
            zx = ans[i-1][0] + h1/24 * (55 * f(mas[i-1], ans[i-1][0], ans[i-1][1]) - 59 * f(mas[i-2], ans[i - 2][0], ans[i-2][1]) + 37 * f(mas[i - 3], ans[i-3][0], ans[i-3][1]) - 9 * f(mas[i - 4], ans[i - 4][0], ans[i-4][1]))
            zy = ans[i-1][1] + h1/24 * (55 * g(mas[i-1],ans[i-1][0], ans[i-1][1]) - 59 * g(mas[i-2], ans[i-2][0], ans[i - 2][1]) + 37 * g(mas[i - 3], ans[i-3][0], ans[i-3][1]) - 9 * g(mas[i - 4], ans[i-4][0], ans[i - 4][1]))
            yx = ans[i-1][0] + h1/24 * (9 * f(mas[i], zx, zy) + 19 * f(mas[i-1], ans[i-1][0], ans[i-1][1]) - 5 * f(mas[i-2], ans[i-2][0], ans[i-2][1]) + f(mas[i-3], ans[i - 3][0], ans[i-3][1]))
            yy = ans[i-1][1] + h1/24 * (9 * g(mas[i], zx, zy) + 19 * g(mas[i-1],ans[i-1][0], ans[i-1][1]) - 5 * g(mas[i-2], ans[i-2][0], ans[i-2][1]) + g(mas[i-3], ans[i-3][0], ans[i - 3][1]))
            ans.append([yx, yy])
        if h == 8:
            a.append([max(abs(ans[h-1][0] - orig(mas[h-1])), abs(ans[h-1][1] - orig2(mas[h - 1]))), 'null'])
        else:
            a.append([max(abs(ans[h-1][0] - orig(mas[h-1])), abs(ans[h-1][1] - orig2(mas[h - 1]))), math.log2(max(abs(ans[h-1][0] - orig(mas[h-1])), abs(ans[h-1][1] - orig2(mas[h - 1]))/a[j-1][0]))])
        if max(abs(ans[h-1][0] - orig(mas[h-1])), abs(ans[h-1][1] - orig2(mas[h - 1]))) < eps:
            return {'ans':ans, 'a': a}
        h *= 2
        j += 1
        



