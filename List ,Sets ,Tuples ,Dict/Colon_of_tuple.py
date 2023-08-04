
'''
@Author: Saba Muttagi
@Date: 2023-07-30
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-30
@Title : Python program to create the colon of a tuple
'''

from copy import deepcopy

#creating a tuple
tuple_t = ("HEY",6,[],86.88,[45,78],False) 
print("Original tuple :",tuple_t)

#make a copy of a tuple using deepcopy() function
colon= deepcopy(tuple_t)
colon[4].append(50)
print("Colon of tuple:",colon)
print("the tuple :",tuple_t)