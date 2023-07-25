'''
@Author: Saba Muttagi
@Date: 2023-07-23
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-23
@Title : Python program to print “Hello” if a number entered by user is multiple of 5
otherwise print “Bye”
'''

#Num = int(input(“Enter the number : )) # 3, 10, 7, 5,15,20
#Bye, Hello, Bye,Hello,Hello,Hello


Num=int(input("Enter the number :"))
if Num%5==0:
    print("Hello") 
else:
    print("Bye")    