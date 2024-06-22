"""
Assignment_1_If_Statement
Assignment by: 
Kunal Kurve (PRN: 240340128012)
Manasi Malge(PRN:240340128013)
"""

"""
Q1. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
"""

class_total=int(input("Enter the number of classes held: "))
class_attend=int(input("Enter the number of classes attended: "))
percent=(class_attend/class_total)*100    #calculate percentage
print(f"\nAttendence= {percent}%")
if percent>=75:
  print("You are allowed to sit in exam.")
else:
  print("You are not allowed to sit in exam.")

"""
Q2. Accept amount from user and find the minimum number notes required to get the amount
amount =512
Notes: 2000,500,100,50,10,5,2,1
500-1 note
10 - 1 note
2- 1 coin
amount=20550
2000 – 10 note
500 – 1 note
50 -1 note
"""
value = int(input("Amount: "))
print("Number of notes are:")
while(value>0):
  if value>=2000:
    d = value//2000
    print(f"2000: {d} note")
    value = value - 2000*d
  elif value>=500:
    d = value//500
    print(f"500: {d} note")
    value = value - 500*d
  elif value>=100:
    d = value//100
    print(f"100: {d} note")
    value = value - 100*d
  elif value>=50:
    d = value//50
    print(f"50: {d} note")
    value = value - 50*d
  elif value>=10:
    d = value//10
    print(f"10: {d} note")
    value = value - 10*d
  elif value>=5:
    d = value//5
    print(f"5: {d} note")
    value = value - 5*d
  elif value>=2:
    d = value//2
    print(f"2: {d} note")
    value = value - 2*d
  elif value>=1:
    d = value//1
    print(f"1: {d} note")
    value = value - 1*d

"""
Q3. Modify the above question to allow student to sit if he/she has medical cause.
Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.
"""
medical_cause = input("Do you have any medical cause ? (Please respond with 'Y' for yes or 'N' for no): ")
if medical_cause.upper() == 'Y':
    print("You are allowed to sit.")
elif medical_cause.upper() == 'N':
    print("You are not allowed to sit.")
else:
    print("Invalid input. Please respond with 'Y' for yes or 'N' for no.")

"""
Q4. A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
"""
# Ask the user to enter marks
marks = float(input("Enter your marks: "))

# Define the grading system based on the given rules
if marks < 25:
    grade = 'F'
elif 25 <= marks < 45:
    grade = 'E'
elif 45 <= marks < 50:
    grade = 'D'
elif 50 <= marks < 60:
    grade = 'C'
elif 60 <= marks < 80:
    grade = 'B'
else:
    grade = 'A'

# Print the corresponding grade
print("Your grade is:", grade)

"""
Q5. Print the output of following statements
If
x = 2
y = 5
z = 0
then find values of the following expressions:
a. x == 2
b. x != 5
c. x != 5 && y >= 5
d. z != 0 || x == 2
e. !(y < 10)
"""
#Given values of variables
x = 2
y = 5
z = 0

# Evaluating expressions
a = x == 2
b = x != 5
c = x != 5 and y >= 5
d = z != 0 or x == 2
e = not (y < 10)

# Printing the output
print("a. x == 2:", a)
print("b. x != 5:", b)
print("c. x != 5 && y >= 5:", c)
print("d. z != 0 || x == 2:", d)
print("e. !(y < 10):", e)

#Q6. Accept number from user and check whether it is divisible by 5 and 11 if divisible then display appropriate message.

number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print(f"{number} is divisible by both 5 and 11.")
else:
    print(f"{number} is not divisible by both 5 and 11.")

"""
Q7. Write a program to calculate the electricity bill
(accept number of unit from user) according to the following criteria :
Unit Price
First 100 units no charge
Next 100 units Rs 5 per unit
After 200 units Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)
"""
unit = int(input("Enter the numbers of unit consumed."))
if unit<=100:
  print("No charge")
elif 100<unit<=200:
  total_bill = (unit-100)*5
else:
  total_bill = ((unit-200)*10+(100*5))   # calculating bill when units > 200

print("Total bill amount is Rs", total_bill)

#Q8. Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.

num=int(input("Enter Number: "))
last=num%10
if last%3==0:
  print(f"Last digit of {num} is {last} is divisible by 3")
else:
  print(f"Last digit of {num} is {last} is not divisible by 3")

"""
Q9. Write a program to check whether an years is leap year or not
the year is leap if it satisfies following condition
• It the year is divisible by 100
o If it is divisible by 100, then it should also be divisible by 400
then it is leap year

• otherwise, all other years divisible by 4 and not divisible by 100
then it is leap year.
"""
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year.")
else:
  print("It's not a leap year.")

"""
Q10. Write a program to accept the price of a bike and display the road tax and
insurance to be paid according to the following criteria . also display total amount to
be paid.

Cost price (in Rs) Tax Inssurance
> 100000 15 % 20%
> 50000 and <= 100000 10% 8%
<= 50000 5% 5%
"""
price = int(input("Enter the price of bike: "))

if price>100000:
  final_price = price + price*0.15 + price*0.2   # 15% Tax i.e. 0.15 and 20% Insurance i.e. 0.20
elif 100000>= price > 50000:
  final_price = price + price*0.1 + price*0.08  # 10% Tax i.e. 0.10 and 8% Insurance i.e. 0.08
else:
  final_price = price + price*0.1     # 5% Tax i.e. 0.05 and 5% Insurance i.e. 0.05
print(final_price)