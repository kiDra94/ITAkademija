'''Zadatak 2.4. Potrebno je omogućiti korisniku da putem komandne linije unese  ime predstave, prvu godinu prikaza kao I žanr.
Podatke je potrebno smestiti u MongoDB nerelacionu bazu podataka.
Nakon uspešnog unošenja, potrebno je u komandnoj liniji prikazati korisniku sve podatke iz kolekcije.'''

#import modula
from pymongo import MongoClient

#Sledeći korak je konekcija na bazu
client = MongoClient()

#Pravimo instancu klijenta koji će izvršiti konekciju na bazu,koristićemo test bazu podataka umesto klasičnog konektovanja na server.
db=client.test

#unos podataka
name = input("Unesite ime: ")
year = input("Unesite godinu: ")
genre=input("Unesite zanr: ") 

#kreiranje kolekcije podatka
plays = db.movies

#pravljenje recnika
play_details = {
    'name': name,
    'year':year,
    'genre': genre
}

#unos jednog objekta u bazu
plays.insert_one(play_details)
 
#pregled podataka
result = plays.find()
 
#ispis podatka
for r in result:
    print("Play: {} | Year: {} | Genre: {}".format(r['name'],r['year'], r['genre']))
