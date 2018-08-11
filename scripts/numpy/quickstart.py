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
"""
When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:
    the last axis is printed from left to right,
    the second-to-last is printed from top to bottom,
    the rest are also printed from top to bottom, with each slice separated from the next by an empty line.
"""
a = np.arange(6)
print('=' * 60)
print(a)

b = np.arange(12).reshape(4, 3)
print('=' * 60)
print(b)

c = np.arange(24).reshape(2, 3, 4)
print('=' * 60)
print(c)

print('=' * 60)
print(np.arange(10000))

print('=' * 60)
# force NumPy to print the entire array
# np.set_printoptions(threshold=np.nan)
print(np.arange(10000).reshape(100, 100))

# Basic Operations
# Arithmetic operators in arrays apply elementwise
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print('=' * 60)
print(a)
print(b)
c = a - b
print('=' * 60)
print(c)
d = b**2
print('=' * 60)
print(d)
e = 10 * np.sin(a)
print('=' * 60)
print(e)
f = a < 35
print('=' * 60)
print(f)

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
C = A * B
print('=' * 60)
print(C)
D = A @ B
print('=' * 60)
print(D)
E = A.dot(B)
print('=' * 60)
print(E)

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print('=' * 60)
print(a.dtype)
print(b.dtype.name)
c = a + b
print('=' * 60)
print(c.dtype)
print(c)
d = np.exp(c * 1j)
print('=' * 60)
print(d.dtype)
print(d)

a = np.random.random((2, 3))
print('=' * 60)
print(a)
print('a.sum =', a.sum())
print('a.min =', a.min())
print('a.max =', a.max())

b = np.arange(12).reshape(3, 4)
print('=' * 60)
print(b)
print('=' * 60)
print(b.sum(axis=0))
print('=' * 60)
print(b.min(axis=0))
print('=' * 60)
print(b.cumsum(axis=1))

# Universal Functions, i.e. ufunc
B = np.arange(3)
print('=' * 60)
print(B)
print('=' * 60)
print(np.exp(B))
print('=' * 60)
print(np.sqrt(B))
C = np.array([2., -1., 4.])
print('=' * 60)
print(np.add(B, C))
