# Q1
# Write a program to maintain student information. For each student store studid, name, m1,
# m2 and m3 (marks of 3 subjects ). Accept information for 2 students and display it as
# follows.
# Student Details:
# ____________
# Student Id
# Name: Divya
# M1 : 78
# M2: 86
# M3: 89
class Student:
    def __init__(self, id=0, name="", m1=0, m2=0, m3=0):
        self.__id = id
        self.__name = name
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        
    def displayDetails (self):
        print("\nStudent Details: ")
        print("______________________")
        print("Student Id: ",self.__id)
        print("Name: ",self.__name)
        print("Marks 1: ",self.__m1)
        print("Marks 2: ",self.__m2)
        print("Marks 3: ",self.__m3)
        print("______________________")
    
student=[]
for i in range(2):
    print(f"Enter for Student {i+1}")
    sid = input("Enter ID:")
    sname = input("Enter Name:")
    sm1 = int(input("Enter Marks 1:"))
    sm2 = int(input("Enter Marks 2:"))
    sm3 = int(input("Enter Marks 3:"))
    student.append(Student(sid,sname,sm1,sm2,sm3))   
    
    
print("Student Details: \n")
for ob in student:
  print(ob.displayDetails())
            