'''
@Author: Saba Muttagi
@Date: 2023-07-23
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-23
@Title : Python program that accepts a word from the user and reverses it.
'''

def reverse(word):
    word=word[::-1]
    return word
word=input("Enter a word:")
print("The original word is:",word)
#print(word)
print("The reversed string is:",reverse(word))
#print(reverse(word))


                #OR

A=input("Enter a word:")
x=A[::-1]
print("Reversed word is:",x)
