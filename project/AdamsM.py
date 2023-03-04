import numpy as np
from RungeKutteM import RungeKutteMethod
import pandas as pd
import math



def adams_method(func: list, start, end, start_value: list, h):
    
    
    mas = np.linspace(start, end, h)
    h1 = (end - start) / (h-1) 
    ans = []
    ans = RungeKutteMethod(func, start, mas[4], start_value, 4)

     
    for i in range(4, h):
        app1 = [mas[i-1], *[ans[i-1][j] for j in range(len(func))]]
       
        app2 = [mas[i-2], *[ans[i-2][j] for j in range(len(func))]]
        app3 = [mas[i-3], *[ans[i-3][j] for j in range(len(func))]]
        app4 = [mas[i-4], *[ans[i-4][j] for j in range(len(func))]]

        zn = np.array([ans[i-1][j] + h1/24 * (55 * func[j](*app1) - 59 * func[j](*app2) + 37 * func[j](*app3) - 9 * func[j](*app4)) for j in range(len(func))])
    
        yn = np.array([ans[i-1][j] + h1/24 * (9 * func[j](mas[i], *zn) + 19 * func[j](*app1) - 5 * func[j](*app2) + func[j](*app3)) for j in range(len(func))])
        ans.append(yn)

    return ans


def norma_adams():
    pass
        



