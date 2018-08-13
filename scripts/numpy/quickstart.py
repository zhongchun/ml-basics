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
from numpy import newaxis

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

# Indexing, Slicing and Iterating
a = np.arange(10)**3
print('=' * 60)
print(a)
print(a[2])
print(a[2:5])
a[:6:2] = -1000
print('=' * 60)
print(a)
print('=' * 60)
# reversed a
print(a[::-1])
print('=' * 60)
for i in a:
    print(i, i**(1 / 3.))


def func(x, y):
    return 10 * x + y


b = np.fromfunction(func, (5, 4), dtype=int)
print('=' * 60)
print(b)
print(b[2, 3])
print('=' * 60)
print(b[0:5, 1])
print('=' * 60)
print(b[:, 1])
print('=' * 60)
print(b[1:3, :])
print('=' * 60)
print(b[-1])

c = np.array([[[0, 1, 2], [10, 12, 13]], [[100, 101, 102], [110, 112, 113]]])
print('=' * 60)
print(c)
print('=' * 60)
print(c[1, ...])
print('=' * 60)
print(c[..., 2])

for row in b:
    print(row)

print('=' * 60)
for element in b.flat:
    print(element)

# Shape Manipulation
tmp = 10 * np.random.random((3, 4))
a = np.floor(tmp)
print('=' * 60)
print(tmp)
print('=' * 60)
print(a)
print(a.shape)

print('=' * 60)
print(a.ravel())
print('=' * 60)
print(a.reshape(6, 2))
print('=' * 60)
print(a.T)
print('=' * 60)
print(a)
a.resize(2, 6)
print('=' * 60)
print(a)

# Stacking together different arrays
tmp = 10 * np.random.random((2, 2))
a = np.floor(tmp)
print('=' * 60)
print(a)
tmp = 10 * np.random.random((2, 2))
b = np.floor(tmp)
print('=' * 60)
print(b)
print('=' * 60)
print(np.vstack((a, b)))
print('=' * 60)
print(np.hstack((a, b)))
print('=' * 60)
print(np.column_stack((a, b)))

a = np.array([4., 2.])
b = np.array([3., 8.])
print('=' * 60)
print(a)
print('=' * 60)
print(b)
print('=' * 60)
print(np.column_stack((a, b)))
print('=' * 60)
print(np.hstack((a, b)))
print('=' * 60)
print(a[:, newaxis])
print('=' * 60)
print(np.column_stack((a[:, newaxis], b[:, newaxis])))
print('=' * 60)
print(np.r_[1:4, 0, 4])

# Splitting one array into several smaller ones
tmp = 10 * np.random.random((2, 12))
a = np.floor(tmp)
print('=' * 60)
print(a)
print('=' * 60)
print(np.hsplit(a, 3))
print('=' * 60)
print(np.hsplit(a, (3, 4)))

# Copies and Views
# No copy at all
a = np.arange(12)
# print('=' * 60)
# print(a)
b = a
print(b is a)
print('=' * 60)
b.shape = 3, 4
print('=' * 60)
print(a.shape)


def func1(x):
    print(id(x))


print('=' * 60)
print(id(a))
print('=' * 60)
func1(a)

# View or Shallow copy
# Different array objects can share the same data. The view method creates a new array object
# that looks at the same data.
c = a.view()
print('=' * 60)
print(c)
print('=' * 60)
print(c is a)
print(c.base is a)
print(c.flags.owndata)
print(c.shape)
print('=' * 60)
print(a.shape)
print('=' * 60)
c.shape = 2, 6
print('=' * 60)
print(c)
print('=' * 60)
print(a)
c[0, 4] = 1234
print('=' * 60)
print(c)
print('=' * 60)
print(a)

# Deep Copy
# The copy method makes a complete copy of the array and its data
d = a.copy()
print('=' * 60)
print(d)
print(d is a)
print(d.base is a)
d[0, 0] = 9999
print('=' * 60)
print(d)
print('=' * 60)
print(a)

# Less Basic
# Broadcasting rules

# Fancy indexing and index tricks
# Indexing with Arrays of Indices
a = np.arange(12)**2
i = np.array([1, 1, 3, 8, 5])
print('=' * 60)
print(a)
print('=' * 60)
print(a[i])
j = np.array([[3, 4], [9, 7]])
print('=' * 60)
print(a[j])
