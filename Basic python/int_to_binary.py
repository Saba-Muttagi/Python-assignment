
'''
@Author: Saba Muttagi
@Date: 2023-08-08
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-08
@Title :Python program to convert an integer to binary keep leading zeros.
Sample data : 50
Expected output : 00001100, 0000001100
'''

inte=int(input("Enter int number :"))
print(format(inte,'08b'))
print(format(inte,'010b'))

#or

'''i=int(input("Enter int number :"))
b=bin(i)
print(b)'''