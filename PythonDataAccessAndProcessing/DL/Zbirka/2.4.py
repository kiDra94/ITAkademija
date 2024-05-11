'''Zadatak 2.4. Potrebno je omogućiti korisniku da putem komandne linije unese  ime predstave, prvu godinu prikaza kao I žanr.
Podatke je potrebno smestiti u MongoDB nerelacionu bazu podataka.
Nakon uspešnog unošenja, potrebno je u komandnoj liniji prikazati korisniku sve podatke iz kolekcije.'''


from pymongo import MongoClient
client = MongoClient()
db=client.test
 
name = input("Unesite ime: ")
year = input("Unesite godinu: ")
genre=input("Unesite zanr: ") 

plays = db.movies
play_details = {
    'name': name,
    'year':year,
    'genre': genre
}
 
plays.insert_one(play_details)
 
result = plays.find()
 
for r in result:
    print("Play: {} | Year: {} | Genre: {}".format(r['name'],r['year'], r['genre']))
