"""
Assignment_4_List
Assignment by: 
Kunal Kurve (PRN: 240340128012)
Manasi Malge(PRN:240340128013)
"""

# 1. Reverse a given list in Python
aList = [100, 200, 300, 400, 500]
aList.reverse()
print(aList)

# 2. Concatenate two lists index-wise
# Given:
list1 = ["M", "na", "i", "Raj"]
list2 = ["y", "me", "s", "esh"]
list3=[]
for i in range(len(list1)):
  list3.append(list1[i]+list2[i])
print(list3)

# 3. Given a Python list of numbers. Turn every item of a list into its square
# aList = [1, 2, 3, 4, 5, 6, 7]
# output:
# [1, 4, 9, 16, 25, 36, 49]
aList = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(aList)):
  aList[i]=aList[i]*aList[i]
print(aList)

# 4. Concatenate two lists in the following order
list1 = ["Hello ", "Welcome "]
list2 = ["Students", "Sir"]
list3=[]
for i in range(len(list1)):
  for j in range(len(list2)):
    list3.append(list1[i]+list2[j])
print(list3)

# 5. Given a two Python list. Iterate both lists simultaneously such that list1 should display item
# in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()
for i in range (len(list1)):
  print(list1[i],"",list2[i])

#6. Remove empty strings from the list of strings

list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
while "" in list1:
  list1.remove("")
print(list1)

#7. Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# 8. Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look
# like the following list


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist = ["h", "i", "j"]
list1[2][1][2].extend(sublist)
print(list1)

# 9. Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only
# update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
n=list1.index(20)
# list1.insert(n,200)
# print(list1)
list1[n]=200
print(list1)

#10. Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
  list1.remove(20)
print(list1)