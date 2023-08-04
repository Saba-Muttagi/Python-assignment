
'''
@Author: Saba Muttagi
@Date: 2023-07-31
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-31
@Title :Python program to display formatted text (width=50) as output
'''

import textwrap

text="Program to display the given text in formatted text"
y=textwrap.fill(text,width=50)
print("Formatted text :",y)