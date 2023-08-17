'''
@Author: Saba Muttagi
@Date: 2023-08-17
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-17
@Title :Python program to create a 8x8 matrix and fill it with a checkerboard pattern.
Checkerboard pattern:
[[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]
[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]
[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]
[0 1 0 1 0 1 0 1]
[1 0 1 0 1 0 1 0]]
'''

import numpy as np

a=np.ones((3,3))
print(a)

a=np.zeros((8,8),dtype=int)
a[1::2,0::2]=1
a[0::2,1::2]=1
print("Checkerboard pattern is :")
print(a)