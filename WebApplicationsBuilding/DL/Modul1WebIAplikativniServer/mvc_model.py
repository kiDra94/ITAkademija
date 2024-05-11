class Book:
    def __init__(self, title = None, year = None):
        self.title = title
        self.year = year
         
    #returns all people inside db.txt as list of Person objects
    def getAll(self):
        books = [{'title':'The Picture of Dorian Gray','year':'1890'},
            {'title':'Pride and Prejudice','year':'1813'},
            {"title":'The Adventures of Tom Sawyer ', 'year':'1875'}]
        return books