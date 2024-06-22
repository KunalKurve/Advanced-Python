import sqlite3

con=sqlite3.connect(r"D:\python bnp\mydata\mydb.db")
if con!=None:
    print("connection done")
    cursor=con.cursor()
    
def displayall():
    cursor.execute("select * from product")
    rows=cursor.fetchall()
    for row in rows:
        print(f"id : {row[0]} name: {row[1]} qty: {row[2]} price: {row[3]}")
    
def addnewrecord():
    pid=int(input("enetr pid"))
    pnm=input("enetr pname")
    qty=int(input("enetr qty"))
    price=float(input("enetr price"))
    cursor.execute("insert into product values(?,?,?,?)",(pid,pnm,qty,price))
    con.commit()

def deletebyid(pid):
    cursor.execute("delete from product where pid=?",(pid,))
    con.commit()
    
def updatebyid(pid,pnm,qty,pr):
    cursor.execute("update product set pname=?,qty=?,price=? where pid=?",(pnm,qty,pr,pid))
    con.commit()  

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
            pass
        case 6:
            pass
        case 7:
            cursor.close()
            con.close()
            print("Thank you for visiting....")
        case _:
            print("invalid choice")