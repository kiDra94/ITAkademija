import sqlite3
conn = sqlite3.connect("TestDataBase.db")
cursor = conn.cursor()

student = (1, 'Karen', 25, 9)
cursor.execute("INSERT INTO Students VALUES (?, ?, ?, ?)", student)
conn.commit()

student = {"studentId":2, 'name':'Steven', "age":27, "grade":7}
cursor.execute("INSERT INTO Students VALUES (:studentId, :name, :age, :grade)", student)
conn.commit()

#dodavanja vise odjednom

student = [{"studentId":4, 'name':'Steven', "age":27, "grade":7},
            {"studentId":3, 'name':'Karen', "age":25, "grade":9}]
cursor.executemany("INSERT INTO Students VALUES (:studentId, :name, :age, :grade)", student)
conn.commit()

cursor.close()
conn.close()