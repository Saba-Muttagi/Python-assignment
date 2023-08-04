
'''
@Author: Saba Muttagi
@Date: 2023-08-03
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-03
@Title :Python program to count number of items in a dictionary value
that is a list.
'''

dict =  {'Days': ['monday', 'tuesday', 'friday'], 'Time':'2pm','Subjects': ['M1', 'english']}
ctr = sum(map(len, dict.values()))
print(ctr)