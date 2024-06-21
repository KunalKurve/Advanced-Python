# 2. Accept lines from user and display only the lines that start with a number or any 2 alphabets
import re

lst1 = [i for i in input("Enter a list: ").split(" ")]
for i in range(len(lst1)):
    m = re.search("^\w{2}",lst1[i],re.I)
    if m!= None:
        print(lst1[i])
    else:
        pass