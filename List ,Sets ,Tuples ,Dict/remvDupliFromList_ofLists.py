
'''
@Author: Saba Muttagi
@Date: 2023-07-30
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-30
@Title :Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
'''


thisList=[[10,20],[40],[30,56,25],[10,20],[33],[40]]

#converting the inner lists to tuples so they are hashable
setB = set(tuple(x) for x in thisList)
A = [ list(x) for x in setB ]
A.sort()
print("New List :",A)