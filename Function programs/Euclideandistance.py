
'''
@Author: Saba Muttagi
@Date: 2023-08-07
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-07
@Title : Write a program Distance.java that takes two integer command-line
arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin
(0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power
function'''


import numpy as np 

x=int(input("Enter value 'x' :"))
y=int(input("Enter value 'y' :"))

distance=np.sqrt((x*x)+(y*y))

print("Distance :",distance)