import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEE
         (EMPNO         CHAR(50),
         NAME           CHAR(20),
         DEPARTMENT     CHAR(20),
         GENDER         CHAR(10),
         ADDRESS        CHAR(40));''')

print("Table created successfully")

conn.close()