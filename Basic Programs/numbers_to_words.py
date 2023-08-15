
'''
@Author: Saba Muttagi
@Date: 2023-08-15
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-15
@Title : Python program when you give number from terminal it should gives you that
number in letters (1 to 10)(one to ten )

# num = int(input(“Enter the number : )) # 4, 5 --> Four , Five
'''


num=input("Enter the number :")
d={"1":"One" ,"2":"Two" ,"3":"Three" ,"4":"Four" ,"5":"Five" ,"6":"Six" ,"7":"Seven" , "8":"Eight" ,"9":"Nine" ,"10":"Ten"}

for i in num:
  if i in d.keys():
    num=num.replace(i,d[i])
print(num) 