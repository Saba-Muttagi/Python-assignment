
'''
@Author: Saba Muttagi
@Date: 2023-07-29
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-29
@Title :Python program to print a specified list after removing the 0th, 4th and
5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''

SmplList=['Red','Green','White','Black','Pink','Yellow']

SmplList.pop(0)
SmplList.pop(4)
SmplList.pop()         #or SmplList.pop(-1)
print("NewList :",SmplList)