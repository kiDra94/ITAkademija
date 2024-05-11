#prodavac i kupac; poravac ima listu kupaca! dodavanjem kupca obavestava se odma o promjeni cijeni!
#prodavac ima info o svim kupcima
#prodavac ima metodu azuriranja cijene; obavestavanja kupca; 
#kupac ima metodu koja provjerava info od prodavca
#2 classe kupac(procitaj info od prodavca) i prodavac(obavesti, dodaj kupca, azuriraj cijenu)
#dizajn patern cemo raditi prkeo abstractne classe -> bolje; posto moze da se pravi novi prodavac sa istim metodama ali drugi prodavac!
from abc import ABC, abstractmethod  
      
class PenSubject(ABC):  #ABC-> Abstract Base Class
     
    @abstractmethod  #abstracmethod nema tijela zato je pass
    def add(self, shop):  
            pass  
        
    @abstractmethod  
    def remove(self, shop):  
            pass  
        
    @abstractmethod  
    def notify(self):  
            pass