import pymongo
 
c = pymongo.MongoClient('localhost', 27017)
db = c['test']

db.q1.insert_one({'val': 'Peric'})
db.q1.insert_one({'val': 'Mikic'})
db.q1.insert_one({'val': 'Zakovic'})
 
for row in db.q1.find():
  print (row)
