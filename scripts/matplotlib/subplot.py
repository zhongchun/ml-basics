#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: undefined
 @Desc:
 @Author: yuzhongchun
 @Date: 2018-08-29 23:00:29
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-08-29 23:00:29
"""

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
# print(x1)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('time(s)')
plt.ylabel('Undamped')

plt.show()
