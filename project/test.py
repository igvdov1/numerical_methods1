
from AdamsM import adams_method
from RungeKutteM import RungeKutteMethod
import numpy as np
from CaushiM import eilerMethod
from matplotlib import pyplot as plt
import pandas as pd
from runge_rule import runge_rule
delta = 500
r = 10
b = 8/3

def xfunc(t, x, y, z):
    return 500 * (y - x)    
def yfunc(t, x, y, z):
    return x * (10 - z) - y
def zfunc(t, x, y, z):
    return x * y - 8/3 * z


if __name__ == '__main__':
    k = ''
    i = 7
    k += str(i)
    print(k)