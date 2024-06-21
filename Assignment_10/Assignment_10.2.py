# accept strings in following format from user and store it in a list:
# 12,queen,2018,kangana,1234562018,pune
# 15,dangal,2018,aamir,34562562018,mumbai
# 12,sholay,1995,amitabh,7869272018,pune
# ---- Display movie name and year separated by, if the movie was released in 2018.
# ---- Display movies released in pune city.

import re

print("Format: Rating, Movie Name, Year, Actor/Actress, Mobile Number, City")
strlst=[]
a1=[]
a2=[]
while True:
    str1 = input("Enter a string in above format (type exit to stop): ")
    if str1.lower() == 'exit':
        break
    else:
        strlst.append(str1)

print(strlst)
for i in strlst:
    if re.search('\D2018',i) != None:       #\D: Anything but digit.
        a1.append(i.split(',')[1])
        #print(f"Movies released in 2018: {i.split(',')[1]}, {i.split(',')[2]}")

    if re.search('pune$',i) != None:
        a2.append(i.split(',')[1])
        # print(f"Movies released in Pune: {i.split(',')[1]}")

print("Movies released in 2018:",a1)
print("Movies released in Pune:",a2)