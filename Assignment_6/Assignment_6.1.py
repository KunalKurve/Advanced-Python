# 7. Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.
lst1=[int(i) for i in input("Enter the elements in list 1: ").split(" ")]
lst2=[int(i) for i in input("Enter the elements in list 2: ").split(" ")]

print("List 1")
print(lst1)
print("List 2")
print(lst2)

def overlapping(lst1, lst2):
  for i in lst1:
    for j in lst2:
      if i == j:
        print("Common Element found")
        return True
  else:
    print("No Common Element Found")
    return False

a = overlapping(lst1, lst2)
print(a)