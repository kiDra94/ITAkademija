import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "banjalukA1%",
    database = "mydb"
)

cursor = mydb.cursor()

'''toys = [('100', 'Teddy Bear', 25.0, 40), ('101', 'Bicycle', 100.0, 15)]
cursor.executemany("INSERT INTO toy_store_products VALUES (%s, %s, %s, %s)", toys) # U mysql se koristi %s umjesto ?
'''
cursor.execute("SELECT * FROM toy_store_products")
prod_list = cursor.fetchall()
print(prod_list)



mydb.commit()