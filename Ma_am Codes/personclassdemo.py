from abc import ABC,abstractmethod
class Person:
    cnt=1
    @staticmethod
    def __generatecode(type):
        pid=type+str(Person.cnt)
        
        return pid
        
    def __init__(self,etype="s",name="",pid=0):
        print("in person init")
        if pid==0:
            self.__pid=Person.__generatecode(etype)
        else:
            self.__pid=pid
        Person.cnt=Person.cnt+1
        self.__pname=name
    def set_pid(self,pid):
        self.__pid=pid
    def get_pid(self):
        return self.__pid
    
    def set_pname(self,nm):
        self.__pname=nm
        
    def get_pname(self):
        return self.__pname
          
    
    def __str__(self):
        print("in person str")
        return f"Id: {self.__pid} Name: {self.__pname}"

class Employee(Person,ABC):
    def __init__(self,etype="s",nm="",dept="",desg="",pid=0):
        print("in employee constructor")
        #call parent constructor
        super().__init__(etype,nm,pid)
        #Person.__init__(self,etype,nm)
        self.__dept=dept
        self.__desg=desg
    def set_dept(self,d):
        self.__dept=d
    def set_desg(self,d):
        self.__desg=d
    def get_dept(self):
         return self.__dept
    def get_desg(self):
         return self.__desg
    @abstractmethod 
    def calcsal(self):
        pass
    
    def __str__(self):
        print("in employee str")
        return super().__str__()+f" Department: {self.__dept} Designation: {self.__desg}"
    
    
class SalariedEmp(Employee):
    def __init__(self,nm="",dept="",desg="",sal=0,pid=0,etype="s"):
        super().__init__(etype,nm,dept,desg,pid)
        self.__sal=sal
        self.__bonus=0.10*sal
    def set_sal(self,s):
        self.__sal=s
    def set_bonus(self,b):
        self.__bonus=b
    def get_sal(self):
        return self.__sal
    def get_bonus(self):
        return self.__bonus
    def calcsal(self):
        return self.__sal+0.10*self.__sal+0.15*self.__sal-0.08*self.__sal
    def __str__(self):
        return super().__str__()+f" Salary : {self.__sal} Bonus: {self.__bonus}"
    
    
class ContractEmp(Employee):
    def __init__(self,nm="",dept="",desg="",hrs=0,hrcharges=0,pid=0,etype="c"):
        super().__init__(etype,nm,dept,desg,pid)
        self.__hrs=hrs
        self.__hrcharges=hrcharges
    def set_hrs(self,s):
        self.__hrs=s
    def set_hrcharges(self,b):
        self.__hrcharges=b
    def get_hrs(self):
        return self.__hrs
    def get_hrcharges(self):
        return self.__hrcharges
    def calcsal(self):
        return self.__hrs*self.__hrcharges
    def __str__(self):
        return super().__str__()+f" Hrs : {self.__hrs} Hr. charges: {self.__hrcharges}"        
    
    
    
if __name__=="__main__":
    #ob=Employee("s","xxx","HR","Manager")
    ob=SalariedEmp("Sanjay","HR","Mgr",300000)
    print("Salary: ",ob.calcsal())
    ob1=ContractEmp("Neeta","HR","Mgr",20,3000)
    print("Charges: ",ob1.calcsal())
    print(ob)
    print(ob1)
    
# =============================================================================
#     ob=Employee("s","xxx","HR","Manager")
#     print(ob)
# =============================================================================
# =============================================================================
#     ob=Person(name="Rajan")
#     ob1=Person(name="Deepali")
#     print(ob)
#     print(ob1)
# =============================================================================

