'''
@Author: Saba Muttagi
@Date: 2023-08-17
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-17
@Title :Python program to convert a list and tuple into arrays.
List to array:
[1 2 3 4 5 6 7 8]
Tuple to array:
[[8 4 6]
[1 2 3]]'''

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8])
print("List to array :")
print(arr)

arr1=np.array([(8,4,6),(1,2,3)])
print("Tuple to array :")
print(arr1)