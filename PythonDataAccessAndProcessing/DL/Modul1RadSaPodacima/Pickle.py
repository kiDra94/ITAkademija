import pickle
'''pickle.HIGHEST_PROTOCOL
pickle.DEFAULT_PROTOCOL'''

books = ('J.K. Rowling', 'Harry Potter',
            ((1997, 'Harry Potter and the Philosopher\'s Stone'),
            (1998, 'Harry Potter and the Chamber of Secrets'),
            (1999, 'Harry Potter and the Prisoner of Azkaban'),
            (2000, 'Harry Potter and the Goblet of Fire'),
            (2003, 'Harry Potter and the Order of the Phoenix'),
            (2005, 'Harry Potter and the Half-Blood Prince'),
            (2007, 'Harry Potter and the Deathly Hallows')))
 
with open('books_file', 'wb') as books_pickled:
    pickle.dump(books, books_pickled)
    '''
    potrebom dump() funkcije prosleđujemo podatke books
    koje želimo da serijalizujemo i parametar books_pickled, 
    koji objekte upisuje u željeni fajl.  
    '''
print(pickle.dumps(books))

with open('books_file', 'rb') as books_unpickled:
   print(pickle.load(books_unpickled))

print(pickle.loads(b"\x80\x04\x95i\x01\x00\x00\x00\x00\x00\x00\x8c\x0cJ.K. Rowling\x94\x8c\x0cHarry Potter\x94(M\xcd\x07\x8c(Harry Potter and the Philosopher's Stone\x94\x86\x94M\xce\x07\x8c'Harry Potter and the Chamber of Secrets\x94\x86\x94M\xcf\x07\x8c(Harry Potter and the Prisoner of Azkaban\x94\x86\x94M\xd0\x07\x8c#Harry Potter and the Goblet of Fire\x94\x86\x94M\xd3\x07\x8c)Harry Potter and the Order of the Phoenix\x94\x86\x94M\xd5\x07\x8c&Harry Potter and the Half-Blood Prince\x94\x86\x94M\xd7\x07\x8c$Harry Potter and the Deathly Hallows\x94\x86\x94t\x94\x87\x94."))
