'''Zadatak 2.3. Konektovati se na bazu example.db pomoću sqlite3 modula. 
Napraviti tabelu Voce ako ne postoji sa podacima:   sifrra (TEXT, PRIMARY KEY), name(TEXT), price(FLOAT). 
Dodati 4 voća I Ispisati podatke iz baze. Izbrisati podatak čija je vrednost polja name ’jabuka’ kao I podatak čija je cena 90.56 ako postoje.
Ispisati opet podatke iz baze podataka.'''


#import modula
import sqlite3

#konekcija na bazu
conn = sqlite3.connect('example.db')

#pravljenje kursora
cursor = conn.cursor()

#pravljenje tabele
cursor.execute("""CREATE TABLE IF NOT EXISTS Voce(
  sifra TEXT PRIMARY KEY,
  name TEXT,
  price FLOAT);
  """)
#kada se izvrsi izmena poziva se metoda commit radi cuvanja promena
conn.commit()

#definisanje podataka i dodavanje u bazu
voce1 = (1, 'jabuka', 50.56)
cursor.execute("INSERT INTO Voce VALUES (?, ?, ?)", voce1)

voce2 = (2, 'kruska', 80.6)
cursor.execute("INSERT INTO Voce VALUES (?, ?, ?)", voce2)

voce3 = (3, 'banana', 90.56)
cursor.execute("INSERT INTO Voce VALUES (?, ?, ?)", voce3)

voce4 = (4, 'ananas', 66.34)
cursor.execute("INSERT INTO Voce VALUES (?, ?, ?)", voce4)

#izdvajanje svih podataka iz baze
cursor.execute("SELECT * FROM Voce;")
#uzimanje redova izdvojenih podataka iz baze
voce = cursor.fetchall() 
#ispis podataka
print(voce)

#brisanje podataka
cursor.execute("""DELETE FROM  Voce
  WHERE name = 'jabuka'""")

cursor.execute("""DELETE FROM  Voce
  WHERE price = 90.56""")

#izdvajanje svih podataka iz baze
cursor.execute("SELECT * FROM Voce;")
#uzimanje redova izdvojenih podataka iz baze
voce = cursor.fetchall() 
#ispis podataka
print(voce)
