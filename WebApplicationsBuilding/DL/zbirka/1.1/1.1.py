import sqlite3
conn = sqlite3.connect("TestDataBase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
   id_studenta INT PRIMARY KEY,
   ime TEXT,
   godina_upisa INT);
""")
conn.commit()

while(True):
    izbor=int(input("\nAko zelite da unesete novog studenta ukucajte 1\nAko zelite da ispisete sve studente iz baze ukucajte 2\nAko zelite da izadjete iz programa ukucajte 0\n"))
    if(izbor==0):
        break
    elif(izbor==1):
        id_studenta=int(input("Unesite id studenta: "))
        ime=input("Unesite ime studenta: ")
        godina_upisa=input("Unesite godinu upisa: ")
        student = (id_studenta,ime,godina_upisa)
        cursor.execute("INSERT INTO Students VALUES (?, ?, ?)", student)
        conn.commit()
    elif(izbor==2):
        cursor.execute("SELECT * FROM Students;")
        studenti = cursor.fetchall()
        for student in studenti:
            print(student)
    else:
        print("Pogresan unos")