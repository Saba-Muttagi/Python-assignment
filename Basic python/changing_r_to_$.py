
'''
@Author: Saba Muttagi
@Date: 2023-07-31
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-31
@Title :Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''

this_string="restart"
print("The original string is :",str(this_string))

x='$'
y=this_string.replace(this_string[0],x).replace(x,this_string[0],1)
print("Replaced string is :"+str(y))