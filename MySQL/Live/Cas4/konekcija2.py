import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="fruitshop2",
  password="banjalukA1%",
  port=3306
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("DELETE from customers")
mydb.commit()