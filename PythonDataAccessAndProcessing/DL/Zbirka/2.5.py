import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Faculty(
  id TEXT PRIMARY KEY,
  country TEXT,
  university TEXT,
  name TEXT);
  """)

conn.commit()

faculty1 = ('121','Srbija', 'Univerzitet u Beogradu', 'ETF')
cursor.execute("INSERT INTO Faculty VALUES (?, ?, ?, ?)", faculty1)

conn.commit()

faculty2 = ('127','Srbija', 'Univerzitet u Novom Sadu', 'PMF')
cursor.execute("INSERT INTO Faculty VALUES (?, ?, ?, ?)", faculty2)

conn.commit()

faculty3 = ('129','Srbija', 'Univerzitet u Beogradu', 'TMF')
cursor.execute("INSERT INTO Faculty VALUES (?, ?, ?, ?)", faculty3)

conn.commit()

cursor.execute("""DELETE FROM  Faculty
  WHERE name = 'TMF'""")

cursor.execute("SELECT * FROM Faculty;")
faculty_list = cursor.fetchall()
 
print(faculty_list)
