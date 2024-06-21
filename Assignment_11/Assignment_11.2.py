# Create a file productdata.txt, using notepad and add contents in following format
# Id:name:description:category:price
# For example
# 123:lays:very crispy:chips:40
# 124:Good day:very sweet:biscuits:35
# 125:maggi:yummy:snacks:60
# 225:chings:yummy:snacks:65
# 123:nachos:very crispy:chips:120
# a. Write a python program read data from file productdata.txt, copy all the lines starting with 12 and ending with 0 in file myproduct.txt
# (use regular expression ^12.*0$)
# b. Write a python program to find sum of prices for each category
# Example the o/p should be as follows
# Chips-→160
# Biscuits-→35
# Snacks-→125
# (hint : use dictionary)
# c. Write a python program to accept category from user, display all products of the given category

import os
import re
from functools import reduce

strlst = []
if os.path.exists(r'D:\AdvMar2024\Assignment_11\productdata.txt'):
  with open(r'D:\AdvMar2024\Assignment_11\productdata.txt','r') as fh1:
    with open(r'D:\AdvMar2024\Assignment_11\myproduct.txt','w') as fh2:
      for ln in fh1:
        strlst.append(ln.rstrip('\n').split(':'))
        m = re.search('^12.*0$',ln)
        if m!= None:
            fh2.write(ln)
else:
    print("File not found")


# b.    
strd={}
print(strlst) 
for k in strlst:
  if k[3] in strd:  
    strd[k[3]] = int(strd[k[3]]) + int(k[4])
  else: 
    strd[k[3]] = int(k[4])
print(strd)  

# c. Write a python program to accept category from user, display all products of the given category
category = input("Enter category of product: ").lower()
for c in strlst:
  if category == c[3]:
    print(c[1])