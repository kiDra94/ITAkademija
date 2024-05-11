'''Zadatak 2.1. Konektovati se na bazu example.db pomoću sqlite3 modula. 
Napraviti tabelu City ako ne postoji sa podacima: name(text), country(text,Primary key), number_od_citizens(int). 
Dodati 2 grada. Ispisati podatke iz baze.'''

import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Citys(
  name TEXT,
  country TEXT PRIMARY KEY,
  number_od_citizens INT);
  """)

conn.commit()

city1 = ('Beograd', 'Srbija', 6945234)
cursor.execute("INSERT INTO Citys VALUES (?, ?, ?)", city1)

city2=('Bratislava',"Hungary",9879000)
cursor.execute("INSERT INTO Citys VALUES (?,?,?)", city2)

conn.commit()


cursor.execute("SELECT * FROM Citys;")

citys = cursor.fetchall() 
print(citys)
