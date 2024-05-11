import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Persons(
  personal_id TEXT PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  year_of_birth INT);
  """)

conn.commit()

person1 = {"personal_id":12, 'first_name':'Mika', "last_name":'Mikic', "year_of_birth":1996}

cursor.execute("INSERT INTO Persons VALUES (:personal_id,:first_name, :last_name , :year_of_birth)", person1)

conn.commit()

person2 = (23,'Laza', 'Lazic', 1995)
cursor.execute("INSERT INTO Persons VALUES (?, ?, ?, ?)", person2)

conn.commit()

cursor.execute("SELECT * FROM Persons;")
persons_list = cursor.fetchall()
 
print(persons_list)
