# 7. Generate a list of lists (NOTE: List should get generated dynamically)
# Accept a number from user and check last digit of the number.
# If it is 1 then add it in the list at 1st position.
# If 0 then it should get added at list in 0th position.
# e.g list should look as follows
# [[10],[51],[52]]
# [[10,30,20,40],[11,31,41,31],[22,32,42]....]
# if user enters 15 then the resultant list should be
# [[10,30,20,40],[11,31,41,31],[22,32,42],[],[],[15]]

#Initilize list of list
lst1=[[] for i in range(10)]   # digits : 0-9 , so range is 10
x=False
while x!=True:
  num = int(input("Enter a number : "))
  d=num%10
  if num!=-1:
    lst1[d].append(num)
    x=False
  else:
    x=True
print(lst1)