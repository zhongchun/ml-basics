#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: undefined
 @Desc:
 @Author: yuzhongchun
 @Date: 2018-08-23 22:57:13
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-08-23 22:57:13
"""

# import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
# print(t)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(
    xlabel='time(s)',
    ylabel='voltage(mV)',
    title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
