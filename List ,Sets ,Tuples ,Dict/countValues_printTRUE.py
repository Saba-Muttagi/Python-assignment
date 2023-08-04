
'''
@Author: Saba Muttagi
@Date: 2023-08-03
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-03
@Title : Python program to count the values associated with key in a
dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True.
'''

Smpl_data= [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

print("The original dictionary : " +  str(Smpl_data))
A=sum(d['success'] for d in Smpl_data)
print("Count of success in dict :",A)





'''dictationary=list(value for dic in Smpl_data for value in dic.values())
print("Unique values(List): ",dictationary)
x=dictationary.count(True)
print(x)'''