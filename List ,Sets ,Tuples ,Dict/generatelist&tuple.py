'''
@Author: Saba Muttagi
@Date: 2023-07-25
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-25
@Title : Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

X=input("Enter your data: ")

mylist=X.split(",")
List1=list((X))
print("List :",mylist)

tuple2=X.split(",")
print("Tuple :",tuple(tuple2))

