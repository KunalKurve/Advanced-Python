# D:\AdvMar2024\python bnp\mydata\mydb.db
import sqlite3
import json

def deletedata(pid):
    con=sqlite3.connect(r"D:\AdvMar2024\python bnp\mydata\mydb.db")
    cursor=con.cursor()
    cursor.execute("delete from product where pid=?",(pid,))
    con.commit()
    cursor.close()
    con.close()
    return True

def modifyproduct(data):
    con=sqlite3.connect(r"D:\AdvMar2024\python bnp\mydata\mydb.db")
    cursor=con.cursor()
    cursor.execute("update product set pname=?,qty=?,price=? where pid=?",(data['pname'],data['qty'],data['price'],data['pid']))
    con.commit()
    cursor.close()
    con.close()
    return True

def addnewproduct(data):
    con=sqlite3.connect(r"D:\AdvMar2024\python bnp\mydata\mydb.db")
    cursor=con.cursor()
    cursor.execute("insert into product values(?,?,?,?)",(data['pid'],data['pname'],data['qty'],data['price']))
    con.commit()
    cursor.close()
    con.close()
    return True

def findallproduct():
    con=sqlite3.connect(r"D:\AdvMar2024\python bnp\mydata\mydb.db")
    cursor=con.cursor()
    cursor.execute("select * from product")
    rows=cursor.fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i] #{"pid":12,"pname":"xxx"}
        result.append(d)
    if len(result)>0:
        #return {"payload":result}
        print(result)
        #convert dictionary into json fomat
        cursor.close()
        con.close()
        return json.dumps(result)
            # return make_response({"payload":result},200)
    else:
        return "No Data Found"