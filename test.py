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

def delValue(lst, value):
    if value in lst:
        lst.remove(value)
        print(lst)
        return 1
    
def delData(lst,ch1):
    match ch1:
              case 'a': 
                  lst.pop()
                  print(lst)
                  return 1
              case 'b':
                  pos = int(input("Enter the position to delete from: "))
                  if 0<pos<=len(lst):
                    lst.remove(lst[pos])
                    print(lst)
                    return 2
                  else:
                    return 3
              case _: print("Invalid Case")

def sortData(lst,ch1):
    match ch1:
              case 'a': 
                  print(lst.sort())
                  return 1
              case 'b':
                  print(lst.sort(reverse=True))
                  return 2
              case _: print("Invalid Case")

def revList(lst):
    print(reversed(lst))

while choice!=9:
  choice=int(input("""
  1. Accept Data
  2. Delete data by value display message deleted successfully or not found
  3. delete data by position
  4. sort
  5. reverse
  6. Print in sorted order without changing original list
  7. print in reverse order without changing original list
  8. display data
    a) normal
    b) numbered
  9. Exit
  Enter Choice: """))

  match choice:
      case 1:
          print("How to accept data")
          ch1=input("""
            a) add at last position 
            b) add at given position""")
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
            a) from last position 
            b) from a given position""")
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
      
      case 6:
          print(sorted(lst))
          print("List sorted successfully without changing the original list.")
      
      case 7:
          print(reversed(lst))
          print("List reversed successfully without changing the original list.")
      case 8:
          print("The list is")
          for indx,d in enumerate(lst):
              print (f"({indx}) {d}")
      
      case 9:
          print("Thank You!")
          
      case _:
          print("Invalid Choice. Enter again!")