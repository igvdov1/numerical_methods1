import numpy as np
def eilerMethod(func: list, start, end, start_value: list, h):

    ans = []
    k = np.linspace(start, end, h)
    h1 = (end-start)/(h)

    ans.append(start_value)

    for i in range(1, h):
        
        app1 = [k[i-1], *[ans[i-1][j] for j in range(len(func))]]
        
        y = [ans[i-1][j] + h1 * func[j](*app1) for j in range(len(func))]
        ans.append(y)
        
        
        

    return ans