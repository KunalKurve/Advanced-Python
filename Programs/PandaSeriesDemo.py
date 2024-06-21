import numpy as np
import pandas as pd
print(np.random.randn(5))
s = pd.Series(np.random.randn(5), 
              index=['a', 'b', 'c', 'd', 'e'])  #Default index: 0,1,2,3.....
print(s)
print()
print(s[s<1]) #filter series and display all values which are < 1
print()
print(s[[4,3,1]])
print()
print(s[['e','d','b']])
print()
np.exp(s)



print(s)
print()
print(s+s)
print()
       # b-e   a-d
print(s[1:]+s[:-1])
print(s[:3])  #retrieve rows from 0 to 2
print(s['d']) #this will retrieve the row with index d
#print(s['f']) #it is Key error

d = {'b' : 1, 'a' : 0, 'c' : 2} #dictionary

s1=pd.Series(d) #keys will become index and values will become value
print(s1)

s1=pd.Series(5,index=[1,2,3]) #keys will become index and values will become value
print(s1)

s=pd.Series(['rainy','no rain','sunny'],
        index=['monday','tuesday','wednesday'])
print(s)
print(s['monday']) 
