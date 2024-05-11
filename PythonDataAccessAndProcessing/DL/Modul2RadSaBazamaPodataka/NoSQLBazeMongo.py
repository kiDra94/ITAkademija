from pymongo import MongoClient
from pprint import pprint
client = MongoClient()
db=client.test
 
contacts = db.contacts
contact_details = {
      'Name': 'Brian Simpson',
      'Phone': '00442561145886'
  }
# DODAVANJE
# contacts.insert_one(contact_details)

# PROMJENA
'''db.contacts.update_one(
        {"Name":'Brian Simpson'},
        {
        "$set": {
            "Name":"Homer Simpson",
            "Phone":'00442561145800'
        }
        })'''
# BRISANJE
contacts.delete_one({"Name":"Homer Simpson"})

queryresult = contacts.find_one({"Name":'Homer Simpson'})
pprint(queryresult)