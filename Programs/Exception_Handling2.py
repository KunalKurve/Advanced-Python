d={"user1":"pass1","user2":"pass2"}
class InvalidPassordError(Exception):
    def __init__(self,msg):
        self.__msg=msg
    def __str__(self):
        return  self.__msg
    
class InvalidUsernameError(Exception):
    def __init__(self,msg):
        self.__msg=msg
    def __str__(self):
        return  self.__msg
    
for i in range(3):
    try:
        uname=input("Enter Username: ")
        password=input("Enter Password: ")
        v=d.get(uname,-1)
        if v!=-1:
            if v==password:
                print("Valid User!")
                break
            else:
                raise InvalidPassordError("Invalid Credentials!")
        else:
            raise InvalidUsernameError("Please enter Valid Credentials!")
    except InvalidPassordError as e:
        print(e)
    except InvalidUsernameError as e:
        print(e)
else:
    print("Please contact Administrator")