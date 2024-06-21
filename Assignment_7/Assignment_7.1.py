# 1. Write a menu driven program to practice String functions
# Design following meu
# a. display characters from even position
# b. display characters from odd position
# c. display length of a string
# d. add a at the end of string length times
# e. exit

str1 = input("Enter the string: ")
choice = 0

chars = [*str1]

# Case 1. Display characters from even position.
def displayFromEven():
  for indx,d in enumerate(chars):
    if indx%2 == 0:
      print(d, end = " ")

# Case 2. Display characters from odd position.
def displayFromOdd():
  for indx,d in enumerate(chars):
    if indx%2 != 0:
      print(d, end = " ")

# Case 4. Add a at the end of string length times.
def addA():
  print(str1 + "a" * len(str1))

while choice != 5:
  choice = int(input("""
  1. Display characters from even position.
  2. Display characters from odd position.
  3. Display length of a string.
  4. Add a at the end of string length times.
  5. Exit
  Enter your Choice:
  """))

  match(choice):
    case 1:
      print("Characters from even positions are:")
      displayFromEven()

    case 2:
      print("Characters from odd positions are:")
      displayFromOdd()

    case 3:
      print("Length of the string is:",len(str1))

    case 4:
      print(" After adding a at the end of string length times:")
      addA()

    case 5:print("Thank You!")

    case _: print("Invalid choice. Enter again")