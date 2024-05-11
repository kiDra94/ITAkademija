import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="banjalukA1%",
  database='fruitshop2',
  port=3306
)

mycursor = mydb.cursor()

def listaj_podatke():
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def unesi_podatke():
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
    mycursor.executemany(sql, val)
    mydb.commit()

def brisi_podatke():
    mycursor.execute("DELETE FROM customers")
    mydb.commit()

def truncate_podatke():
    mycursor.execute("TRUNCATE TABLE customers")
    mydb.commit()

def azuriraj_podatke():
    sql = "UPDATE customers SET address = %s WHERE address = %s"
    val = ("Canyon 123", "Valley 345")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

def azuriraj_podatke2(nova,stara):
    sql = "UPDATE customers SET address = %s WHERE address = %s"
    val = (nova, stara)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

if __name__=="__main__":
    truncate_podatke()
    brisi_podatke()
    unesi_podatke()
    listaj_podatke()
    print("--------------")
    azuriraj_podatke()
    listaj_podatke()
    print("--------------")
    azuriraj_podatke2("Valley 345", "Canyon 123")
    listaj_podatke()
    