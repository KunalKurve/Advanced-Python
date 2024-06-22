"""
Assignment_5_Tuple
Assignment by: 
Kunal Kurve (PRN: 240340128012)
Manasi Malge(PRN:240340128013)
"""

#1. Reverse the following tuple

aTuple = (10, 20, 30, 40, 50,60)
a=[]
for i in range (len(aTuple)-1,-1,-1):
  a.append(aTuple[i])
print(tuple(a))

# 2. display value 20 from the following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])

# 3. Unpack the following tuple into 4 variables
aTuple = (10, 20, 30, 40)
a,b,c,d=aTuple
print(a,b,c,d)

# 4. Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)

temp=tuple1
tuple1=tuple2
tuple2=temp
print(tuple1)
print(tuple2)

# 5. Copy element 44 and 55 from the following tuple into a new tuple

tuple1 = (11, 22, 33, 44, 55, 66)
m=tuple1.index(44)
n=tuple1.index(55)
tuple2=tuple1[m],tuple1[n]
print(tuple2)

#6. Modify the first item (22) of a list inside a following tuple to 200

tuple1 = (11, [22, 33], 44, 55)
a=tuple1[1]
n=a.index(22)
a[n]=200
print(a)
print(tuple1)