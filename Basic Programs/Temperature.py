'''
@Author: Saba Muttagi
@Date: 2023-07-23
@Last Modified by: Saba Muttagi
@Last Modified : 2023-07-23
@Title : Python program to convert temperatures to and from Celsius and Fahrenheit
'''

"""F = input(“Enter the value of Fahrenheit to convert it into degree celsius : ”) #200
#Convert it to Degree Celsius"""

Fahrenheit=float(input("Enter the value of Fahrenheit to convert it into degree celsius :"))
Celsius=((Fahrenheit-32)*(5/9))
print("Fahrenheit into Celsuis is:",Celsius)



"""C = input(“Enter the value of celsius to convert it into Fahrenheit ”) #50
#Convert it to Fahrenheit"""

Celsius_1=float(input("Enter the value of celsius to convert it into degree Fahrenheit : "))
Fahrenheit_1=(Celsius_1*(9/5))+32;
print("Celsuis into Fahrenheit is :", Fahrenheit_1)