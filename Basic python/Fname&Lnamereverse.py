'''
@Author: Saba Muttagi
@Date: 2023-07-24
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-25
@Title : Python program which accepts the user's first and last name and print them in
reverse order with a space between them.
'''
Firstname=input("Enter Firstname: ")
Lastname=input("Enter Lastname: ")

def my_func(Firstname,Lastname):
 print("User's Firstname & Lastname is: ",Firstname,Lastname) 
my_func(Firstname,Lastname) 


def reverse(Firstname,Lastname):
 reverseofname=Firstname+" "+Lastname
 return reverseofname[::-1]
print("User's Firstname & Lastname in reverse is :",reverse(Firstname,Lastname)) 
reverse(Firstname,Lastname)