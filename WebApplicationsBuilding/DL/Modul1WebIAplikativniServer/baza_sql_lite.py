import sqlite3
conn = sqlite3.connect("TestDataBase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
   studentId INT PRIMARY KEY,
   name TEXT,
   age INT,
   grade INT);
""")
conn.commit()

cursor.close()
conn.close()