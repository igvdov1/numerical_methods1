import math


if __name__ == '__main__':
    i = 1
    e = 1.0
    k = 1.0
    x = math.inf
    x1 = 1000000.0
    x2 = 1.0
    while (i + e != i):
        e /= 2
    e *= 2
    m = math.log(e, 2) * -1

    print ("epsilon = ", e)
    print("mantis = ", m)
    print("1 + e == 1 -",1+e == 1)
    print("1+e/2 == 1 -", 1+e/2 == 1)
    print("1+e/2 + e == 1+e/2",1+e/2+e ==1 + e/2)
    print("1+e/2 + e == 1+e", 1 + e / 2 + e == 1 + e)
    print("по отдельности эти числа меньше эпсилон, а вместе больше", 1 + pow(10, -16) + pow(10, - 16))
    print(1 + (pow(10, -16) + pow(10, -16)))
