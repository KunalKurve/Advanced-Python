# Write a python program to accept category from user, display all products of the given category
# Example
# if category given is chips then use regular expression :chips:
# if category given is chips then use regular expression :snack:
# generate pattern :<givencategory name>: and use it for finding lines of the given category

import os
import re
from functools import reduce

strlst = []
if os.path.exists(r'D:\AdvMar2024\Assignment_11\productdata.txt'):
  with open(r'D:\AdvMar2024\Assignment_11\productdata.txt','r') as fh1:
    for ln in fh1:
        strlst.append(ln.rstrip('\n').split(':'))    
else:
    print("File not found")

category = input("Enter category of product: ").lower()
for c in strlst:
  if re.search(f"{[category]}",c) != None:
    print(c[1])