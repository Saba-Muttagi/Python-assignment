
'''
@Author: Saba Muttagi
@Date: 2023-08-01
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-01
@Title : Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''


Sampl_List=['abc','xyz','aba','1221']

count=0
for i in Sampl_List:
   if i[0]==i[len(i)-1] and len(i)>=2: 
      count=count+1
print("count of strings :",count)