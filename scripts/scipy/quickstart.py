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
import matplotlib as mpl
import matplotlib.pyplot as plt
# from scipy import some_module

# Basic functions

# Interaction with Numpy
print('=' * 80)

# Index Tricks
a = np.concatenate(([3], [0]*5, np.arange(-1, 1.002, 2/9.0)))
print(a)
