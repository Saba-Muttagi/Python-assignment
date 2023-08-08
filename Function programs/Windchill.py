
'''
@Author: Saba Muttagi
@Date: 2023-08-08
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-08
@Title :A program WindChill.java that takes two double command-line
arguments t and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature (the wind
chill) to be:
Note: the formula is not valid if t is larger than 50 in absolute value or if
v is larger
than 120 or less than 3 (you may assume that the values you get are in
that range)'''



import math

t=float(input("Enter temperature 't' (in Fahrenheit): "))
v=float(input("Enter wind speed 'v' (in miles/hour): "))

def windchill(t,v):
  if t<=50 and 3<v<120:
   W=13.12+(0.6215*t)-(11.37*math.pow(v,0.16))+(0.3965*t*math.pow(v,0.16))
   return W
  else:
    print("Values out of range..!!")
print("The Windchill is :",(windchill(t,v)))

print("Rounding off the value of Windchill is :",int(round(windchill(t,v))))