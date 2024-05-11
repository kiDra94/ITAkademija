import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "banjalukA1%",
    database = "mydb"
)

cursor = mydb.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Toy_Store_products(
               toy_id INT PRIMARY KEY,
               product_name TEXT,
               price FLOAT,
               quantity INT);)""")

mydb.commit()
