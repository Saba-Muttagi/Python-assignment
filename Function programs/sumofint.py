'''
@Author: Saba Muttagi
@Date: 2023-08-06
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-06
@Title :Sum of three Integer adds to ZERO

a. Desc -> A program with cubic running time. Read in N integers and
counts the
number of triples that sum to exactly 0. b. I/P -> N number of integer, and N integer input array
c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
d. O/P -> One Output is number of distinct triplets as well as the second
output is to
print the distinct triplets'''



#creating empty list
L1=[]

A=int(input("Enter the Number of elements:"))
#creating a list for elements
for i in range(0,A):
   l=int(input())
   L1.append(l)
print("Elements in the list are : ",L1)
print("The Distinct triplets are :")



n=len(L1)
def createArray(L1,n):
 cnt=0;
 for i in range(0,n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
       if (L1[i]+L1[j]+L1[k]==0):
        print(L1[i],L1[j],L1[k])
        cnt+=1;
 return cnt;
print("Count of distinct triplets are : ",createArray(L1,n))
#createArray(L1,n)

