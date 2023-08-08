
'''
@Author: Saba Muttagi
@Date: 2023-08-08
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-08
@Title : A program Quadratic.java to find the roots of the equation
a*x*x + b*x + c. Since the equation is x*x, hence there are 2 roots. The 2 roots of the
equation
can be found using a formula (Note: Take a, b and c as input values)
delta = b*b - 4*a*c
Root 1 of x = (-b + sqrt(delta))/(2*a)
Root 2 of x = (-b - sqrt(delta))/(2*a)
'''

from math import sqrt

print("Quadratic function : (a * x^2) + b*x + c")
a=float(input("Enter input value (a!=0) 'a' :"))
b=float(input("Enter input value 'b' :"))
c=float(input("Enter input value 'c' :"))


delta = ((b*b) - (4*a*c))  
print("Delta is :",delta)

if delta > 0:
    no_of_roots = 2
    Root1_x = (((-b) + sqrt(delta))/(2*a))     
    Root2_x = (((-b) - sqrt(delta))/(2*a))
    print("There are 2 roots: %f and %f" % (Root1_x, Root2_x))
elif delta == 0:
    no_of_roots = 1
    x = (-b) / (2*a)
    print("There is one root: ", x)
else:
    no_of_roots = 0
    print("No roots, discriminant < 0.")
    exit()