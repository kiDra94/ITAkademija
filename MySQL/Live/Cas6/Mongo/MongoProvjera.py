import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["customers"]

for x in mycol.find():  # the same as SELECT * FROM customers
    print(x)
print("----------------------")

#The second parameter of the find() method is an object describing which fields to include in the result.
for x in mycol.find({}, {"address": 1}): #id + adresa
    print(x)
print("----------------------")
for x in mycol.find({}, {"_id":0,"address": 1}): #samo adresa
    print(x)
print("----------------------")
for x in mycol.find({}, {"name":1,"address": 1}): #id + ime + adresa
    print(x)
print("----------------------")
for x in mycol.find({}, {"_id":0, "name":1, "address": 1}): #ime + adresa
    print(x)
print("----------------------")