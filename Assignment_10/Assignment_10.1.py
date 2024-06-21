# Do the following using Regular Expression:
# 1. accept lines from user and store in a list.
# convert list into dictionary as follows
# {
# “found”:[“this is algorithm”, “this is mid”],
# “not found:[“this is data”,”this is min”]
# }
# store all lines ending with m or mid in a list and assign list to key “found” in dictionary
# otherwise store it in a list and assign it to key not found”

import re

lines = []
while True:
    line = input("Enter a line (type exit to stop): ")
    if line.lower() == 'exit':
        break
    else:
        lines.append(line)

resultD = {"Found":[], "Not Found":[]}

for line in lines:
    if re.search('m$',line) or re.search('mid$',line):
        resultD['Found'].append(line)
    else:
        resultD['Not Found'].append(line)

for k,v in resultD.items():
    print(f"{k} -> {v}")