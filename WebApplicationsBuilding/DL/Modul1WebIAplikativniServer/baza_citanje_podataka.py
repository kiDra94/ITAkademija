import sqlite3
conn = sqlite3.connect("TestDataBase.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Students;")
all_results = cursor.fetchall()
one_results = cursor.fetchone()
mny_results = cursor.fetchmany(2)
print(all_results)
print(one_results)
print(mny_results)

cursor.close()
conn.close()