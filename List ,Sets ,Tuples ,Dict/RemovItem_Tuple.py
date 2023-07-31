
'''
@Author: Saba Muttagi
@Date: 2023-07-31
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-31
@Title : Python program to remove an item from a tuple.
'''

the_tuple=("circle","square","star","triangle","eclipse")
print(the_tuple)

the_list=list(the_tuple)
print(the_list)

the_list.remove("star")
print(the_list)

the_tuple=tuple(the_list)
print(the_tuple)