# -*- coding: utf-8 -*-
"""OOPs-Assignment_12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gzrsh6Qs9HQB-Kghi10e0WwkMFGhW6Dt
"""

# 1. Write a program to maintain student information. For each student store studid, name, m1,
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
  def __init__(self, studid, name, m1, m2, m3):
    self.__name = name
    self.__studid = studid
    self.__m1 = m1
    self.__m2 = m2
    self.__m3 = m3

  def __str__(self):
    return f"Student Id: {self.__studid}\nName: {self.__name}\nM1: {self.__m1}\nM2: {self.__m2}\nM3: {self.__m3}\n"

# name = input("name: ")
# id = input("id: ")
# m1 = input("m1: ")
# m2 = input("m2: ")
# m3 = input("m3: ")

lst1 = []
for i in range(2):
  user = input("Enter Student Id, name, M1, M2, M3: ").split(" ")
  lst1.append(Student(user[0], user[1], user[2], user[3], user[4]))


print("Student Details: \n")
for ob in lst1:
  print(ob)

# 2. Write a menu driven program to maintain student information. Modify Student class
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
  def __init__(self, sid, name, m1, m2, m3):
    self.__name = name
    self.__sid = sid
    self.__m1 = m1
    self.__m2 = m2
    self.__m3 = m3
    self.__gpa = 0

  def get_id(self):
    return self.__sid

  def get_name(self):
    return self.__name

  def set_calculateGPA(self):
      self.__gpa = (1/3)*self.__m1+(1/2)*self.__m2+(1/4)*self.__m3

  def __str__(self):
    if self.__gpa == 0:
      return f"Student Id: {self.__sid}\nName: {self.__name}\nM1: {self.__m1}\nM2: {self.__m2}\nM3: {self.__m3}\n"
    else:
      return f"Student Id: {self.__sid}\nName: {self.__name}\nM1: {self.__m1}\nM2: {self.__m2}\nM3: {self.__m3}\nGPA:{self.__gpa}"


std_lst = []
n = int(input("Enter the total no. of students: "))
for i in range(1):
  user = input("Enter Id, name, M1, M2, M3: ").split(",")
  std_lst.append(Student(int(user[0]), user[1], int(user[2]), int(user[3]), int(user[4])))


def calculateGPA(sid):
  ind, ob = searchbyId(sid)
  if ind != -1:
    ob.set_calculateGPA()
    return ind, ob
  else:
    return -1, None

def displayallStudent():
  # print("Student Details: \n")
  for ob in std_lst:
    print(ob)

def searchbyId(sid):
  for ind, ob in enumerate(std_lst):
    if ob.get_id() == sid:
      return ind, ob
  else:
    return -1, None

def searchbyName(sname):
  for ind, ob in enumerate(std_lst):
    if ob.get_name() == sname:
      return ind, ob
  else:
    return -1, None

ch = 0
while(ch!=5):
  ch = int(input("""Enter your choice
1. Display All Student
2. Search by id
3. Search by name
4. calculate GPA of a student
5. Exit
"""))
  match ch:
    case 1:
      displayallStudent()
    case 2:
      sid = int(input("Enter the id of student. "))
      ind, ob = searchbyId(sid)
      if ind != -1:
        print(ob)
      else:
        print("Student not found.")
    case 3:
      sname = input("Enter the name of student. ")
      ind, ob = searchbyName(sname)
      if ind != -1:
        print(ob)
      else:
        print("Student not found.")
    case 4:
      sid = int(input("Enter the id of student. "))
      ind, ob = calculateGPA(sid)
      if ind != -1:
        print(ob)
      else:
        print("Student not found.")
    case 5:
      print("Thank you for visiting. ")
    case _:
      print("Wrong choice.")

# Q3. Write a python program to store information of your friends
# id,name,lastname,hobbies,mobno,email,bdate,address
# note: hobbies- a friend may have multiple hobbies

# Accept all friends details and store it in an array
# And do the following.
# 1. Display All Friend
# 2. Search by id
# 3. Search by name
# 4. Display all friend with a particular hobby
# 5. Exit

class friends:

  def __init__(self, id=0, name = '', lastname='', mobno=1234567890, email='', bdate=221199, address='', hobbies = ['']):
    self.__id = id
    self.__name = name
    self.__lastname = lastname
    self.__mobno = mobno
    self.__email = email
    self.__bdate = bdate
    self.__address = address
    self.__hobbies = hobbies

  def __str__(self):
    return f"Friend id: {self.__id},\n Name: {self.__name},\n Lastname: {self.__lastname},\n mobno: {self.__mobno},\n email: {self.__email},\n Bdate: {self.__bdate},\n Address: {self.__address},\n Hobbies: {self.__hobbies}"

  def get_id(self):
    return self.__id

  def get_name(self):
    return self.__name

  def get_lastname(self):
    return self.__lastname

  def get_hobbies(self):
    return self.__hobbies


FriendList = [friends(1, "Kunal", "Kurve", 987654321, "kk@gmail.com", 221199, "Gondia", ['Music', 'Movies']),
              friends(2, "Manasi", "Malge", 123564341, "manasi@gmail.com",100200, "Nagpur", ['Dance', 'NDA']),
              friends(3, "Yogesh", "Siral", 1235643343, "yogi@gmail.com",040400, "Parbhani", ['Coding', 'Travel']),
              friends(4, "Kunal", "Ukey", 123564546, "kunal@gmail.com",290200, "Gondia", ['Cube', 'Coding'])
              ]

def displayallFriends():
  print("Friends Details: \n")
  for ob in FriendList:
    friend = ob.__str__()
    print(friend)


def findFriendsbyHobby(hobby):
  lst = []
  for ind, ob in enumerate(FriendList):
    if hobby in ob.get_hobbies():
      lst.append(ob)
  else:
    if lst == []:
      print("Nobody in Your Friends Has This Hobby")
  for ob1 in lst:
    print(ob1)


def searchbyId(fid):
  for ind, ob in enumerate(FriendList):
    if ob.get_id() == fid:
      return ind, ob
  return -1, None

def searchbyName(fname, flastname):
  for ind, ob in enumerate(FriendList):
    if ob.get_name() == fname and  ob.get_lastname() == flastname:
      return ind, ob
  return -1, None


ch = 0
while(ch!=5):
  ch = int(input("""\nEnter your choice
# 1. Display All Friend
# 2. Search by id
# 3. Search by name
# 4. Display all friend with a particular hobby
# 5. Exit
"""))
  match ch:
    case 1:
      displayallFriends()


    case 2:
      fid = int(input("Enter the id of friend. "))
      ind, ob = searchbyId(fid)
      if ind != -1:
        print(ob)
      else:
        print("Friend not found.")


    case 3:
      fname = input("Enter the name of friend in Camel case ")
      flastname = input("Enter the last name of friend in Camel case ")
      ind, ob = searchbyName(fname,flastname)
      if ind != -1:
        print(ob)
      else:
        print("Friend not found.")


    case 4:
      hobby = input("Enter the hobby to find friends by ")
      findFriendsbyHobby(hobby)

    case 5:
      print("Thank you for visiting. ")


    case _:
      print("Wrong choice.")

#Q4. Design a class hierarchy to maintain information for ABCTel telecom company , company wants to maintain information of customers and vendors.
# For vendors they want to store vendorid, name, email, phone number,list of products they supply
# For customers they want to store custid, name, email, credit class(based on credit history), discounts, plan assigned to customer
# Customer may be Individual or a company
# For individual customer, system should store phone number
# For a customer of type Company, system should store info about relationship manager, credit line, extensions, list of numbers

class ABCTelClients:
  def __init__(self, id=0, name = '', email=''):
    self.__id = id
    self.__name = name
    self.__email = email

  def __str__(self):
    return f"Company id: {self.__id},\n Name: {self.__name},\n email: {self.__email}"

  def get_id(self):
    return self.__id

  def get_name(self):
    return self.__name

  def get_email(self):
    return self.__email

class Vendor(ABCTelClients):
  def __init__(self, vendorid=0, name = '', email='', mobno=1234567890,  products = ['']):
    super().__init__()
    self.__mobno = mobno
    self.__products = products

  def __str__(self):
    return f"Vendor id: {self.__vendorid},\n Name: {self.__name},\n mobno: {self.__mobno},\n email: {self.__email},\n Products: {self.__products}"

  # def get_vendorid(self):
  #   return self.__vendorid

  def get_mobno(self):
    return self.__mobno

  def get_products(self):
    return self.__products

class Customer(ABCTelClients):
  def __init__(self, id=0, name = '', email='', creditclass='', discounts = 0, plan = 0):
    super().__init__()
    self.__creditclass = creditclass
    self.__discounts = discounts
    self.__plan = plan

  def __str__(self):
    return f"Customer id: {self.__id},\n Name: {self.__name},\n email: {self.__email},\n Credit Class: {self.__creditclass},\n Discounts : {self.__discounts}, \n Plan : {self.__plan}"

  # def get_custid(self):
  #   return self.__custid

  def get_creditclass(self):
    return self.__creditclass

class IndiCustomer(Customer):
  def __init__(self, id=0, name = '', email='', creditclass='', discounts = 0, plan = 0, mobno = 1234567890):
    super().__init__()
    self.__mobno = mobno

  def __str__(self):
    return f"Customer id: {self.__id},\n Name: {self.__name},\n email: {self.__email},\n Credit Class: {self.__creditclass},\n Discounts : {self.__discounts},\n Plan : {self.__plan}, \n Mobile Number: {self.__mobno}"

  # def get_custid(self):
  #   return self.__custid

  def get_mobno(self):
    return self.__mobno


class CompanyCustomer(Customer):
  def __init__(self, id=0, name = '', email='', creditclass='', discounts = 0, plan = 0, relationmanager='', creditline=100000, extensions=0, listOfNumbers = []):
    super().__init__()
    self.__creditline= creditline
    self.__extensions= extensions
    self.__listOfNumbers = listofNumbers
    self.__relationManager = relationManager

  def __str__(self):
    return f"Customer id: {self.__id},\n Name: {self.__name},\n email: {self.__email},\n Credit Class: {self.__creditclass},\n relationmanager={self.__relationmanager},\n creditline={self.__creditline},\n extensions: {self.__extensions},\n listOfNumbers = {self.__listOfNumbers}"

  # def get_custid(self):
  #   return self.__custid

  def get_creditline(self):
    return self.__creditline

  def get_extensions(self):
    return self.__extensions

  def get_listOfNumbers(self):
    return self.__listOfNumbers

  def get_relationManager(self):
    return self.__relationManager


def __init__ = "__main__":
  ob = Vendor(vendorid=1, name = 'SS', email='SS@gmail.com', mobno=1234567890,  products = ['TV'])
  ob1 = CompanyCustomer(id=45, name = 'DFE', email='dfe@gmail.com', creditclass='W', discounts = 10, plan = 111000, relationmanager='Plpl', creditline=100000, extensions=0, listOfNumbers = [1,161,5151])
  ob1 = CompanyCustomer(id=45, name = 'DFE', email='dfe@gmail.com', creditclass='W', discounts = 10, plan = 111000, relationmanager='Plpl', creditline=100000, extensions=0, listOfNumbers = [1,161,5151])
  ob2 = IndiCustomer( id=867, name = 'dgd', email='', creditclass='jg', discounts = 20, plan = 12.420, mobno = 1234567890)