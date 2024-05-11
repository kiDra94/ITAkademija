import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root", #moze i na anu da se konektujemo(manje mogucnosti, posto joj nismo dali prava)
  #database="sakila", #moze i na bazu da se konektuje!
  password="banjalukA1%",
  port=3306
)

print(mydb)

mycursor = mydb.cursor() #memorijski objekat; prostor za podatke; tje moze da se napuni podatcima; pravi se iz konekcije

mycursor.execute("SHOW DATABASES") #izvrsava mysql naredbe!

for x in mycursor:
  print(x)

