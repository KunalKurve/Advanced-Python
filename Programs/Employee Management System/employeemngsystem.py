from personclassdemo import *
import os
'''
emplst=[SalariedEmp("Rajan","design","game designer",400000),
        ContractEmp("Revati","design","UX designer",50,7000),
        SalariedEmp("Atharva","Admin","CEO",4100000)]
'''
emplst=[]

#accept data and add new employee in the list
def addnewemployee(ch):
    nm=input("enter name")
    dept=input("enter department")
    desg=input("enetr designation")
    if ch==1:
        sal=float(input("enetr salary"))
        e=SalariedEmp(nm,dept,desg,sal)
    elif ch==2:
        hrs=int(input("enter hours"))
        hrcharges=float(input("enter hourly charges"))
        e=ContractEmp(nm,dept,desg,hrs,hrcharges)
    else:
        pass
        #add for vendor
    emplst.append(e)

#display all employees
def displayall():
    for ob in emplst:
        print(ob)
        
#seach emplyee by id
def findById(pid):
    for ind,ob in enumerate(emplst):
        if ob.get_pid()==pid:
            return ind,ob
    return -1,None
     
def deleteById(pid):
    ind,e=findById(pid) 
    if e!=None:
        ans=input(f"{e.get_pid()} {e.get_pname()} do you want to delete?(y/n)")
        if ans=="y":
            emplst.pop(ind) 
            return 1
        else:
            return 2
    else:
        return 3
    
def updateById(pid,sal):
    pos,e=findById(pid)
    if e!=None:
        ans=input(f"{e.get_pid()} {e.get_pname()} do you want to update")
        if ans=="y":
            if isinstance(e, SalariedEmp):
                e.set_sal(sal)
            elif isinstance(e,ContractEmp):
                e.set_hrcharges(sal)
            return 1
        else:
            return 2
    else:
        return 3

def calculatesalarydetails(pid):
    pos,e=findById(pid)
    if e!=None:
        return e.calcsal()
    else:
        return -1
    
def readSalariedfile(fname):
    with open(fname) as fh:
        for ln in fh:
            #s1,Rajan,design,game designer,400000
            lst=ln.rstrip("\n").split(",")
            e=SalariedEmp(lst[1],lst[2],lst[3],float(lst[4]),lst[0])
            emplst.append(e)
            
def readContractfile(fname):    
     with open(fname) as fh:
         for ln in fh:
             #c4,Deepa,HR,analyst,50,1000
             lst=ln.rstrip("\n").split(",")
             e=ContractEmp(lst[1],lst[2],lst[3],int(lst[4]),float(lst[5]),lst[0])       
             emplst.append(e)

def  writeTofile(fname1,fname2):
    with open(fname1,"w") as fh1:
        with open(fname2,"w") as fh2:
            for ob in emplst:
               if isinstance(ob,SalariedEmp):
                   fh1.write(f"{ob.get_pid()},{ob.get_pname()},{ob.get_dept()},{ob.get_desg()},{ob.get_Sal()}\n")
               elif isinstance(ob,ContractEmp):
                   fh2.write(f"{ob.get_pid()},{ob.get_pname()},{ob.get_dept()},{ob.get_desg()},{ob.get_hrs()},{ob.get_hrcharges()}\n")
        
             
if os.path.exists("salariedemp.csv"):
    #read data from file and store it in the lst
    readSalariedfile("salariedemp.csv")
if os.path.exists("contractemp.csv"):
    #read data from file and store it in the lst
    readContractfile("contractemp.csv")
    print("length: ",len(emplst))
choice=0
while choice!=7:
    choice=int(input("""1. add new employee
                     2. delete by id
                     3. update by id
                     4. display all
                     5. display By id
                     6. calculate salary
                     7. exit"""))
    match choice:
        case 1:
            ch=int(input("1. Salararied\n2. Contract\n 3. vendor\n"))
            addnewemployee(ch)
        case 2:
            pid=pid=input("enetr id")
            status=deleteById(pid)
            if status==1:
                print("found and deleted")
            elif status==2:
                print("found but not deleted")
            else:
                print("not found")
        case 3:
            pid=pid=input("enetr id")
            sal=float(input("enetr salary"))
            status=updateById(pid,sal)
            
            if status==1:
                print("found and updated")
            elif status==2:
                print("found but not updated")
            else:
                print("not found")
        case 4:
            displayall()
        case 5:
            pid=input("enetr id")
            pos,e=findById(pid)
            if e!=None:
                print(e)
            else:
                print("Not found====>",pid)
        case 6:
            pid=input("enetr id")
            sal=calculatesalarydetails(pid)
            if sal!=-1:
                print("Salary : ",sal)
            else:
                print("not found")
        case 7:
            writeTofile("salariedemp.csv","contractemp.csv")
            print("Thank you for visiting")
        case _:
            print("wrong choice")