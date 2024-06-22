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
        uname=input("enetr user name")
        password=input("enter password")
        v=d.get(uname,-1)
        if v!=-1:
            if v==password:
                print("valid user")
                break
            else:
                raise InvalidPassordError("invalid credentials")
        else:
            raise InvalidUsernameError("pls enter valid credentials")
    except InvalidPassordError as e:
        print(e)
    except InvalidUsernameError as e:
        print(e)
else:
    print("pls contact administrator")
    
