import pymysql

con=pymysql.connect(r"D:\AdvMar2024\python bnp\mydata\mydb.db")

# MVT - model view template is the framework followed in Django

if con!=None:
    print("Connection Done")
    cursor=con.cursor()
    
def displayall():
    cursor.execute("select * from product")
    rows=cursor.fetchall()  #List of tuples in rows
    for row in rows:
        print(f"id :{row[0]}, name:{row[1]}, qty:{row[2]}, price:{row[3]}")
    
def addnewrecord():
    pid=int(input("Enter Product ID: "))
    pnm=input("Enter Product Name: ")
    qty=int(input("Enter Quantity: "))
    price=float(input("enetr price"))
    cursor.execute("Insert into product values(%s,%s,%s,%s)",(pid,pnm,qty,price))
    con.commit()

def deletebyid(pid):
    cursor.execute("select * from product where pid=%s",(pid,))
    con.commit()
    
def updatebyid(pid,pnm,qty,pr):
    cursor.execute("update product set pname=%s,qty=%s,price=%s where pid=%s",(pnm,qty,pr,pid))
    con.commit()  

def displayByID(pid):
    cursor.execute("Delete from product where pid=%s",(pid,))
    
def displaysorted():
    cursor.execute("select * from product prder by pname" )
    rows = cursor.fetchall()
    for row in rows:
        print(f"id : {row[0]} name: {row[1]} qty: {row[2]} price: {row[3]}" )

choice=0
while choice!=7:
    choice=int(input("""
                     1. add new record
                     2. delete record
                     3. update record
                     4. display all
                     5. display by id
                     6. display in sorted order
                     7.exit"""))
    match choice:
        case 1:
            addnewrecord()
        case 2:
            pid=int(input("enetr pid"))
            deletebyid(pid)
        case 3:
            pid=int(input("enetr pid"))
            pnm=input("enetr pname")
            qty=int(input("enetr qty"))
            pr=float(input("enetr price"))
            updatebyid(pid,pnm,qty,pr)
        case 4:
            displayall()
        case 5:
            pid=int(input("enetr pid"))
            displayByID(pid)
        case 6:
            print("Printing in Sorted Order: ")
            displaysorted()
            pass
        case 7:
            cursor.close()
            con.close()
            print("Thank you for visiting....")
        case _:
            print("invalid choice")