'''Zadatak 2.2. Konektovati se na bazu example.db pomoću sqlite3 modula. 
Napraviti tabelu Faculty ako ne postoji sa podacima:   id (TEXT, PRIMARY KEY), country(TEXT), university (TEXT), name(TEXT).
Dodati 3 fakulteta I Ispisati podatke iz baze. 
Izbrisati podatak čija je vrednost polja name TMF. Ispisati opet podatke iz baze podataka.'''

#import modula
import sqlite3

#konekcija na bazu
conn = sqlite3.connect('example.db')

#pravljenje kursora
cursor = conn.cursor()

#pravljenje tabele
cursor.execute("""CREATE TABLE IF NOT EXISTS Faculty(
  id TEXT PRIMARY KEY,
  country TEXT,
  university TEXT,
  name TEXT);
  """)

#kada se izvrsi izmena poziva se metoda commit radi cuvanja promena
conn.commit()

#definisanje podataka i dodavanje u bazu
faculty1 = (1234563113, 'Srbija', 'Univerzitet u Beogradu','ETF')
cursor.execute("INSERT INTO Faculty VALUES (?, ?, ?, ?)", faculty1)

faculty2 = (12345631321, 'Srbija', 'Univerzitet u Novom Sadu','PMF')
cursor.execute("INSERT INTO Faculty VALUES (?, ?, ?,?)", faculty2)

faculty3 = (23234321321, 'Srbija', 'Univerzitet u Beogradu','TMF')
cursor.execute("INSERT INTO Faculty VALUES (?, ?, ?,?)", faculty3)

#izdvajanje svih podataka iz baze
cursor.execute("SELECT * FROM Faculty;")
#uzimanje redova izdvojenih podataka iz baze
facultys = cursor.fetchall() 
#ispis podataka
print(facultys)

#brisanje podatka koji za ime ima vrednost TMF
cursor.execute("""DELETE FROM  Faculty
  WHERE name = 'TMF'""")


#izdvajanje svih podataka iz baze
cursor.execute("SELECT * FROM Faculty;")
#uzimanje redova izdvojenih podataka iz baze
facultys = cursor.fetchall() 
#ispis podataka
print(facultys)
