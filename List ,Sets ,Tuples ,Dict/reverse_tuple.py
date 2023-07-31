
'''
@Author: Saba Muttagi
@Date: 2023-07-31
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-31
@Title : Python program to reverse a tuple.
'''

t_tuple=('g','f','e','d','c','b','a')
print("Original tuple is :",t_tuple)

l_list=list(t_tuple)
print("tuple to list is :",l_list)

l_list=l_list[::-1]
print("Reversed list is :",l_list)

t_tuple=tuple(l_list)
print("Reversed tuple is :",t_tuple)