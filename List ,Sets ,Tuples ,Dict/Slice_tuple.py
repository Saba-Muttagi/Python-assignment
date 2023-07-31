
'''
@Author: Saba Muttagi
@Date: 2023-07-31
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-31
@Title : Python program to slice a tuple
'''

Tuple_X=(9,15,24,30,36,45,53,60,72)
print("the Original tuple is :",Tuple_X)

List_X=list(Tuple_X)
print("Tuple to list is :",List_X)

#Slicing list
X=List_X[2:7]
print("Sliced List is :",X)

Tuple_X=tuple(X)
print("Sliced tuple is :",Tuple_X)