
'''
@Author: Saba Muttagi
@Date: 2023-07-27
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-27
@Title : Python program to multiplies all the items in a list
'''

mlist=[2,3,4,5]

def mulof_items(x):
    a=1
    for i in x:
        a=a*i
    return a
print("multiple of list :" ,mulof_items(mlist))