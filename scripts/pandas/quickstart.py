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

# Viewing Data
print('=' * 80)
print(df.head())
print('=' * 80)
print(df.tail(3))

print('=' * 80)
print(df.index)
print('=' * 80)
print(df.columns)
print('=' * 80)
print(df.values)
print('=' * 80)
print(type(df.values))
print('=' * 80)
print(df.describe())
print('=' * 80)
print(df.T)
print('=' * 80)
print(df.sort_index(axis=1, ascending=False))
print('=' * 80)
print(df.sort_values(by='B'))

# Selections
# Getting
print('=' * 80)
print(df['A'])
print('=' * 80)
print(df[0:3])
print('=' * 80)
print(df['2018-01-01':'2018-01-04'])

# Selection by Label
print('=' * 80)
print(df.loc[dates[0]])
print('=' * 80)
print(df.loc[:, ['A', 'B']])
print('=' * 80)
print(df.loc['20180102':'20180104', ['A', 'B']])
print('=' * 80)
print(df.loc['20180102', ['A', 'B']])
# get a scalar value
print('=' * 80)
print(df.loc[dates[0], 'A'])
print('=' * 80)
print(df.at[dates[0], 'A'])

# Selection by Position
print('=' * 80)
print(df.iloc[3])
print('=' * 80)
print(df.iloc[3:5, 0:2])
print('=' * 80)
print(df.iloc[[1, 2, 4], [0, 2]])
print('=' * 80)
print(df.iloc[1:3, :])
print('=' * 80)
print(df.iloc[:, 1:3])
print('=' * 80)
print(df.iloc[1, 1])
print('=' * 80)
print(df.iat[1, 1])

# Boolean Indexing
print('=' * 80)
print(df.A > 0)
print('=' * 80)
print(df[df.A > 0])
print('=' * 80)
print(df > 0)
print('=' * 80)
print(df[df > 0])
df2 = df.copy()
print('=' * 80)
print(df)
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print('=' * 80)
print(df2)
print('=' * 80)
print(df2['E'])
print('=' * 80)
print(df2['E'].isin(['two', 'four']))
print('=' * 80)
print(df2[df2['E'].isin(['two', 'four'])])

# Setting
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20180102', periods=6))
print('=' * 80)
print(s1)
df['F'] = s1
print('=' * 80)
print(df)
print('=' * 80)
df.at[dates[0], 'A'] = 0
print('=' * 80)
print(df)
df.iat[0, 1] = 0
print('=' * 80)
print(df)
df.loc[:, 'D'] = np.array([5] * len(df))
print('=' * 80)
print(df)

df2 = df.copy()
df2[df2 > 0] = -df2
print('=' * 80)
print(df2)

# Missing Data
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print('=' * 80)
print(df1)
print('=' * 80)
tmp1 = df1.dropna(how='any')
print(tmp1)
print('=' * 80)
print(df1.fillna(value=5))
print('=' * 80)
print(pd.isna(df1))

# Operations
# Stats
print('=' * 80)
print(df.mean())
print('=' * 80)
print(df.mean(0))
print('=' * 80)
print(df.mean(1))

# Apply
print('=' * 80)
print(df.apply(np.cumsum))

# Histogramming
s = pd.Series(np.random.randint(0, 7, size=10))
print('=' * 80)
print(s)
print('=' * 80)
print(s.value_counts())

# String Methods
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print('=' * 80)
print(s)

# Merge
# Concat
df = pd.DataFrame(np.random.randn(10, 4))
print('=' * 80)
print(df)
pieces = [df[:3], df[3:7], df[7:]]
print('=' * 80)
print(pieces)
print('=' * 80)
print(pd.concat(pieces))

# Join
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print('=' * 80)
print(left)
print('=' * 80)
print(right)
print('=' * 80)
print(pd.merge(left, right, on='key'))

# Append
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print('=' * 80)
print(df)

s = df.iloc[3]
print('=' * 80)
print(df.append(s, ignore_index=True))

# Grouping
df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C':
    np.random.randn(8),
    'D':
    np.random.randn(8)
})
print('=' * 80)
print(df)
print('=' * 80)
print(df.groupby('A').sum())

# Reshaping
tuples = list(
    zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
print('=' * 80)
print(tuples)
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print('=' * 80)
print(index)
df2 = df[:4]
print('=' * 80)
print(df2)

# Time Series
rng = pd.date_range('1/1/2018', periods=100, freq='S')
print('=' * 80)
print(rng)
ts = pd.Series(np.random.randn(len(rng)), rng)
print('=' * 80)
print(ts)
ts_utc = ts.tz_localize('UTC')
print('=' * 80)
print(ts_utc)
print('=' * 80)
print(ts_utc.tz_convert('US/Eastern'))

# Categoricals
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']
})
print('=' * 80)
print(df)
df["grade"] = df["raw_grade"].astype("category")
print('=' * 80)
print(df)
print('=' * 80)
print(df['grade'])

# Plotting
ts = pd.Series(
    np.random.randn(1000), index=pd.date_range('1/1/2016', periods=1000))
print('=' * 80)
print(ts)
ts = ts.cumsum()
print('=' * 80)
ts.plot()
plt.show()

# Getting Data In/Out
# CSV
# HDF5
# Excel
