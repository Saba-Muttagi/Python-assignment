
'''
@Author: Saba Muttagi
@Date: 2023-08-03
@Last Modified by: Saba Muttagi
@Last Modified : 2023-08-03
@Title :Python script to sort (ascending and descending) a dictionary by
value.
'''

import operator

d={1:22  ,3:11 ,5:43 ,2:61 ,0:40 }
print('Original dictionary : ',d)
sorted_d =dict(sorted(d.items(), key=operator.itemgetter(1)))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)