'''Zadatak 2.3. Konektovati se na bazu example.db pomoću sqlite3 modula. 
Napraviti tabelu Voce ako ne postoji sa podacima:   sifrra (TEXT, PRIMARY KEY), name(TEXT), price(FLOAT). 
Dodati 4 voća I Ispisati podatke iz baze. Izbrisati podatak čija je vrednost polja name ’jabuka’ kao I podatak čija je cena 90.56 ako postoje.
 Ispisati opet podatke iz baze podataka.'''

import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Voce(
  sifra TEXT PRIMARY KEY,
  name TEXT,
  price FLOAT);
  """)
conn.commit()

voce1 = (1, 'jabuka', 50.56)
cursor.execute("INSERT INTO Voce VALUES (?, ?, ?)", voce1)

voce2 = (2, 'kruska', 80.6)
cursor.execute("INSERT INTO Voce VALUES (?, ?, ?)", voce2)

voce3 = (3, 'banana', 90.56)
cursor.execute("INSERT INTO Voce VALUES (?, ?, ?)", voce3)

voce4 = (4, 'ananas', 66.34)
cursor.execute("INSERT INTO Voce VALUES (?, ?, ?)", voce4)

cursor.execute("SELECT * FROM Voce;")
voce = cursor.fetchall() 
print(voce)

cursor.execute("""DELETE FROM  Voce
  WHERE name = 'jabuka'""")

cursor.execute("""DELETE FROM  Voce
  WHERE price = 90.56""")

cursor.execute("SELECT * FROM Voce;")
voce = cursor.fetchall() 
print(voce)
