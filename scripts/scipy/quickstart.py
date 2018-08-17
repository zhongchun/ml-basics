#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: undefined
 @Desc:
 @Author: yuzhongchun
 @Date: 2018-08-15 23:29:21
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-08-15 23:29:21
"""

import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
from numpy import poly1d

# 1. Basic functions

# 1.1 Interaction with Numpy

# 1.2 Index Tricks
print('=' * 80)
a = np.concatenate(([3], [0] * 5, np.arange(-1, 1.002, 2 / 9.0)))
print(a)
a = np.r_[3, [0] * 5, -1:1:10j]
print('=' * 80)
print(a)
print(type(a))
print(a.shape)

b = np.mgrid[0:5, 0:5]
print('=' * 80)
print(b)
print(type(b))
print(b.shape)

c = np.mgrid[0:5:4j, 0:5:4j]
print('=' * 80)
print(c)
print(type(c))
print(c.shape)

# 1.3 Shape manipulation
# 1.4 Polynomials
p = poly1d([3, 4, 5])
print('=' * 80)
print(p)
print(type(p))
print('=' * 80)
print(p * p)
print('=' * 80)
print(p.integ(k=6))
print('=' * 80)
print(p.deriv())


# 1.5 Vectorizing functions(vectorize)
def addsubtract(a, b):
    if a > b:
        return a - b
    else:
        return a + b


vec_addsubtract = np.vectorize(addsubtract)
vec = vec_addsubtract([0, 3, 6, 9], [1, 3, 5, 7])
print('=' * 80)
print(vec)

# 1.6 Type handling
