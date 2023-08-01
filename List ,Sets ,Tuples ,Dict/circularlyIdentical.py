
'''
@Author: Saba Muttagi
@Date: 2023-07-29
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-29
@Title :Python program to check whether two lists are circularly identical.
'''

List_1=[2,4,6,8]
List_2=[4,8,6,2]

List_1.sort()
List_2.sort()

if List_1==List_2:
  print("Identical")
else:
  print("Not identical")