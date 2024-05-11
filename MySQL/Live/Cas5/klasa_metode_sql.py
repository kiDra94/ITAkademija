import mysql.connector

class Konekcija:
    
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="banjalukA1%",
        database='fruitshop2',
        port=3306)
        self.mycursor = self.mydb.cursor()

    def listaj_podatke(self):
        self.mycursor.execute("SELECT * FROM customers")
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)

    def unesi_podatke(self):
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = [
        ('Peter', 'Lowstreet 4'),
        ('Amy', 'Apple st 652'),
        ('Hannah', 'Mountain 21'),
        ('Michael', 'Valley 345'),
        ('Sandy', 'Ocean blvd 2'),
        ('Betty', 'Green Grass 1'),
        ('Richard', 'Sky st 331'),
        ('Susan', 'One way 98'),
        ('Vicky', 'Yellow Garden 2'),
        ('Ben', 'Park Lane 38'),
        ('William', 'Central st 954'),
        ('Chuck', 'Main Road 989'),
        ('Viola', 'Sideway 1633')
        ]
        self.mycursor.executemany(sql, val)
        self.mydb.commit()

    def brisi_podatke(self):
        self.mycursor.execute("DELETE FROM customers")
        self.mydb.commit()

    def truncate_podatke(self):
        self.mycursor.execute("TRUNCATE TABLE customers")
        self.mydb.commit()

    def azuriraj_podatke(self):
        sql = "UPDATE customers SET address = %s WHERE address = %s"
        val = ("Canyon 123", "Valley 345")
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record(s) affected")

    def azuriraj_podatke2(self, nova, stara):
        sql = "UPDATE customers SET address = %s WHERE address = %s"
        val = (nova, stara)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record(s) affected")

if __name__=="__main__":
    k = Konekcija()
    print(id(k))
    k2 = Konekcija()
    print(id(k2))
    k.truncate_podatke()
    k.brisi_podatke()
    k.unesi_podatke()
    k.listaj_podatke()
    print("--------------")
    k.azuriraj_podatke()
    k.listaj_podatke()
    print("--------------")
    k.azuriraj_podatke2("Valley 345", "Canyon 123")
    k.listaj_podatke()
    