'''Zadatak 1.5.  Napraviti klasu Person koja konstruktorom definiše ime I prezime. Instancirati 2 objekta.
 Upisati objekte u fajl ShelveExample pomoću Shelve modula. 
 Ključevi treba da budu stringovi koji predstavljaju redni broj objekta a vrednosti treba da budu objekti. 
 Promeniti da prezime drugog objekta bude drugačije I izbrisati prvi objekat. Ispisati podatke iz ShelveExample.
'''

#import modula
import shelve

#definisanje klase
class Person:
    #konstruktor
    def __init__(self,first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

    #metoda ispisa    
    def ispis(self):
        print("Ime: ",self.first_name," Prezime: ",self.last_name)


#instanciranje objekata
person1=Person("Pera","Peric")
person2=Person("Mika","Mikic")

#upisivanje objekata u fajl kao recnika, kljucevi su redni brojevi
with shelve.open("ShelveExample") as persones:
    persones['1']=person1
    persones['2']=person2

#promena prezimena el sa kljucem 2 i brisanje elementa sa kljucem 1
with shelve.open("ShelveExample") as persones:
    ime=persones['2'].first_name
    prezime='Markovic' 
    persones['2']={'first_name':ime,'last_name':prezime}
    del persones['1']

#ispis podataka iz fajla
with shelve.open("ShelveExample") as persones:
    for i in persones:
        print(i, persones[i]['first_name'], persones[i]['last_name'])
    
