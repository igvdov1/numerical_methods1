import numpy as np
import math

def sympsonMethod(x1, x2, eps, f):
    print('sympsonMethod')
    len = x2 - x1
    scet = 2
    sum1 = 100000
    sum = 0
    data = []
    flag = 0
    i = 0
    while(abs(sum - sum1) > eps):
        
        a = np.linspace(x1, x2, scet)
        sum = sum1
        sum1 = 0
        

        for i in range (0, scet-1):
            sum1 += (f(a[i]) + f(a[i+1])+4*f((a[i]+a[i+1])/2))*((a[i+1]-a[i])/6)
               


        if flag == 1:
            data.append([scet, abs(sum1 - sum), 'null', sum1])
        if flag >= 2:

            if(sum == sum1):
                break
            data.append([scet, abs(sum1 - sum),  math.log2((abs(sum - sum1))/data[flag-2][1]), sum1])
        flag +=1 
        scet *= 2
 


    return data



    
# def sympsonMethod(x1, x2, eps, f):
#     print('sympsonMethod')
#     len = x2 - x1
#     scet = 2
#     sum1 = 10000
#     sum = 0
#     data = []
#     flag = 0
#     while(abs(sum - sum1) > eps):
#         a = np.linspace(x1, x2, scet)
#         a1 = np.linspace(x1, x2, scet*2)
#         sum1 = 0
#         sum = 0

#         for i in range (0, scet*2-1):
#             if(i < scet - 1):
#                 sum += (f(a[i]) + f(a[i+1])+4*f((a[i]+a[i+1])/2))*((a[i+1]-a[i])/6)
#                 sum1 += (f(a1[i]) + f(a1[i+1])+4*f((a1[i]+a1[i+1])/2))*((a1[i+1]-a1[i])/6)
#             else:
#                 sum1 += (f(a1[i]) + f(a1[i+1])+4*f((a1[i]+a1[i+1])/2))*((a1[i+1]-a1[i])/6)
#         if(flag == 0):
#              data.append([scet, abs(sum-sum1), 'notnull', sum])
#         else:
#             data.append([scet, abs(sum-sum1), math.log2(data[flag-1][1]/(abs(sum - sum1))), sum])
#         scet*=2
#         flag += 1
#     return data