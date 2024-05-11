'''Zadatak 2.1. Konektovati se na bazu example.db pomoću sqlite3 modula. 
Napraviti tabelu City ako ne postoji sa podacima: name(text), country(text,Primary key), number_od_citizens(int). 
Dodati 2 grada. Ispisati podatke iz baze.'''


#import modula
import sqlite3

#konekcija na bazu
conn = sqlite3.connect('example.db')

#pravljenje kursora
cursor = conn.cursor()

#pravljenje tabele
cursor.execute("""CREATE TABLE IF NOT EXISTS Citys(
  name TEXT,
  country TEXT PRIMARY KEY,
  number_od_citizens INT);
  """)

#kada se izvrsi izmena poziva se metoda commit radi cuvanja promena
conn.commit()

#definisanje podataka i dodavanje u bazu
city1 = ('Beograd', 'Srbija', 6945234)
cursor.execute("INSERT INTO Citys VALUES (?, ?, ?)", city1)

city2=('Bratislava',"Hungary",9879000)
cursor.execute("INSERT INTO Citys VALUES (?,?,?)", city2)

#izdvajanje svih podataka iz baze
cursor.execute("SELECT * FROM Citys;")

#uzimanje redova izdvojenih podataka iz baze
citys = cursor.fetchall() 

#ispis podataka
print(citys)
