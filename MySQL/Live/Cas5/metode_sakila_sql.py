import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="banjalukA1%",
  database='sakila',
  port=3306
)

mycursor = mydb.cursor()

def izlistaj_podatke():
    sql = "SELECT category.name, AVG(length) FROM  film JOIN film_category USING (film_id)\
          JOIN category USING (category_id) GROUP BY category.name ORDER BY AVG(length) DESC;"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

if __name__=="__main__":
    izlistaj_podatke()