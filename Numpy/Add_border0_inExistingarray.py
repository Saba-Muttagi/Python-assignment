'''
@Author: Saba Muttagi
@Date: 2023-08-17
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-17
@Title :Python program to add a border (filled with 0's) around an existing array.
Expected Output:
Original array:
[[ 1. 1. 1.]
[ 1. 1. 1.]
[ 1. 1. 1.]]
1 on the border and 0 inside in the array
[[ 0. 0. 0. 0. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 1. 1. 1. 0.]
[ 0. 0. 0. 0. 0.]]
'''

import numpy as np

x=np.ones((3,3))
print("Original array is: ")
print(x)

x=np.pad(x,pad_width=1,mode='constant',constant_values=0)
print("Array with 1 on the border and 0 inside:")
print(x)