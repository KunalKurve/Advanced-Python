# Write a python program to accept mobile number and validate it. it should contain exactly 10 digits. (use regularexpression---→ \d{10} -- it will match 10 digit number

import re
n = input("Enter a mobile number: ")
m = re.search("^\d{10}$",n)
if m!=None:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")