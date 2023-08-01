
'''
@Author: Saba Muttagi
@Date: 2023-07-31
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-31
@Title : Python program to find the repeated items of a tuple.
'''

myTuple=(1,3,5,7,9,2,5,3,1,7,8)
dict={}

for i in myTuple:
    if i in dict:
      dict[i]+=1
    else:
      dict[i]=1
print("Repeated items are :"+str(dict))