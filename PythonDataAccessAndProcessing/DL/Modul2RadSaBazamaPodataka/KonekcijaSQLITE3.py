#kreiranje baze
import sqlite3

conn = sqlite3.connect('example.db') #ako je neam sama se kreira

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Toy_Store_Products(
               toy_id INT PRIMARY KEY,
               product_name TEXT,
               price FLOAT,
               quantity INT);""")

conn.commit()
