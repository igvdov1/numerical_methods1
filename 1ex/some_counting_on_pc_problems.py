import math


if __name__ == '__main__':
    #1  machine epsilon
    i = 1
    e = 1.0
    while (i + e/2 != i):
        e /= 2
    print("epsilon = ", e)
    #2 mantissa
    e *= 2
    m = math.log(e/2, 2) * -1
    print("mantis = ", m)
    #3 e_min
    e_min = 1.0
    while 2**(e_min-1) != 0:
        e_min -= 1
    print("e_min =", e_min+51-1)
    #4 e_max
    e_max = 10.0
    k = 2**e_max
    while(k <= 2**1200):
        e_max+=1
        try:
            k = 2**e_max
        except OverflowError:
            print("e_max =", e_max)
            break



    #5 comparison
    print("1 + e == 1 -",1+e == 1)
    print("1+e/2 == 1 -", 1+e/2 == 1)
    print("1+e/2 + e == 1+e/2",1+e/2+e ==1 + e/2)
    print("1+e/2 + e == 1+e", 1 + e / 2 + e == 1 + e)
    print("по отдельности эти числа меньше эпсилон, а вместе больше", 1 + pow(10, -16) + pow(10, - 16))
    print(1 + (pow(10, -16) + pow(10, -16)))


