#kreiranje baze
import sqlite3

conn = sqlite3.connect('example.db') #ako je neam sama se kreira

cursor = conn.cursor()
# DODAVANJE PREKO N-TORKE
# toy = ('100', 'Teddy Bear', 25.0, 40)
# cursor.execute("INSERT INTO Toy_Store_Products VALUES (?, ?, ?, ?)", toy)
# DODAVANJE PREKO RIJECNIKA
# toy1 = {'toy_id':'200', 'product_name':'Puzzle', 'price':30.0, 'quantity':20}
# cursor.execute("""INSERT INTO Toy_Store_Products VALUES 
               # (:toy_id, :product_name, :price, :quantity)""", 
               # toy1)
# DODAVANJE VISE ODJEDNOM PREKO LISTE N-TORKE (executemany!)
'''toys = [('101', 'Bicycle', 100.0, 15), ('102', 'Doll', 20.0, 35)]
cursor.executemany("""INSERT INTO Toy_Store_Products VALUES 
               (?, ?, ?, ?)""", toys)'''

cursor.execute("SELECT * FROM Toy_Store_Products")
product_list = cursor.fetchall() #kupi sve
print(product_list)
cursor.execute("UPDATE Toy_Store_Products SET price = 80.0 WHERE product_name = 'Bicycle'")

cursor.execute("DELETE FROM Toy_Store_Products WHERE product_name = 'Doll'")



conn.commit()
