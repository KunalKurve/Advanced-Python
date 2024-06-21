# 8. Accept name and new salary for a employee, modify salary of the employee. display
# appropriate message if salary modified. or if name not found.
# note : the new salary should be > current salary otherwise show message wrong salary.

GivenDict = {'emp1': {'name': 'Jhon', 'salary': 7500},
             'emp2': {'name': 'Emma', 'salary': 8000},
             'emp3': {'name': 'Brad', 'salary': 6500}}

def modData(name,sal):
    for k,v in GivenDict.items():
        for x,y in v.items():
            if y == name:
                if v['salary'] < sal:
                    v['salary'] = sal
                return 1
            return 2
    return 3

name = input("Enter name to modify: ")
sal = int(input("Enter Salary to modify: "))
x = modData(name,sal)
if x == 1:
    print("Salary found and modified")
elif x == 2:
    print("Salary found but not modified")
else:
    print("Salary not found")
print(GivenDict)












































# # GivenDict = {}

# # Case 1
# def addData():
#     cemp = input("Enter employee: ")
#     cname = input("Enter name to add: ")
#     csal = int(input("Enter Salary to add: ")) 
#     a = GivenDict.get(cemp,-1)
#     print(a)
#     #if key is not there add it
#     if a==-1:
#         GivenDict[cemp]['name']=cname
#         GivenDict[cemp]['salary']=csal
#         return True
#     else:
#         return False

# # Case 2
# def modData(nemp,nsal):
#     if nemp in GivenDict:
#         if nsal > GivenDict.get(nemp).get("salary"):
#                 GivenDict[nemp]['salary']=nsal
#                 return 1
#         return 2
#     return 3


# # Case 3: Display all the values from the given dictionary
# def displayAll():
#     for k,v in GivenDict.items():
#         print(f"{k}---->{v}")


# choice = 0
# while choice != 4:
#     choice = int(input("""
#     1. Add name and salary
#     2. Modify salary
#     3. Display all
#     4. Exit
#     Enter choice: 
# """))
    
#     match choice:
#         case 1:
#             addData()
#             print("Element added successfully")

#         case 2:
#             nemp = input("Enter employee to modify: ")
#             nsal = int(input("Enter Salary to modify: "))
#             x = modData(nemp,nsal)
#             if x == 1:
#                 print("Salary found and modified")
#             elif x == 2:
#                 print("Salary found but not modified")
#             else:
#                 print("Salary not found")
        
#         case 3:
#             displayAll()
#         case 4:
#             print("Thank you")
            
#         case _:
#             print("Invalid choice. Enter again")