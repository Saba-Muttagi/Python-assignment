
'''
@Author: Saba Muttagi
@Date: 2023-07-29
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-29
@Title :Python program to find common items from two lists
'''

#declaring 2 Lists
a=[2,4,6,8,10,12,14,16,18,20]
b=[3,6,7,12,13,16,19]

#converting list into set
setA=set(a)
setB=set(b)
print("setA =",setA)
print("setB =",setB)

#Finding common items in sets
setC=setA.intersection(setB)
print("setC =",setC)

#coverting Resultant-set back into list
c=list(setC)
print("Common items are :",c)