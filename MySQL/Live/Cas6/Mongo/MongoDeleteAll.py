import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
 
# Delete all documents were the address starts with the letter S:
myquery = {"address": {"$regex": "^S"}}
 
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")
 
for x in mycol.find():  # the same as SELECT * FROM customers
    print(x)
 
# Delete all documents in the "customers" collection:
'''
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")
'''
 
# Delete the "customers" collection:
# mycol.drop() 