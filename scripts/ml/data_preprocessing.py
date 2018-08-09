#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: undefined
 @Desc:
 @Author: yuzhongchun
 @Date: 2018-08-06 22:44:12
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-08-06 22:44:12
"""

# Import the libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

np.set_printoptions(suppress=True)

# Importing dataset
data_url = "./datasets/Data.csv"
dataset = pd.read_csv(data_url)

print('=' * 80)
print(dataset.head())
print('=' * 80)
print(dataset.shape)
print('=' * 80)
dataset.info()
print('=' * 80)
print(dataset.describe())
print('=' * 80)
print(dataset.describe(include=['O']))
print('=' * 80)
print(dataset.isnull().sum().sort_values(ascending=False))
print('=' * 80)

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

# print(type(X))
print(X)
# print(type(Y))
# print(Y)

# Handling the missing data
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print('=' * 80)
print(X)

# Encoding categorical data
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
print('=' * 80)
print(X)

# Creating a dummy variable
one_hot_encoder = OneHotEncoder(categorical_features=[0])
X = one_hot_encoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)
print('=' * 80)
print(X)
print(Y)

# Splitting the datasets into training sets and Test sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0)

print('=' * 80)
print(X_train)
print('=' * 80)
print(X_test)

# Feature Scaling
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

print('=' * 80)
print(X_train)
print('=' * 80)
print(X_test)
