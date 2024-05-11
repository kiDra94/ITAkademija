import sqlite3
conn = sqlite3.connect("TestDataBase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Pijaca(
   id_proizvoda INT PRIMARY KEY,
   ime TEXT,
   cena INT);
""")
conn.commit()


id_proizvoda=int(input("Unesite id proizvoda: "))
ime=input("Unesite ime proizvoda: ")
cena=input("Unesite cenu {}/a: ".format(ime))
proizvod = (id_proizvoda,ime,cena)
cursor.execute("INSERT INTO Pijaca VALUES (?, ?, ?)", proizvod)
conn.commit()

cursor.execute("SELECT * FROM Pijaca;")
proizvodi = cursor.fetchall()
suma=0
for proizvod in proizvodi:
    suma=suma+proizvod[2]
    print(proizvod)
    
print("Racun je ",suma)

