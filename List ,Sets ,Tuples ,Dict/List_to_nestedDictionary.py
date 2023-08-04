
'''
@Author: Saba Muttagi
@Date: 2023-08-03
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-03
@Title :Python program to convert a list into a nested dictionary of keys.
'''

listofNum = [20,35,50,65,80]
thedict = current = {}
for num in listofNum:
    current[num] = {}
    current = current[num]
print(thedict)