
'''
@Author: Saba Muttagi
@Date: 2023-08-08
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-08
@Title :Python program to concatenate all elements in a list into a string and return it.
'''

theList=["Concatenating","all","elements","and","return","string"]
print("The original list :",theList)

string=" ".join([str(item) for item in theList])
print("String is :",string)