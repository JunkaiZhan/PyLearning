#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Author: zhanjunkai

import numpy as np

# Create the ndarray
a = np.arange(20)
print(type(a), " : ", a)

# method: Reshape the ndarray
a = a.reshape(2, 2, 5)
print(type(a), " : \n", a)

# member: ndim shape size and dtype
print("a.ndim: ", a.ndim)
print("a.shape: ", a.shape)
print("a.size: ", a.size)
print("a.dtype: ", a.dtype)

# Create the array
raw = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
a = np.array(raw)
print(type(a), " : \n", a)

# Specified dim
d = (4, 5)
np.zeros(d)