# display all the keys with value 200 from the following dictionary.
sampleDict = {'a': 100, 'b': 200, 'c': 300,'d':200}

for k,v in sampleDict.items(): 
  if sampleDict[k] == 200:
    print(k)
