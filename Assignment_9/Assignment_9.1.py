# 1. write a regex to get only the part of the email before the "@" sign excluding the "@" sign.
# example myemail@google.com o/p myemail

import re
s = "myemail@google.com"
m= re.search("\w+",s,re.I)
print(m.group())