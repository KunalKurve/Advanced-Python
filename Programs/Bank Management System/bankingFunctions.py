from account_class import *
# import re

aclst=[SavingsAc("Rajan",5000,1234,'s1'),
        CurrentAc("Revati",10000,1234,'c1'),
        DematAc("Atharva",18000,1234,'d1')]


def findAccount(acno):
    for ind,ob in enumerate(aclst):
        if ob.get_acno()==acno:
            return ind,ob
    return -1,None

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
    # for ob in aclst:
    #     print(ob)

# Case 2: Withdraw Amount
def withdrawAmt(acno,acpin,ch):
    indx, ob = findAccount(acno)
    if ob!= None:
        if ob.get_acpin() == acpin:
            amount = int(input("Enter amount to withdraw: "))
            for indx,ob in enumerate(aclst):
                if ch == 1:
                    if ob.get_acbal() - amount >= SavingsAc.min_bal:
                        ob.set_withdraw(amount)
                    else:
                        print("Low balance")
                elif ch == 2:
                    if ob.get_acbal() - amount >= CurrentAc.min_bal:
                        ob.set_withdraw(amount)
                    else:
                        print("Low balance")
                elif ch == 3:
                    if ob.get_acbal() - amount >= DematAc.min_bal:
                        ob.set_withdraw(amount)
                    else:
                        print("Low balance")
                else:
                    print("Invalid Operation")
        else:
            print("Incorrect Pin")
    else:
        print("Account Not Found")    

# Case 3: Deposit Amount
def depositAmt(acno,acpin):
    indx, ob = findAccount(acno)
    if ob!= None:
        if ob.get_acpin() == acpin:
            recpacno=input("Enter Account Number to deposit amount: ")
            amount = int(input("Enter amount to deposit: "))
            indx1, ob1 = findAccount(recpacno)
            if ob1 != None and ob1.get_acno() == recpacno:
                ob1.set_deposit(amount)
                print("Ammount deposited Successfully!")
            else:
                print("Recipient Account Not Found")
        else:
            print("Incorrect Pin")
    else:
        print("Your Account Not Found")

# Case 4: Change Pin
def changePin(acno,acpin):
    indx, ob = findAccount(acno)
    if ob!= None:
        if ob.get_acpin() == acpin:
            newacpin=int(input("Enter Your new 4 Digit Pin: "))
            ob.set_acpin(newacpin)
            print("Pin Changed Successfully!")
        else:
            print("Incorrect Pin")
    else:
        print("Account Not Found")

# Case 5: Check Balance
def checkBal(acno, acpin):
    for indx,ob in enumerate(aclst):
        if ob.get_acno()==acno and ob.get_acpin() == acpin:
            return indx,ob
    return -1,None

# Case 6: Close Account
def closeAccount(acno, acpin):
    for indx,ob in enumerate(aclst):
        if ob.get_acno() == acno and ob.get_acpin() == acpin:
            ans=input(f"{ob.get_acno()} {ob.get_acname()} Do you want to delete?(y/n): ")
            if ans=="y":
                aclst.pop(indx)
                return 1
            else:
                return 2
        else:
            return 3

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
        case 1: # Add New Account
            ch=int(input("1. Saving Account\n2. Current Account\n 3. Demat Account\n"))
            addNewAccount(ch)
        
        case 2: # Withdraw Amount
            acno=input("Enter Your Account Number: ")
            acpin=int(input("Enter Your 4 Digit Pin: "))
            ch=int(input("Enter your account type\n1. Saving Account\n2. Current Account\n 3. Demat Account \n"))
            withdrawAmt(acno,acpin,ch)
        
        case 3: # Deposit Amount
            acno=input("Enter Your Account Number: ")
            acpin=int(input("Enter Your 4 Digit Pin: "))
            depositAmt(acno,acpin)
            pass
        
        case 4: # Change Pin
            acno=input("Enter Your Account Number: ")
            acpin=int(input("Enter Your 4 Digit Pin: "))
            changePin(acno,acpin)
            pass
        
        case 5: # Check Balance
            acno=input("Enter Your Account Number: ")
            acpin=int(input("Enter Your 4 Digit Pin: "))
            pos,e=checkBal(acno, acpin)
            if e!=None:
                print(e)
            else:
                print("Account Not found ",acno)
        
        case 6: # Close Account
            acno=input("Enter Your Account no: ")
            acpin=int(input("Enter Your 4 Digit Pin: "))
            status=closeAccount(acno,acpin)
            if status==1:
                print("Found and Deleted")
            elif status==2:
                print("Found but Not Deleted")
            else:
                print("Not Found")
        
        case 7:
            print("Thank you for visiting!")
        
        case _:
            print("Wrong choice. Enter Again!")