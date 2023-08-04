
'''
@Author: Saba Muttagi
@Date: 2023-08-03
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-03
@Title :Python program to check multiple keys exists in a dictionary.
'''

student = {
  'name': 'Harry',
  'class': 'VI',
  'roll_id': '6'
}
print(student.keys() >= {'roll_id', 'name'})
print(student.keys() >= {'name','VI'})
print(student.keys() >= {'6', 'class'})