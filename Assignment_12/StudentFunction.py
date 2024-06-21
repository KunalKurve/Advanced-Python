#Q2 
#Write a menu driven program to maintain student information. Modify Student class
# created in previous assignment. Add a member gpa in student class, add a function in
# student class to return GPA of a student
# calculateGPA()
# gpa=(1/3)*m1+(1/2)*m2+(1/4)*m3
# Create an array to store Multiple students.
# 1. Display All Student
# 2. Search by id
# 3. Search by name
# 4. calculate GPA of a student
# 5. Exit
class Student:
    def __init__(self, id=0, name="", m1=0, m2=0, m3=0):
        self.__id = id
        self.__name = name
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        self.__gpa = 0
        
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_calculateGPA(self):
        self.__gpa = (1/3)*m1+(1/2)*m2+(1/4)*m3
    
    def displayDetails (self):
        print("\nStudent Details: ")
        print("______________________")
        print("Student Id: ",self.__id)
        print("Name: ",self.__name)
        print("Marks 1: ",self.__m1)
        print("Marks 2: ",self.__m2)
        print("Marks 3: ",self.__m3)
        print("GPA: ",self.__gpa)
    
student=[]
for i in range(2):
    print(f"Enter for Student {i+1}")
    sid = input("Enter ID:")
    sname = input("Enter Name:")
    sm1 = int(input("Enter Marks 1:"))
    sm2 = int(input("Enter Marks 2:"))
    sm3 = int(input("Enter Marks 3:"))
    student.append(Student(sid,sname,sm1,sm2,sm3)) 



# Case 1: Display Allp                                                                                                                                                                                                                                                                                                                                                          

def displayAll():
    for s1 in lst:
        s1.displayDetails()

# Case 2. Search by ID
def searchById():
    pass

# Case 3. Search by Name
def searchByName():
    pass

# Case 4. Calculate GPA
def calculateGPA():
    gpa = (1/3)*Student1.m1+(1/2)*Student1.m2+(1/4)*Student1.m3
    print("GPA =",gpa)

choice = 0
while choice != 5:
    choice = int(input("""
1. Display All Student
2. Search by ID
3. Search by Name
4. Calculate GPA
5. Exit
Enter choice: """))
    match(choice):
        case 1:
            displayAll()

        case 2:
            pass
        case 3:
            pass

        case 4:
            
            calculateGPA()

        case 5:
            print("Thank you for visiting!")

        case _:
            print("Invalis choice. Enter again!")