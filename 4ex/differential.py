import math
import random

def derivative(func, x, eps, real):
    a = []
    count = 0
    dx = 1
    while dx > eps:
        sum = ((func(x+dx)+random.uniform(-0.000001, 0.000001)) - (func(x)+random.uniform(-0.000001, 0.000001)))/dx
        a.append([sum, real - sum])
            
        print(dx)
        dx /= 2  
        count += 1
    print(count)
    return a
