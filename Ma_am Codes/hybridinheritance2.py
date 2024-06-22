class A:
    def __init__(self,a1=0,a2=0):
        self.__a1=a1
        self.__a2=a2
    def __str__(self):
        return f"A1: {self.__a1} A2: {self.__a2}"
    
class B(A):
    def __init__(self,b1=0,**kwarg):
        print("in B ",kwarg)  #a1,a2,c1,c2
        super().__init__(**kwarg)  # to c constructor
        self.__b1=b1
    def __str__(self):
        return super().__str__()+f" B1: {self.__b1}"

class C(A):
    def __init__(self,c1=0,c2=0,**kwarg):
        print("in C",kwarg) #a1,a2
        super().__init__(**kwarg)
        self.__c1=c1
        self.__c2=c2
    def __str__(self):
        return super().__str__()+f" C1: {self.__c1} C2:{self.__c2}"
        
class D(B,C):
    def __init__(self,d1=0,**kwarg):
        print("in D : ",kwarg)
        super().__init__(**kwarg)
        self.__d1=d1
    def __str__(self):
        return super().__str__()+f" D1: {self.__d1}"
    
d1=D(a1=1,a2=2,b1=10,c1=31,c2=32,d1=41)
print(d1)
print(D.mro())

        
        
        
        
        
        
        








      
        
