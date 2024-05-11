import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
 
# Change the address from "Valley 345" to "Canyon 123":
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}
 
mycol.update_one(myquery, newvalues)
 
# print "customers" after the update:
for x in mycol.find():
    print(x)
 
# Update all documents where the address starts with the letter "H":
myquery = {"address": {"$regex": "^H"}}
newvalues = {"$set": {"name": "Minnie"}}
 
x = mycol.update_many(myquery, newvalues)
 
print(x.modified_count, "documents updated.")
 
# print "customers" after the update:
for x in mycol.find():
    print(x)