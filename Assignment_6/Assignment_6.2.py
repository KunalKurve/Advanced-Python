# 8. Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
from functools import reduce

lst=[i for i in input("Enter a list of words: ").split(" ")]
lst1=[]
def find_longest_word(lst):
  for i in lst:
    lst1.append(len(i))
  max1=reduce(lambda x,y:x if x>y else y,lst1)
  # return max(lst1)
  return max1

max = find_longest_word(lst)
print("Max= ",max)