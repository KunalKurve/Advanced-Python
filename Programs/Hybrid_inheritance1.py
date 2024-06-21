class A:
    def __init__(self,a1=0,a2=0):
        self.__a1=a1
        self.__a2=a2
    def __str__(self):
        return f"A1:{self.__a1} A2:{self.__a2} "
    
class B(A):
    def __init__(self,a1=0,a2=0,b1=0):
        A.__init__(self,a1,a2)
        self.__b1=b1
    def __str__(self):
        return A.__str__(self)+f" B1:{self.__b1} "

class C(A):
    def __init__(self,a1=0,a2=0,c1=0,c2=0):
        A.__init__(self,a1,a2)
        self.__c1=c1
        self.__c2=c2
    def __str__(self):
        return A.__str__(self)+f" C1:{self.__c1} C2:{self.__c2} "
        
class D(B,C):
    def __init__(self,a1=0,a2=0,b1=0,c1=0,c2=0,d1=0):
        B.__init__(self,a1,a2,b1)
        C.__init__(self,a1,a2,c1,c2)
        self.__d1=d1
    def __str__(self):
        return B.__str__(self)+C.__str__(self)+f" D1:{self.__d1}"
    
d1=D(a1=1,a2=2,b1=10,c1=31,c2=32,d1=41)
print(d1)

# Here as B and C are both parent classes having the same parent class A. Hence class A is called twice.
# Hence to remove that we pass a dictionary with d to avoid calling A twice