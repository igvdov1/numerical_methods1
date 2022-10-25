import numpy as np
import math

def rectangleMethod1(x1, x2, eps, f):
    len = x2 - x1
    scet = 2
    sum1 = 10000
    sum = 0
    data = []
    flag = 0
    while(abs(sum - sum1) > eps):
        a = np.linspace(x1, x2, scet)
        a1 = np.linspace(x1, x2, scet*2)
        sum1 = 0
        sum = 0

        for i in range (0, scet*2-1):
            if(i < scet - 1):
                sum += f((a[i]+a[i+1])/2)*(a[i+1]-a[i])
                sum1 += f((a1[i]+a1[i+1])/2)*(a1[i+1]-a1[i])
            else:
                sum1 += f((a1[i]+a1[i+1])/2)*(a1[i+1]-a1[i])
        
        if flag == 0:
            data.append([scet, abs(sum-sum1), 'null', sum])
        else:
            data.append([scet, abs(sum-sum1), math.log2((abs(sum - sum1))/data[flag-1][1]), sum])
        scet*=2
        flag += 1
       
    return data