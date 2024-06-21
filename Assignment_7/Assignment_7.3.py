# 3. Write a menu driven program to practice List functions. Validate input data wherever required.
# Display following menu:
# 1. Accept Data
#   a) add at last position
#   b) add at given position
# 2. Delete data by value
# display message deleted successfully
# or not found
# 3. delete data by position
#   a) delete last element
#   b) delete from particular position
# 4. sort
#   a) ascending
#   b) descending
# 5. reverse
# 6. Print in sorted order without changing original list
# 7. print in reverse order without changing original list
# 8. display data
#   a) normal
#   b) numbered
choice=0

lst = [int(i) for i in input("Enter a list: ").split(" ")]

# Case 1
def acceptData(lst,ch1):
    match ch1:
              case 'a':
                  last = int(input("Enter the value to add: "))
                  lst.append(last)
                  print(lst)
                  return 1
              case 'b':
                  value = int(input("Enter the value to add: "))
                  pos = int(input("Enter the position to add at: "))
                  if pos<=len(lst):
                    lst.insert(pos, value)
                    print(lst)
                    return 2
                  else:
                    return 3
              case _: print("Invalid Case")

# Case 2
def delValue(lst, value):
    if value in lst:
        lst.remove(value)
        print(lst)
        return 1

# Case 3
def delData(lst,ch1):
    match ch1:
              case 'a':
                  lst.pop()
                  print(lst)
                  return 1
              case 'b':
                  pos = int(input("Enter the position to delete from: "))
                  if 0<=pos<=len(lst):
                    lst.remove(lst[pos])
                    print(lst)
                    return 2
                  else:
                    return 3
              case _: print("Invalid Case")

# Case 4
def sortData(lst,ch1):
    match ch1:
              case 'a':
                  lst.sort()
                  print(lst)
                  return 1
              case 'b':
                  lst.sort(reverse=True)
                  print(lst)
                  return 2
              case _: print("Invalid Case")

# Case 5
def revList(lst):
    lst.reverse()
    print(lst)

while choice!=9:
  choice=int(input("""
  1. Accept Data
  2. Delete data by value
  3. Delete data by position
  4. Sort
  5. Reverse
  6. Print in sorted order without changing original list
  7. Print in reverse order without changing original list
  8. Display data
  9. Exit
  Enter Choice: """))

  match choice:
      case 1:
          print("How to accept data")
          ch1=input("""
            a) Add at last position
            b) Add at given position: """)
          x = acceptData(lst,ch1)
          if x==1:
            print("Data added at last position successfully!")
          elif x==2:
            print("Data added at given position successfully!")
          elif x==3:
            print("Index out of range, Please enter a different position")
          else:
            print("Wrong choice!")

      case 2:
          value = int(input("Enter a value to be deleted: "))
          x = delValue(lst, value)
          if x==1:
            print("Data deleted successfully!")
          else:
            print("Element not found")

      case 3:
          print("How to delete data")
          ch1=input("""
            a) From last position
            b) From a given position: """)
          x = delData(lst,ch1)
          if x==1:
            print("Data at last position deleted successfully!")
          elif x==2:
            print("Data at given position deleted successfully!")
          elif x==3:
            print("Index out of range, Please enter a different position")
          else:
            print("Wrong choice!")

      case 4:
          ch1=input("""
            a) Ascending Order
            b) Descending Order """)
          x = sortData(lst,ch1)
          if x==1:
            print("List sorted in ascending order!")
          elif x==2:
            print("List sorted in descending order!")

      case 5:
          revList(lst)
          print("List reversed!")

      case 6:
          print(sorted(lst))
          print("Original list is: ", lst)
          print("List sorted successfully without changing the original list.")

      case 7:
          for i in reversed(lst):
            print(i, end=" ")
          print("\nOriginal list is: ", lst)
          print("List reversed successfully without changing the original list.")
      case 8:
          print("The list is")
          for indx,d in enumerate(lst):
              print (f"({indx}) {d}")

      case 9:
          print("Thank You!")

      case _:
          print("Invalid Choice. Enter again!")