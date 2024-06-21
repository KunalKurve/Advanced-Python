# 8. Create a list to store strings in a list in following manner list
# [dxz,axz,bat,rat,cat,pat,bbc,bbm,cbm,....] pat axz
# All list with same character at second position should be consecutive.
# If user adds sat, then the resultant list will be:
# [bat,rat,cat,sat,bbc,bbm,cbm,....]
# If user adds pick, then it should be added at
# [bat,rat,cat,bbc,bbm,cbm,pick]


strlst = input("Enter list of strings : ").split(",")
# strlst = ["bat","rat","cat","bbc","cbm"]
def addStrLst(str1,strlst):
  il=[]
  if not strlst:
    strlst.append(str1)
    print(strlst)
  #converting list elements to single string
  for indx,val in enumerate(strlst):
    if val[1] == str1[1]:
      il.append(indx)
  strlst.insert(max(il)+1, str1)
  print(strlst)


while True:
  str1 = input("Enter a string: ")
  if len(str1) == 3:
    addStrLst(str1, strlst)
  elif str1 == "stop":
    print(strlst)
    break
  else:
    strlst.append(str1)
    print(strlst)