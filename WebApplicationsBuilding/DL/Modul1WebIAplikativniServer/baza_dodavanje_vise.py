import sqlite3
conn = sqlite3.connect("TestDataBase.db")
cursor = conn.cursor()

student = [{"studentId":4, 'name':'Steven', "age":27, "grade":7},
            {"studentId":3, 'name':'Karen', "age":25, "grade":9}]
cursor.executemany("INSERT INTO Students VALUES (:studentId, :name, :age, :grade)", student)
conn.commit()

cursor.close()
conn.close()