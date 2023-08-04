
'''
@Author: Saba Muttagi
@Date: 2023-08-03
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-03
@Title :Python program to print a dictionary in table format.
'''

dict1 = {}
 
# insert data into dictionary
dict1 = {(0, 0): 'Samuel', (0, 1): 23, (0, 2): 'DBMS',
         (1, 0): 'Richie', (1, 1): 21, (1, 2): 'Data Structure',
         (2, 0): 'Lauren', (2, 1): 22, (2, 2): 'OOPS with Java'
         }
 
# print the name of the columns explicitly.
print(" NAME ", " AGE ", "  COURSE ")
 
# Iterate through the dictionary
# to print the data.
for i in range(3):
 for j in range(3):
  print(dict1[(i, j)], end='   ')
 print()