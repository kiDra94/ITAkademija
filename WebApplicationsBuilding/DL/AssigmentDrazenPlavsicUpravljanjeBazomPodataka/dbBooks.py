import sqlite3
conn = sqlite3.connect("Books.db")
cursor = conn.cursor()

def napraviTabelu():
   cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
      bookID INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT,
      year INT);
   """)
   conn.commit()

def dodajKnjige():
   title = str(input("Pleas enter the title: "))
   year = int(input("Pleas enter the year: "))
   books = {'title':title, "year":year}
   cursor.execute("INSERT INTO Books (title, year) VALUES (:title, :year)", books)
   conn.commit()

def iscitajKnjige():
   cursor.execute("SELECT * FROM Books;")
   all_results = cursor.fetchall()
   print(all_results)

iscitajKnjige()

cursor.close()
conn.close()