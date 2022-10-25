import numpy as np
import math
import numpy as np
import math 
def trapeseMethod(x1, x2, eps, f):
    print('trapeseMethod')
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
            sum1 += (f(a[i])+f(a[i+1]))/2*(a[i+1]-a[i])
               


        if flag == 1:
            data.append([scet, abs(sum1 - sum), 'null', sum1])
        if flag >= 2:

            if(sum == sum1):
                break
            data.append([scet, abs(sum1 - sum),  math.log2((abs(sum - sum1))/data[flag-2][1]), sum1])
        flag +=1 
        scet *= 2
        print(flag, abs(sum - sum1))


    return data



    
