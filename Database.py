import sqlite3
conn =sqlite3.connect('ahmed.db')
print("opened successfully")

conn.execute('''CREATE TABLE EMPLOYEE(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("table created successfully")
conn.close()