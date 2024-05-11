
from pymongo import MongoClient
client = MongoClient()
db=client.test

while True: 
    index=input("Unesite index: ")
    first_name = input("Unesite ime: ")
    last_name = input("Unesite prezime: ")


    if(index=='' or first_name=='' or last_name==''):
        break
    else:
        students = db.students
        student_details = {
            'index': index,
            'first_name':first_name,
            'last_name': last_name
        }

        students.insert_one(student_details)

        result = students.find()

        for r in result:
            print("Index: {} | First name: {} | Last name: {}".format(r['index'],r['first_name'], r['last_name']))