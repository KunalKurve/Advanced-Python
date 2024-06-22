"""
Assignment_3_Strings
Assignment by: 
Kunal Kurve (PRN: 240340128012)
Manasi Malge(PRN:240340128013)
"""

"""
1. Write a program that asks the user how many days are in a month,
and what day of the week the month begins on (0 for Monday, 1 for Tuesday, etc),
and then prints a calendar for that month.
"""

while True:
  numday=int(input("Enter Days: "))
  if 28<=numday<=31:
    break
startday=int(input("Enter Start day (0-6): "))
print("Mon\tTue\tWed\tThu\tFri\tSat\tSun")
print("\t"*startday, end="")
count=startday
for i in range(1, numday+1):
  print(" "+str(i), end="\t")
  count = count + 1
  if count==7:
    print()
    count=0

#2.Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.

num_list=[]
n=int(input("enter range"))
for i in range(n):
  num = int(input("enter numbers"))
  num_list.append(num)
for i in range(n):
  print("*"*num_list[i])

"""
Q3. Write a version of a palindrome recognizer that also accepts phrase palindromes such as
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a
potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed
under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!".
Note that punctuation, capitalization, and spacing are usually ignored.
"""
import re
str = input()
str= str.casefold()
x = re.sub(r'\W+', '', str)
for i in range(len(x)//2):
  if x[i]==x[len(x)-i-1]:
    print("String is a Palindrome")
    break
  else :
    print("String is not a Palindrome")
    break

"""
Q4. A pangram is a sentence that contains all the letters of the English alphabet at least once, for
example: The quick brown fox, jumps over the lazy dog!!!!.
Your task here is to write a function to check a sentence to see if it is a pangram or not.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
input_string = "The quick brown fox, jumps over the lazy dog"
for i in alphabet:
  x = input_string.find(i)
  if x == -1:
    print("It's not a panagram")
    break
else:
  print("It's a panagram")

"""
Q5. Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's
language").
That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string "tothohisos isos fofunon".
"""

vowels = "aeiouAEIOU "
user_input = input("Enter a string: ")
for i in user_input:
  x = vowels.find(i)
  print(i+"o"+i, end="") if x== -1  else print(i, end="")

"""
Q6. Write a program that contains a function that has one parameter, n, representing an integer
greater than 0. The function should return n! (n factorial). Then write a main function that calls
this function with the values 1 through 20, one at a time, printing the returned results. This is
what your output should look like:
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
10 628800
"""

def fact(n):
  if n==1 or n==0:
    return 1
  return n*fact(n-1)

user_input = int(input("Enter a number: "))
for i in range(1, user_input):
  print(i, fact(i))

"""
Q7. Write a recursive sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer x ≥ 1:
  1, if x = 1
  x + sum from 1 to x-1 if x > 1
Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
def sum(x):
  # you complete this function recursively
def main():
  # compute and print 1 + 2 + ... + 10
  print(sum(10))
  main()
"""

def add(n):
  if n == 1 or n==0:
    return n
  return n + add(n-1)

user_input = int(input("Enter a number: "))
print(add(user_input))