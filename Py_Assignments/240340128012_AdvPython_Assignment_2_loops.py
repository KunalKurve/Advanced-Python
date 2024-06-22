"""
Assignment_2_Loops
Assignment by: 
Kunal Kurve (PRN: 240340128012)
Manasi Malge(PRN:240340128013)
"""

#1. Accept 10 integers from user and print their average value on the screen
sum=0
for i in range(10):
  a=int(input("Enter Number:"))
  sum=sum+a
avg=sum/10
print("Average=",avg)

#2. Print the following patterns using loop :
""""b.
*
***
*****
***
*"""
n=int(input("Enter height of triangle:"))
for i in range(n):
  print(" "*(n-i), end="")
  print("*"*(2*i+1))
for j in range(n-2, -1, -1):
  print(" "*(n-j), end="")
  print("*"*(2*j+1))

"""c.
1010101
10101
101
1"""
n=int(input("Enter height of triangle:"))
for i in range(n, 0, -1):
  print(" "*(n-i),end="")
  for j in range(0, 2*i-1):
    if j%2 == 0:
      print("1", end="")
    else:
      print("0",end="")
  print()

"""d.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""
n=int(input("Enter Number of rows:"))
for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end="")
  print()

##3. Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
n1=int(input("Enter Number 1:"))
n2=int(input("Enter Number 2:"))
small=min(n1,n2)
for i in range (2,small+1):
  if n1%i==0 and n2%i==0:
    maxnum=i
print(maxnum)

##3. Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
n1=int(input("Enter Number 1:"))
n2=int(input("Enter Number 2:"))

def gcd(n1,n2):
    if(n2==0):
        return n1
    else:
        return gcd(n2,n1%n2)
gcd(n1,n2)

#4. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.
print("""Menu
Enter Integer.
Press q to exit after every integer input.""")
count=0
prod=1
sum=0
flag=True
while flag:
  choice=input("Enter Integer: ")
  match choice:
    case 'q':
      flag=False
    case _:
      count=count+1
      sum=sum+int(choice)
      prod=prod*int(choice)

avg=sum/count
print("Average= ",avg)
print("Product= ",prod)

#5. Given a number count the total number of digits in a number and also find sum of digits of the number.
num=int(input("Enter Number:"))
count=0
sum=0
while num>0:
  sum=sum+num%10
  count=count+1
  num=num//10
print("Number of digits= ",count)
print("Sum of digits= ",sum)

#6. To display the cube of the number upto given an integer. If the given integer is 5, then display cube of 1 to 4.
num=int(input("Enter Number:"))
for i in range(1,num):
  print("Cube of ",i,"=",i*i*i)

#7. Accept 20 numbers from user and display sum of only even numbers.
sum=0
for i in range(0,20):
  num=int(input("Enter Number:"))
  if(num%2==0):
    sum=sum+num
print("Sum of even numbers=",sum)

#8. Ask user number of terms to be generated of a series. generate numbers for the following series and find its addition [9 + 99 + 999 + 9999+........]
prod = 1
sum=0
num=int(input("Enter Number: "))
for i in range(1, num+1):
  prod = 10**i - 1
  sum=sum+prod
  print(prod," ",end="")
#print(".....")
print("\nSum=",sum)

#9. Write a program in python to display the sum of the series [ 1+x+x^2/2!+x^3/3!+....]. Go to the editor

def fact(num):
  if num==1 or num==0:
    return 1
  else:
    return num*fact(num-1)

num=int(input("Enter Number: "))
count=int(input("Enter count: "))
sum=0

for i in range (0,count):
  div=(num**i)/fact(i)
  sum=sum+div

print(sum)

#10. Write a program in python to find the sum of the series [ x - x^3 + x^5 + ......]. Go to the editor
import math
num=int(input("Enter Number: "))
count=int(input("Enter count: "))
sum=0
c=1
for i in range (1,2*count, 2):
  prod=pow(num,i)
  #print(prod)
  if(c%2==0):
    print(f"-{prod}")
    sum=sum-prod
  else:
    print(prod)
    sum=sum+prod
  c=c+1
print("Sum=",sum)