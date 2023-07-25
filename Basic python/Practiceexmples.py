
'''
@Author: Saba Muttagi
@Date: 2023-07-23
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-25
@Title : Basic exercise Practice
'''

#Printing hello world
print("Hello,World!")

#indentation
if 1>2:
    print("one is greater than two!")
else:
    print("Less than 2")    

#variables
x=5
y="Hello"
print(x)
print(y)

#creating variables
a=6
b="Smith"
print(a)
print(b)

#changing variable type
x=3
x="Sally"
print(x)


#casting
x=str(4)
y=int(4)
z=float(4)
print(x)
print(y)
print(z)


#getting the type
a=5
b="John"
print(type(a))
print(type(b))


#single/double quotes
x="John"
print(x)
x='John'
print(x)


#case-sensitive
a=4
A="Sally"
print(a)
print(A)

#variable names
myvar="John"
my_var="John"
_my_var="John"
myVar="John"
MYVAR="John"
myvar2="John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#many values to multiple variables
a,b,c="orange","banana","cherry"
print(a)
print(b)
print(c)

#one values to multiple variables
x=y=z="orange"
print(x)
print(y)
print(z)

#Extracting values to variables
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)


#output variables
x="Python is awesome"
print(x)


#output multiple variables
x="Python"
y="is"
z="fantastic"
print(x,y,z)

#(or) '+' for only character
x="Python "
y="is "
z="fantastic "
print(x+y+z)

#(or) '+' for only numbers
x=5
y=17
print(x+y)

#(and) '+' for string & numbers 
#x=6
#y="John"
#print(x+y)


#global variables
x="fantastic"
def myfunc():
 print("Python is "+x)
myfunc() 

#same local variable and global variable name
x="fantastic"
def myfunc():
 x="awesome"
 print("Python is "+x)
myfunc()
print("Python is "+x)

#using global keyword
def myfunc():
 global x
 x="awesome"
myfunc()
print("Python is "+x)

#changing value of a global variable
x="awesome"
def myfunc():
 global x
 x="fantastic"
myfunc()
print("Python is "+x)


#