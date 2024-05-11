'''Zadatak 2.2. Konektovati se na bazu example.db pomoću sqlite3 modula. 
Napraviti tabelu Faculty ako ne postoji sa podacima:   id (TEXT, PRIMARY KEY), country(TEXT), university (TEXT), name(TEXT).
Dodati 3 fakulteta I Ispisati podatke iz baze. 
Izbrisati podatak čija je vrednost polja name TMF. Ispisati opet podatke iz baze podataka.'''

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

faculty1 = (1234563113, 'Srbija', 'Univerzitet u Beogradu','ETF')
cursor.execute("INSERT INTO Faculty VALUES (?, ?, ?, ?)", faculty1)

faculty2 = (12345631321, 'Srbija', 'Univerzitet u Novom Sadu','PMF')
cursor.execute("INSERT INTO Faculty VALUES (?, ?, ?,?)", faculty2)

faculty3 = (23234321321, 'Srbija', 'Univerzitet u Beogradu','TMF')
cursor.execute("INSERT INTO Faculty VALUES (?, ?, ?,?)", faculty3)

cursor.execute("SELECT * FROM Faculty;")
facultys = cursor.fetchall() 
print(facultys)

cursor.execute("""DELETE FROM  Faculty
  WHERE name = 'TMF'""")

cursor.execute("SELECT * FROM Faculty;")
facultys = cursor.fetchall() 
print(facultys)
