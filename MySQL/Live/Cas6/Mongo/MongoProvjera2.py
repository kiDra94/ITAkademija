import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# sort("name", 1) #ascending
# sort("name", -1) #descending

# Sort the result alphabetically by name:
mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)

print("-----------------")

# Sort the result reverse alphabetically by name:
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
    print(x)

print("-----------------")

mydoc = mycol.find().sort("address")

for x in mydoc:
    print(x)

print("-----------------")

# Sort the result reverse alphabetically by name:
mydoc = mycol.find().sort("address", -1)

for x in mydoc:
    print(x)