# 3. Display the value of key history from the following dictionary
# the value of key ‘history’ from the below dict


sampleDict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}

v = sampleDict.get("class").get("student").get("marks").get("history")

print(v)
