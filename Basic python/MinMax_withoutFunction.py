
'''
@Author: Saba Muttagi
@Date: 2023-08-12
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-12
@Title :Python function to find the maximum and minimum numbers from a sequence of
numbers.
'''

def MaxMin(data):
  largest = data[0]
  smallest = data[0]
  for number in data:
    if number > largest:
      largest = number
    elif number < smallest:
      smallest = number
  return largest,smallest

print(MaxMin([90,4,32,15,-3,26,-12,0,-2,78]))