
'''
@Author: Saba Muttagi
@Date: 2023-08-07
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-07
@Title :
1. 2D Array
a. Desc -> A library for reading in 2D arrays of integers, doubles, or
booleans from
standard input and printing them out to standard output. b. I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner
Class
c. Logic -> create 2 dimensional array in memory to read in M rows and
N cols
d. O/P -> Print function to print 2 Dimensional Array. In Java use
PrintWriter with
OutputStreamWriter to print the output to the'''


import numpy as np

rows=int(input("Enter the M-row number:"))
colm=int(input("Enter N-col number :"))
print("Dimensions: \n", (rows,colm))  

print("Please Enter elements :")
m= [[(input()) for c in range (colm)] for r in range(rows)]  
print("Elements in list format are :",m)  

matrix = np.array(m).reshape(rows,colm)  
print("Elements in matrix form :\n",matrix)  