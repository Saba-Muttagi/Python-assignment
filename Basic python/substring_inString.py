
'''
@Author: Saba Muttagi
@Date: 2023-07-31
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-31
@Title :Python program to count occurrences of a substring in a string
'''


string_1=input("Enter string :")
substr=input("enter substring :")

'''string_1='dcaabcbaabcaabcceabccfabc'
substr='abc' '''

if substr in string_1:
  print(substr)
  print("Occurence of substring in string :",string_1.count(substr))