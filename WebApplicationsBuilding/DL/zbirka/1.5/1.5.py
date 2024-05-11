import sqlite3
conn = sqlite3.connect("TestDataBase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Company(
   id  INT PRIMARY KEY,
   ime TEXT,
   godine INT,
   adresa TEXT,
   plata FLOAT);
""")
conn.commit()

while True:
    unos=input('Do you want to enter data for another worker? Yes/No: ')
    if unos=='Yes':
        id=int(input("Unesite id: "))
        ime=input("Unesite ime: ")
        godine=int(input("Unesite godine: "))
        adresa=input("Unesite adresu: ")
        plata=float(input('Unesite platu: '))
        radnik = (id,ime,godine,adresa,plata)
        cursor.execute("INSERT INTO Company VALUES (?, ?, ?, ?, ?)", radnik)
        conn.commit()
    
    elif unos=='No':
        break
    
    else:
        print('Pogresan unos. Unesite Yes ili No')

cursor.execute("SELECT * FROM Company;")

radnici = cursor.fetchall()
suma=0
broj_radnika=0
for radnik in radnici:
    if radnik[2]>=18:
        suma=suma+radnik[4]
        broj_radnika+=1

prosek=suma/broj_radnika
print("Prosecna plata punoletnih radnika je ",prosek)