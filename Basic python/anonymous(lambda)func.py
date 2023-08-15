
'''
@Author: Saba Muttagi
@Date: 2023-08-15
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-15
@Title :Python program to get numbers divisible by fifteen from a list using an anonymous
function.
'''

n=[6,15,24,39,45,30,75,105,115]

x=list(filter(lambda i:(i%15==0),n))
print("Numbers divisible by fifteen are :",x)