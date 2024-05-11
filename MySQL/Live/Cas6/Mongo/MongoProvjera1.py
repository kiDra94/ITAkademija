import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Find document(s) with the address "Park Lane 38":

myquery = {"address": "Park Lane 38"}
mydoc = mycol.find(myquery)

# SELECT * FROM mydatabase.customers WHERE address = 'Park Lane 38'
for x in mydoc:
    print(x)

print("-------------------------")

# Find documents where the address starts with the letter "S" or higher:
myquery = {"address": {"$gt": "S"}}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# Filter With Regular Expressions
# Find documents where the address starts with the letter "S":
myquery = {"address": {"$regex": "^S"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
