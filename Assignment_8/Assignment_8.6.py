# 6. Rename key city to location in the following dictionary

# sampleDict = {
# "name": "Kelly",
# "age":25,
# "salary": 8000,
# "city": "New york"
# }
# Expected output:

# {
# "name": "Kelly",
# "age":25,
# "salary": 8000,
# "location": "New york"
# }

GivenDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
 
# printing initial json
print("Initial 1st dictionary", GivenDict)
 
# changing keys of dictionary
GivenDict['location'] = GivenDict['city']
del GivenDict['city']
 
 
# printing final result
print("Final dictionary", str(GivenDict))