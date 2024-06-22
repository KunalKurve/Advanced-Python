class WrongChoiceError(Exception):
    def __init__(self,msg="error"):
        self.__msg=msg
    def __str__(self):
        return self.__msg
while True:   
    try:
        num=34
        n=int(input("enetr  number"))
        if n==num:
            print("Yepee!!, you guess the number")
            break
        else:
            raise WrongChoiceError("OOPs!, you lost the attempt pls re guess")
    except WrongChoiceError as e:
        print(e)