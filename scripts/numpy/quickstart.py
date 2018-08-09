#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: undefined
 @Desc:
 @Author: yuzhongchun
 @Date: 2018-08-09 22:33:33
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-08-09 22:33:33
"""

import numpy as np
from numpy import pi

# The Basics
"""
NumPy’s main object is the homogeneous multidimensional array.
It is a table of elements (usually numbers), all of the same type,
indexed by a tuple of positive integers. In NumPy dimensions are called axes.
"""
"""
NumPy’s array class is called ndarray. It is also known by the alias array.
Note that numpy.array is not the same as the Standard Python Library class array.array,
which only handles one-dimensional arrays and offers less functionality.
The more important attributes of an ndarray object are:
    ndarray.ndim
    ndarray.shape
    ndarray.size
    ndarray.dtype
    ndarray.itemsize
    ndarray.data
"""

# Basic use
a = np.arange(15).reshape(3, 5)
print(a)
print('=' * 60)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.dtype.name)
print(a.itemsize)
print(a.data)
print(type(a))

# Array creation
b = np.array([6, 7, 8])
print()
print('=' * 60)
print(type(b))
print('=' * 60)
print(b.dtype)

c = np.array([(1.5, 2, 3), (4, 5, 6)])
print(c)
"""
Often, the elements of an array are originally unknown, but its size is known.
Hence, NumPy offers several functions to create arrays with initial placeholder content.
These minimize the necessity of growing arrays, an expensive operation.
The function zeros creates an array full of zeros, the function ones creates an array full of ones,
and the function empty creates an array whose initial content is random and depends on the state of the memory.
By default, the dtype of the created array is float64.
"""

a = np.zeros((3, 4))
print('=' * 60)
print(a)

b = np.ones((2, 3, 4), dtype=np.int16)
print('=' * 60)
print(b)

c = np.empty((2, 3))
print('=' * 60)
print(c)
"""
To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists.
"""
a = np.arange(10, 30, 5)
print('=' * 60)
print(a)
b = np.arange(0, 2, 0.3)
print('=' * 60)
print(b)

c = np.linspace(0, 2, 9)
print('=' * 60)
print(c)

x = np.linspace(0, 2 * pi, 100)
print('=' * 60)
print(x)
f = np.sin(x)
print('=' * 60)
print(f)

# Printing Arrays
