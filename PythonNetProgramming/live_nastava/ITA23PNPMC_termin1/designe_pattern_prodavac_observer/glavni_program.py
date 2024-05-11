from konkretan_observer import Shop  
from konkretan_subject import Pen  
      
pen = Pen(10)  #postavlja prvobitnu cijenu
pen.add(Shop('Shop1'))  #dodaje shopove u listu; ovo je objekat za jednokratnu upotrebu pa ne treba ime tj. a = Shop("Shop1")
pen.add(Shop('Shop2'))  
pen.add(Shop('Shop3'))  
  
pen.penPrize = 15  #postavlja novu cijnu i svakoga obavjestava; radi ovako zato sto se poziva setter!, ne rusi princpi enkapsulacije!!!
pen.penPrize = 20  
pen.remove(pen.shops[0])#brise jedan shop!
pen.penPrize = 32
pen.add(Shop('Shop4'))  
pen.penPrize = 35