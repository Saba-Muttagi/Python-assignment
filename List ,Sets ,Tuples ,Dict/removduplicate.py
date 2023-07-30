
'''
@Author: Saba Muttagi
@Date: 2023-07-29
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-29
@Title : Python program to remove duplicates from a list.
'''

X=["red","blue","purple","grey","red","green","blue"]
X=list(dict.fromkeys(X))
print("New List is : ",X)