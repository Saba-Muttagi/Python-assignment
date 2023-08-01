
'''
@Author: Saba Muttagi
@Date: 2023-07-29
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-29
@Title : Python function that takes two lists and returns True if they have at
least one common member.
'''



List_A=["pink","grey","red","blue","white"]
List_B=["white","black"]

for i in List_B:
   if i in List_A:
    print(True)
else:
    print(False)