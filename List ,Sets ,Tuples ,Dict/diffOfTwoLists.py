
'''
@Author: Saba Muttagi
@Date: 2023-07-29
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-29
@Title : Python program to get the difference between the two lists.
'''

#Declaring two lists
A_List=[5,10,15,20,25,30,35,40]
B_List=[10,25,40]
 
#Converting lists into sets 
A_set=set(A_List)
B_set=set(B_List)
print("ASet =",A_set)
print("BSet =",B_set)

#Finding Difference of Two sets
Diff_set=(A_set)-(B_set)
print("DiffSet =",Diff_set)

#Converting sets back into lists
Diff_List=list(Diff_set)
print("Diff list is =",Diff_List)