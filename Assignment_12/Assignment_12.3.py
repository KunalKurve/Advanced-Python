# Write a python program to store information of your friends
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

  def get_hobbies(self):
    return self.__hobbies


FriendList = [friends(1, "Kunal", "Kurve", 987654321, "kk@gmail.com", 221199, "Gondia", ['Music', 'Movies']),
              friends(2, "Manasi", "Malge", 123564341, "manasi@gmail.com",120400, "Nagpur", ['Dance', 'NDA']),
              friends(3, "Yogesh", "Siral", 1235643343, "yogi@gmail.com",210500, "Parbhani", ['Coding', 'Travel']),
              friends(4, "Kunal", "Ukey", 123564546, "kunal@gmail.com",120200, "Gondia", ['Cube', 'Coding'])
              ]

def displayallFriends():
  print("Friends Details: \n")
  for ob in FriendList:
    friend = ob.__str__()
    print(friend)


def findFriendsbyHobby(hobby):
  for ind, ob in enumerate(FriendList):
    if hobby in ob.get_hobbies():
      print(ob.__str__())
      return ind, ob
    else:
      return -1, None


def searchbyId(fid):
  for ind, ob in enumerate(FriendList):
    if ob.get_id() == fid:
      return ind, ob
  return -1, None

def searchbyName(fname):
  for ind, ob in enumerate(FriendList):
    if ob.get_name() == fname:
      return ind, ob
    else:
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
      ind, ob = searchbyName(fname)
      if ind != -1:
        print(ob)
      else:
        print("Friend not found.")


    case 4:
      hobby = input("Enter the hobby to find friends by ")
      ind, ob = findFriendsbyHobby(hobby)
      if ind != -1:
        print(ob)
      else:
        print("Hobby not found.")


    case 5:
      print("Thank you for visiting. ")


    case _:
      print("Wrong choice.")