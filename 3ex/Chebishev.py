import math
def Chebyshev(n):
    arr = []
    for i in range(1, n+1):
        arr.append(math.cos((2*i - 1)/(2*n) * math.pi))
    return arr