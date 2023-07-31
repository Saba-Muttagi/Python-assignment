
'''
@Author: Saba Muttagi
@Date: 2023-07-31
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-31
@Title : Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''

x=str(input("Enter a string :"))

if len(x)<3:
    print(x)
elif len(x)==3:
    print(x+"ing")
elif x[-3:]=='ing':
    print(x+"ly")