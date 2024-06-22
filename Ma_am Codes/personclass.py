class Person:
    def __init__(self,pid=0,pname="",mob=""):
        self.__pid=pid
        self.__pname=pname
        self.__mobile=mob
    def __str__(self):
        return f"Id: {self.__pid} name:{self.__pname} mobile: {self.__mobile}"
    def set_pid(self,pid):
        self.__pid=pid
    def get_pid(self):
        return self.__pid
    def set_pname(self,pnm):
        self.__pname=pnm
    def get_pname(self):
        return self.__pname
    def set_mobile(self,m):
        self.__mobile=m
    def get_mobile(self):
        return self.__mobile
p1=Person(12,"Rajan","11111")
print(p1)
p1.set_mobile("33333")
print(p1.get_mobile())
#print(p1.__mobile)  #error
