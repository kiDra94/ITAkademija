from mvc_model import Book
import mvc_view
def showAll():
   b = Book()   
   books_in_db = b.getAll()
    
   return mvc_view.showAllView(books_in_db)
 
def start():
    mvc_view.startView()
    showAll()
    mvc_view.endView()
 
if __name__ == "__main__":
   start()