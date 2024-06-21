# 3. Write a python program to accept mobile number and validate it. it should contain exactly 10 digits.
import re
n = input("Enter a mobile number: ")
m = re.search("[0-9]{10}",n)
if m!=None:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
