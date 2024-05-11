import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["customers"]

#ispis prvih 5 redova
myresults = mycol.find().limit(5)

for x in myresults:
    print(x)