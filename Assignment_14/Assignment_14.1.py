# Using numpy create a matrix of size 3 by 5. Create another matrix of 5 by 3
# Perform following operations on the matrices
# 1. Display shape of both matrix
# 2. Find matrix multiplication
# 3. Create another matrix of size 3 by 5 using random numbers
# 4. And display addition subtraction and member wise multiplication
# 1. accept numbers from user and store it in a list1 and list2 then convert these list into ndarray
# create list3 and list4 to store numbers and convert it into ndarray
# (list1 and list 2 in one array) (list3 and list 4 in another array)
# combine these 4 arrays into 2D arrays (use stack functions)
# and find memberwise addition,multiplication
# and exponential of first array

import numpy as np

matrix1 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
    ])
matrix2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
    [13,14,15]
    ])

print ("Matrix 1:\n",matrix1)
print ("Matrix 2:\n",matrix2)

# 1. Display shape of both matrix
print("\nShape of Matrix 1:",matrix1.shape)
print("Shape of Matrix 2:",matrix2.shape)

# 2. Find matrix multiplication
print("\nProduct:\n",matrix1.dot(matrix2))

# 3. Create another matrix of size 3 by 5 using random numbers
matrix3 = np.empty((3,5),dtype=int)
print("\nEnter values for 3x5 matrix")
for i in range(3):
    for j in range(5):
        v = int(input(f"Enter value at {i+1},{j+1}: "))
        matrix3[i,j] = v        
print("\nMatrix 3:\n",matrix3)

#4. And display addition subtraction and member wise multiplication
# Addition
print("\nAddition of Matrix 1 and Matrix 3 (3x5):\n",matrix1 + matrix3)
# Subtraction
print("\nSubtraction of Matrix 1 and Matrix 3 (3x5):\n",matrix1 - matrix3)
# Member wise Multiplication
print("\nMember wise Multiplication of Matrix 1 and Matrix 3 (3x5):\n",matrix1 * matrix3)


# 5. accept numbers from user and store it in a list1 and list2 then convert these list into ndarray
# create list3 and list4 to store numbers and convert it into ndarray
# (list1 and list 2 in one array) (list3 and list 4 in another array)
 
lst1 = [int(i) for i in(input("Enter list 1: ")).split(' ')]
lst2 = [int(i) for i in(input("Enter list 2: ")).split(' ')]
lst3 = [int(i) for i in(input("Enter list 3: ")).split(' ')]
lst4 = [int(i) for i in(input("Enter list 4: ")).split(' ')]
# import numpy as np
# lst1 = [10,20,30,40]
# lst2 = [50,60,70,80]
# lst3 = [11,22,33,44]
# lst4 = [55,66,77,88]

arr1 = np.array(lst1)
arr2 = np.array(lst2)
arr3 = np.array(lst3)
arr4 = np.array(lst4)

print("\nNumpy Arrays:")
print(arr1)
print(arr2)
print(arr3)
print(arr4)

arr12 = np.array((arr1,arr2))
arr34 = np.array((arr3,arr4))

print("\nList 1 and List 2 in one array:")
print(arr12)
print("List 3 and List 4 in one array:")
print(arr34)


# 6. combine these 4 arrays into 2D arrays (use stack functions)
arr1234 = np.vstack((arr12,arr34))
print("\nCombined Matrix of all 4:\n",arr1234)
print("\n2D arrays of size:", arr1234.shape)

# 7. Find memberwise addition,multiplication and exponential of first array
# Addition
print("\nMemberwise Addition of combined Matrix:\n",arr1234+arr1234)
#Multiplication
print("\nMemberwise Multiplication of combined Matrix:\n",arr1234*arr1234)
# exponential
print("\nExponential of Matrix:\n",np.exp(arr1))

