
'''
@Author: Saba Muttagi
@Date: 2023-07-22
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-22
@Title : Python program to count the number of characters (character frequency) in a string
'''
print("Character frequency:")
string="google.com"
#print(string.count("g"))

def myfunc(string):
  for i in string:
    c=string.count(i)
    print(i,c)
myfunc(string)   



    
