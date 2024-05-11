import pymongo

c = pymongo.MongoClient('localhost', 27017)
db = c['test']
'''
# BRISANJE (posto je pokrenuto par puta bez printa, pa se svaka poruka snimi)
db.q1.drop()
db.q2.drop()

db.q1.insert_one({'val': 'first mesage'}) #q1 je red
db.q1.insert_one({'val': 'second mesage'})
db.q1.insert_one({'val': 'third mesage'})

db.q2.insert_one({'val': 'queue2 first mesage'}) #q2 je red
db.q2.insert_one({'val': 'queue2 second mesage'})

print(db.q1.find()) # <pymongo.cursor.Cursor object at 0x00000284BD79A870>
print(db.q2.find()) # <pymongo.cursor.Cursor object at 0x00000284BDE326F0>
'''

deleted_document = db.q1.find_one_and_delete({'val': {'$regex': 'first mesage'}})

if deleted_document is not None:
    print(deleted_document['val'])
else:
    print("No document found with val='first_message'")


for rq1 in db.q1.find():
    print(rq1)
for rq2 in db.q2.find():
    print(rq2)