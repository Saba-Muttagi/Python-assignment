
'''
@Author: Saba Muttagi
@Date: 2023-08-12
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-12
@Title :Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''

from datetime import date

def num_ofDays(date1,date2):
  if date2>date1:
    return(date2-date1).days
  else:
    return(date1-date2).days
    
date1=date(2014, 7, 2)
date2=date(2014, 7, 11)
print("Number of days is:",num_ofDays(date1,date2),"days")