import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="root1997",database="Hospital")
if con.is_connected():
    print("successfully connected")
cursor=con.cursor()
def insert():
    if d==1:
        insert()
        print("1.Enter Your Data")
    return
def update():
    if d==2:
        update()
    return
def delete():
    if d==3:
        delete()
    return
def select():
    if d==4:
        select()
    return
while True:
    name=input("enter name")
    age=int(input("enter age"))
    illness=input("enter illness")
    fees=float(input("enter fees"))
    query="insert into bombay_hospital values ('{}',{},'{}',{})". format(name,age,illness,fees)
    cursor.execute(query)
    if cursor.rowcount>0:
            print("successfully inserted")
    else:
        print("no insertion")
    con.commit()
    print("1.continue \n 2. Exit")
    k=int(input("enter your choice"))
    if k==2:
        break
while True:
    age=int(input("enter age"))
    name=input("enter name")
    query="update bombay_hospital set age={} where name='{}'".format(age,name)
    cursor.execute(query)
    if cursor.rowcount>0:
         print("successfully updated")
    else:
        print ("not update")
    con.commit()
    print("1. continue \n 2. Exit")
    k=int(input("Enter your choice"))
    if k==2:
        break
cursor=con.cursor()
age=int(input("enter age"))
query="delete from bombay_hospital where age={}".format(age)
cursor.execute(query)
if cursor.rowcount>0:
    print("Successfully deleted")
else:
    print("No delection")
con.commit()

print("Successfully connected")
cursor=con.cursor()
query="select * from bombay_hospital"
cursor.execute(query)
data=cursor.fetchall()
print(data)
