from account_class import *
# import re

aclst=[SavingsAc("Rajan",345678,1200,1234),
        CurrentAc("Revati",234567,1500,9874),
        DematAc("Atharva",123456,1800,4100)]

# Case 1: Add New Account
def addNewAccount(ch):
    name=input("Enter Name: ")
    accountpin=int(input("Enter Account Pin: "))
    balance=int(input("Enter Amount to add: "))
    if ch == 1:
        print("Savings Account created")
        saving = SavingsAc(name,balance,accountpin) 
    
    elif ch==2:
        print("Current Account created")
        saving = CurrentAc(name,balance,accountpin) 
    
    elif ch==3:
        print("Demat Account created")
        saving = DematAc(name,balance,accountpin)
    else:
        print("Invalid Choice")
    aclst.append(saving)
    print(aclst)

# Case 2: Withdraw Amount
def withdrawAmt():
    pass   

# Case 3: Deposit Amount
def depositAmt():
    pass

# Case 4: Change Pin
def changePin():
    pass

# Case 5: Check Balance
def checkBal(acno, acpin):
    for indx,ob in enumerate(aclst):
        if ob.get_acno()==acno and ob.get_acpin() == acpin:
            return indx,ob
    return -1,None

# Case 6: Close Account
def closeAccount():
    pass

choice=0
while choice!=7:
    choice=int(input("""
                     1. Create New Account
                     2. Withdraw Amount
                     3. Deposit Amount
                     4. Change Pin
                     5. Check Balance
                     6. Close Account
                     7. Exit
                     Enter Choice: """))
    match choice:
        case 1:
            ch=int(input("1. Saving Account\n2. Current Account\n 3. Demat Account\n"))
            addNewAccount(ch)
        
        case 2:
            pid=input("enetr id")
            status=withdrawAmt(pid)
            if status==1:
                print("found and deleted")
            elif status==2:
                print("found but not deleted")
            else:
                print("not found")
        
        case 3:
            pid=input("enetr id")
            sal=float(input("enetr salary"))
            status=depositAmt(pid,sal)
            
            if status==1:
                print("found and updated")
            elif status==2:
                print("found but not updated")
            else:
                print("not found")
        
        case 4:
            ch=int(input("1. Saving Account\n2. Current Account\n 3. Demat Account\n"))
            changePin()
        
        case 5:
            acno=int(input("Enter Account Number: "))
            acpin=int(input("Enter Your 4 Digit Pin: "))
            pos,e=checkBal(acno, acpin)
            if e!=None:
                print(e)
            else:
                print("Account Not found ",acno)
        
        case 6:
            pid=input("entr id")
            sal=closeAccount()
            if sal!=-1:
                print("Salary : ",sal)
            else:
                print("not found")
        
        case 7:
            print("Thank you for visiting")
        
        case _:
            print("Wrong choice. Enter Again")