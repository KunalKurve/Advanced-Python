# 2. Write a program to accept a string from user. Accept a second string from user to search and find all occurrences of in the given string.
str1 = input("Enter the string: ")
word = input("Enter the word to search: ")
c=0
pos = str1.find(word)
while pos!=-1:
  print(f"{word}=",pos)
  pos=str1.find(word,pos+1)
  c=c+1
print("Count=",c)