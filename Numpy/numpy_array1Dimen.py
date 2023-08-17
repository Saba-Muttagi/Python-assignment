
'''
@Author: Saba Muttagi
@Date: 2023-08-17
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-17
@Title : Python program to convert a list of numeric value into a one-dimensional
NumPy array.
Expected Output:
Original List: [12.23, 13.32, 100, 36.32]
One-dimensional numpy array: [ 12.23 13.32 100. 36.32]
'''

import numpy as np

arr=np.array([12.23, 13.32, 100, 36.32])
print(arr)

print(type(arr))