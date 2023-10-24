import sqlite3
conn =sqlite3.connect('ahmed.db')
print("opened successfully")

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
VALUES(10,'sankuri','27','section3',187000)");

conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,SALARY)\
VALUES(11,'musaa','28','section3',200000)");

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
VALUES(12,'Minska','25','section3',250000)");

conn.execute("INSERT INTO EMPLOYEE(ID,NAME,AGE,ADDRESS,SALARY)\
VALUES(13,'abdi','24','section3',102000)");

conn.commit()
print("Recorded inserted Correctly")
conn.close()