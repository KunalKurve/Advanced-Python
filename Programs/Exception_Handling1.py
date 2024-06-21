# Base class (Pre-Built): Exception
# Child classes: Value Error, Key Error, Type Error 
# Keyword: try, except, raise, finally, else
# try: add statements that can give an error
# except: handles error
# raise: if the program detects an error we explicitly raise an exception message using an object.
# finally: it gets executed after try and except block regardless the exception
# else: it is executed when there is no exception

class WrongChoiceError(Exception):
    def __init__(self,msg="Error"):
        self.__msg=msg
    def __str__(self):
        return self.__msg
while True:   
    try:
        num=34
        n=int(input("Enter Number: "))
        if n==num:
            print("You guessed the number!")
            break
        else:
            raise WrongChoiceError("You lost the attempt. Please guess again!")
    except WrongChoiceError as e:
        print(e)