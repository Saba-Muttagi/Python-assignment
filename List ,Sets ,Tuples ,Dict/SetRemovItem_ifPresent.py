
'''
@Author: Saba Muttagi
@Date: 2023-08-01
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-01
@Title : Python program to remove an item from a set if it is present in the set.
'''

fruit_Set={"strawberry","pear","guava","mango","kiwi"}
x=input("Enter a fruit :")

if x in fruit_Set:
    fruit_Set.remove(x)
    print("Fruit removed from set")
    print("New fruit set is :",fruit_Set)
else:
    print("Fruit not present")