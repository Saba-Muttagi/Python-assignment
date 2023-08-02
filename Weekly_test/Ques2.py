
#Loop from 1-100
#if multiple of 3 ,print("buzz")
#if multiple of 5 print("fizz")
#if multiple of 3&5 ,print("Fiz-buzz")


for x in range(1,100):
  if x%3==0 and x%5==0:
   print(x,"fizz-buzz")
  elif x%3==0:
    print(x,"Fizz")
  elif x%5==0 :
   print(x,"buzz")