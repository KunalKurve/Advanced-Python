# 9. Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n
lst=[i for i in input("Enter a list of words: ").split(" ")]
n=int(input("Enter integer: "))
def filter_long_words(lst, n):
  lst2=list(filter(lambda x:len(x)>n, lst))
  #print(lst2)
  return lst2

max = filter_long_words(lst, n)
print("Max= ",max)