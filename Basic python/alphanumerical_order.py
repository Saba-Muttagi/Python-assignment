
'''
@Author: Saba Muttagi
@Date: 2023-07-31
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-31
@Title :Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white
'''


thestr=input("Enter a sequence of words :")
i=thestr.split(",")
print(i)

j=list(set(i))
j.sort()
print(j)