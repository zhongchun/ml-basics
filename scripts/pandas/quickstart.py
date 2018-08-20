#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: undefined
 @Desc:
 @Author: yuzhongchun
 @Date: 2018-08-16 23:11:43
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-08-16 23:11:43
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Object Creation
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print('=' * 80)
print(s)

dates = pd.date_range('20180101', periods=6)
print('=' * 80)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print('=' * 80)
print(df)

df2 = pd.DataFrame({
    'A': 1,
    'B': pd.Timestamp('20180820'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})
print('=' * 80)
print(df2)
print('=' * 80)
print(df2.dtypes)
print('=' * 80)

# Viewing Data
