# Q2
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


class Student1:
    def __init__(self, sid=0, sname="", sm1=0, sm2=0, sm3=0):
        self.__sid = sid
        self.__sname = sname
        self.__sm1 = sm1
        self.__sm2 = sm2
        self.__sm3 = sm3
        
    def displayDetails (self):
        print("\nStudent Details: ")
        print("______________________")
        print("Student Id: ",self.__sid)
        print("Name: ",self.__sname)
        print("Marks 1: ",self.__sm1)
        print("Marks 2: ",self.__sm2)
        print("Marks 3: ",self.__sm3)
        print("______________________")
        

            
            