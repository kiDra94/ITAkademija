from pymongo import MongoClient
client = MongoClient()
db = client.assigment
 
film = db.film
name = input("Unesite ime filma: ")
zanr = input("Unesite zanr: ")
godina = input("Unesite godinu: ")
movie_details = {
      'naziv_filma': name,
      'zanr': zanr,
      'godina' : godina,
  }
film.insert_one(movie_details)

result = film.find()

for i in result:
    print("Naziv filma: {} | Zanr: {} | Godina: {}".format(i['naziv_filma'], i['zanr'], i['godina']))
