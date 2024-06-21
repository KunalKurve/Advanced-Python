# 4. Write a python program to accept user name and password and validate it. username
# should contain only alphabets or digits and password length should be 8, starts with
# alphabet and should contain at least one special character(#,@) .
# accept username and password from user and validate it. if it is valid then display message
# welcome to our application. otherwise ask to re-enter.
# (allows maximum 3 attempts to accept password

import re

def validName(uname):
    return bool(re.match("[a-zA-Z0-9]+$",uname))

def validPassword(psw):
    return bool(re.match("[a-zA-Z][a-zA-Z0-9#@]{7}$",psw))

attempt = 3
while attempt > 0:
    uname = input("Enter Name: ")
    psw = input("Enter Password: ")

    if validName(uname) and validPassword(psw):
        print("Valid Credentials")
        break
    else:
        print("Invalid Credentials. Enter again.")
        attempt = attempt-1

    if attempt == 0:
        print("You have exceeded the limit to enter credentials!")
