from abc import ABC,abstractmethod

class Account(ABC): 

    cnt=1
    @staticmethod
    def __generatecode(actype):
        acno=actype+str(Account.cnt)
        
        return acno

    def __init__(self, acname="", acbal = 0,acpin = 0, acno = 0,actype='s'):
        self.__acname = acname
        if acno==0:
            self.__acno = Account.__generatecode(actype)
        else:
            self.__acno=acno
        Account.cnt=Account.cnt+1
        
        self.__acbal = acbal
        self.__actype = actype
        self.__acpin = acpin

    def __str__(self):
        return f"Account name : {self.__acname}, Account Type: {self.__actype}, Account no : {self.__acno} , Account Balance : {self.__acbal}"
    
    def get_acname(self):
        return self.__acname
    def set_acname(self, acname):
        self.__acname = acname

    def get_acno(self):
        return self.__acno
    def set_acno(self, acno):
        self.__acno = acno

    def get_acbal(self):
        return self.__acbal
    def set_acbal(self, acbal):
        self.__acbal = acbal

    def get_acpin(self):
        return self.__acpin
    def set_acpin(self, acpin):
        self.__acpin = acpin

    def get_actype(self):
        return self.__actype
    def set_actype(self, actype):
        self.__actype = actype

    @abstractmethod
    def set_withdraw(self, amount):
        pass

    def checkBal(self, acno, acpin):
        if self.__acno == acno and self.__acpin == acpin:
            return f"Account Balance : {self.__acbal}"
    


class SavingsAc(Account):

    def __init__(self, acname="", acbal = 0,acpin = 0, acno = 0,actype='s', ECS=0):
        super().__init__(acname, acbal, acpin, acno, actype)

    def __str__(self):
        return super().__str__()
    
    def get_ecs(self):
        return self.__ecs
    def set_ecs(self, ecs):
        self.__ecs = ecs

    savintr_rate = 8
    min_bal = 2000

    def set_withdraw(self, amount):
        self.set_acbal(self.get_acbal()-amount)

    

class CurrentAc(Account):
    def __init__(self, acname="", acbal = 0,acpin = 0, acno = 0,actype='c'):
        super().__init__(acname, acbal, acpin, acno, actype)

    def __str__(self):
        return super().__str__()
    
    curintr_rate = 6.5
    notrans = 1000
    min_bal = 1000

    def set_withdraw(self, amount):
        self.set_acbal(self.get_acbal()-amount)


    
class DematAc(Account):
    def __init__(self, acname="", acbal = 0,acpin = 0, acno = 0, actype='d'):
        super().__init__(acname, acbal, acpin, acno, actype)

    def __str__(self):
        return super().__str__()
    
    demintr_rate = 5
    commision = 7
    min_bal = 1500

    def set_withdraw(self, amount):
        self.set_acbal(self.get_acbal()-amount)

if __name__ == "__main__":
    print()
