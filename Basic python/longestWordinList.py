
'''
@Author: Saba Muttagi
@Date: 2023-07-31
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-31
@Title :Python function that takes a list of words and returns the length of the longest
one.
'''

WordsList=input("Enter list of words :")
List_ofWords=str(WordsList)

words=List_ofWords.split(",")
longest_word=max(words,key=len)
print("Longest word is:",longest_word)
Length=len(longest_word)
print("Length of Longest word is :",Length)