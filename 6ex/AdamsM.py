import numpy as np
from RungeKutteM import RungeKutteMethod
import pandas as pd
import math
# def generate_first_3_points(f, g, start, xstart, ystart, array, h1):
#     return Runge_Kutte_for_3(f, g, start, xstart, ystart, mas, h1)


def adams_method(func: list, start, end, start_value: list, h):
    
    
    mas = np.linspace(start, end, h)
    h1 = (end - start) / (h-1) 
    ans = []
    ans = RungeKutteMethod(func, start, mas[4], start_value, 4)

     
    for i in range(4, h):
        zn =[ans[i-1][j] + h1/24 * (55 * func[j](mas[i-1], ans[i-1][0], ans[i-1][1]) - 59 * func[j](mas[i-2], ans[i-2][0], ans[i - 2][1]) + 37 * func[j](mas[i - 3], ans[i-3][0], ans[i-3][1]) - 9 * func[j](mas[i - 4], ans[i-4][0], ans[i - 4][1])) for j in range(len(func))]
        # zx = ans[i-1][0] + h1/24 * (55 * func[0](mas[i-1], ans[i-1][0], ans[i-1][1]) - 59 * func[0](mas[i-2], ans[i - 2][0], ans[i-2][1]) + 37 * func[0](mas[i - 3], ans[i-3][0], ans[i-3][1]) - 9 * func[0](mas[i - 4], ans[i - 4][0], ans[i-4][1]))
        # zy = ans[i-1][1] + h1/24 * (55 * func[1](mas[i-1], ans[i-1][0], ans[i-1][1]) - 59 * func[1](mas[i-2], ans[i-2][0], ans[i - 2][1]) + 37 * func[1](mas[i - 3], ans[i-3][0], ans[i-3][1]) - 9 * func[1](mas[i - 4], ans[i-4][0], ans[i - 4][1]))
        # yx = ans[i-1][0] + h1/24 * (9 * func[0](mas[i], zx, zy) + 19 * func[0](mas[i-1], ans[i-1][0], ans[i-1][1]) - 5 * func[0](mas[i-2], ans[i-2][0], ans[i-2][1]) + func[0](mas[i-3], ans[i - 3][0], ans[i-3][1]))
        # yy = ans[i-1][1] + h1/24 * (9 * func[1](mas[i], zx, zy) + 19 * func[1](mas[i-1],ans[i-1][0], ans[i-1][1]) - 5 * func[1](mas[i-2], ans[i-2][0], ans[i-2][1]) + func[1](mas[i-3], ans[i-3][0], ans[i - 3][1]))
        yn = [ans[i-1][j] + h1/24 * (9 * func[j](mas[i], zn[0], zn[1]) + 19 * func[j](mas[i-1], ans[i-1][0], ans[i-1][1]) - 5 * func[j](mas[i-2], ans[i-2][0], ans[i-2][1]) + func[j](mas[i-3], ans[i - 3][0], ans[i-3][1])) for j in range(len(func))]
        ans.append([yn[0], yn[1]])

    return ans
        



