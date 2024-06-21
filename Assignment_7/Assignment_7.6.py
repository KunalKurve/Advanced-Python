# 6. Write a menu driven program to practice Set functions.
# Write a program to accept names from users and store it in a set.
# Display the following menu:
# print("""1. delete element if exists otherwise
# do not show any errr""")
# print("2. add a elemet")
# print("3. create one more set")
# print("4. union of 2 sets")
# print("4. intersection of 2 sets")
# print("5. difference of 2 sets")
# print("6. convert set into frozenset")
# print("7. exit")

def delElem(value):
  if value in s:
    ch1 = input("Do you want to delete elemen(y/n): ")
    if(ch1=='y'):
      s.discard(value)
      return 1
    else:
      return 2
  else:
    return 3

def addElem(value):
  if value not in s:
    s.add(value)
    return 1
  else:
    return 2

def unionS(s,s1):
  return s|s1

def intersectS(s,s1):
  return s&s1

def diffOfS(s,s1):
  return s-s1



s=set()
s.update(list(input("Enter list of names:").split(" ")))

ch=-1
while ch!=9:
  ch=int(input('''
      1. Delete element if exists otherwise do not show any error
      2. Add a elemet
      3. Create one more set
      4. Union of 2 sets
      5. Intersection of 2 sets
      6. Difference of 2 sets
      7. Convert set into frozenset
      8. Display set
      9. Exit
    Enter your choice: '''))

  match ch:
    case 1:
      value = input("Enter element to delete: ")
      x=delElem(value)
      if x==1:
        print("Element found and deleted successfully")
      elif x==2:
        print("Element found and not deleted")
      elif x==3:
        print("Element does not exists")

    case 2:
      value = input("Enter element to add: ")
      x=addElem(value)
      if x==1:
        print("Element added successfully")
      elif x==2:
        print("Element already exists")

    case 3:
      s1=set()
      s1.update(list(input("Enter list of names: ").split(",")))

    case 4:
      s2=unionS(s,s1)
      print(f"The union of {s} and {s1} is {s2}")

    case 5:
      s2=intersectS(s,s1)
      print(f"The intersection of {s} and {s1} is {s2}")
    case 6:
      s2=diffOfS(s,s1)
      print(f"The difference of {s} and {s1} is {s2}")
    case 7:
      frozen_set = frozenset(s)
      print("The frozen set is : ",frozen_set)
    case 8:
      print(s)
    case 9:
      print("Thank you!")
    case _:
      print("Invalid Choice. Enter again!")