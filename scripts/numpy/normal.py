#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: undefined
 @Desc:
 @Author: yuzhongchun
 @Date: 2018-08-17 23:17:59
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-08-17 23:17:59
"""

import numpy as np
import matplotlib.pyplot as plt

u = np.random.uniform(0.0, 1.0, 10000)
print(type(u))
print(u.shape)
plt.hist(u, 80, facecolor='g', alpha=0.75)
plt.grid(True)
plt.show()

times = 1000
for time in range(times):
    u += np.random.uniform(0.0, 1.0, 10000)
print(len(u))
u /= times
print(len(u))

plt.hist(u, 80, facecolor='g', alpha=0.75)
plt.grid(True)
plt.show()
