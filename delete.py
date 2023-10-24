import sqlite3
conn =sqlite3.connect('ahmed.db')
print("opened successfully")



conn.execute("DELETE FROM EMPLOYEE where ID =10")

conn.commit()
cursor = conn.execute("SELECT * FROM EMPLOYEE")

for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("ADDRESS =", row[3])
    print("SALARY =", row[4])
    print("Operation Done Successfully")

conn.close()