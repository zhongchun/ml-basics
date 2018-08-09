#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @FileName: undefined
 @Desc:
 @Author: yuzhongchun
 @Date: 2018-08-09 22:05:04
 @Last Modified by: yuzhongchun
 @Last Modified time: 2018-08-09 22:05:04
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

data_url = "./datasets/50_Startups.csv"
dataset = pd.read_csv(data_url)
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

label_encoder = LabelEncoder()
X[:, 3] = label_encoder.fit_transform(X[:, 3])

one_hot_encoder = OneHotEncoder(categorical_features=[3])
X = one_hot_encoder.fit_transform(X).toarray()

X = X[:, 1:]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, Y_train)

y_pred = regressor.predict(X_test)
print(y_pred)