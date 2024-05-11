import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Delete the document with the address "Mountain 21":
myquery = {"address": "Mountain 21"}

mycol.delete_one(myquery)

for x in mycol.find():  # the same as SELECT * FROM customers
    print(x)