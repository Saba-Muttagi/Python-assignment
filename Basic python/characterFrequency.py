
'''
@Author: Saba Muttagi
@Date: 2023-07-26
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-22
@Title : Python program to count the number of characters (character frequency) in a string
'''


string="google.com"
#string=input("Enter string:")
dict={}

for i in string:
  if i in dict:
    dict[i]+=1
  else:
    dict[i]=1  
print("Character frequency: "+str(dict))