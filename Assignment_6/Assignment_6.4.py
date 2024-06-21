# 10. Define a simple "spelling correction" function correct() that takes a string and sees to it that
# 1) two or more occurrences of the space character is compressed into one, and
# 2) inserts an extra space after a period if the period is directly followed by a letter.
# e.g. correct("This is very funny and cool.Indeed!")
# should return "This is very funny and cool. Indeed!"

# str1=input("Enter string: ")
# def correct(str1):
#   while "  " in str1:
#     str1.replace("  ", " ")
#     print(str1)

# correct("This is  very  funny and cool.Indeed!")


str1=input("Enter String: ")
def correct(str1):
  while "  " in str1:
    str1=str1.replace("  "," ")
  str1=str1.replace(".", ". ")
  print(str1)

correct(str1)