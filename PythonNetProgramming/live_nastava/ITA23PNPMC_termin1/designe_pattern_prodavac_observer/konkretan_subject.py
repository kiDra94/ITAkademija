from subject import PenSubject  
    
class Pen(PenSubject):  

    shops = []  

    def __init__(self, prize):  
        self._penPrize = prize   

    def add(self, shop):  
        self.shops.append(shop)  
  
    def remove(self, shop):  
        self.shops.remove(shop)  
  
    def notify(self):  
        for shop in self.shops:  
            shop.update(self)  #svaki shop poziva update (fajl observer!!!)
        print('---------------------------------------')  

    @property  #getter; vraca vrijednost tj ovo je getter!!!
    def penPrize(self):  
        return self._penPrize  #vracanje cijene
 
    @penPrize.setter  #postavljanje cijene i automatizuje obavjestenje svima (notify metoda!); ovo je setter!!!
    def penPrize(self, prize):  
        self._penPrize = prize  
        self.notify()