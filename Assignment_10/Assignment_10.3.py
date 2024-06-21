# Accept 2 patterns from user
# Accept multiple strings from user till user enters end, if string has pattern 1 then store it in list1
# If it has pattern 2 then store it in list 2 else display message pattern not found

import re

print("Format: Rating, Movie Name, Year, Actor/Actress, Mobile Number, City")
strlst=[]
lst1=[]
lst2=[]

while True:
    str1 = input("Enter a string in above format (type end to stop): ")
    if str1.lower() == 'end':
        break
    else:
        strlst.append(str1)

for i in strlst:
    if re.search('\D2018',i) != None:      
        lst1.append(i.split(',')[1])
    if re.search('pune$',i) != None:       
        lst2.append(i.split(',')[1])

print("Pattern 1: Movies released in 2018:",lst1)
print("Pattern 2: Movies released in Pune",lst2)