
'''
@Author: Saba Muttagi
@Date: 2023-08-08
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-08
@Title :Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

N=input("Enter data :")
L=N.split(",")
ls=list(L)
print(L)

i=input("Enter 'i' :")

while i in N:
    print(True)
    break
else:
    print(False)