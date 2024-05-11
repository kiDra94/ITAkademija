'''Zadatak 1.5.  Napraviti klasu Person koja konstruktorom definiše ime I prezime. Instancirati 2 objekta.
 Upisati objekte u fajl ShelveExample pomoću Shelve modula. 
 Ključevi treba da budu stringovi koji predstavljaju redni broj objekta a vrednosti treba da budu objekti. 
 Promeniti da prezime drugog objekta bude drugačije I izbrisati pri objekat. Ispisati podatke iz ShelveExample.
'''


import shelve

class Person:
    def __init__(self,first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
    
    def ispis(self):
        print("Ime: ",self.first_name," Prezime: ",self.last_name)

person1=Person("Pera","Peric")
person2=Person("Mika","Mikic")

with shelve.open("ShelveExample") as persones:
    persones['1']=person1
    persones['2']=person2

with shelve.open("ShelveExample") as persones:
    ime=persones['2'].first_name
    prezime='Markovic' 
    persones['2']={'first_name':ime,'last_name':prezime}
   
    del persones['1']

with shelve.open("ShelveExample") as persones:
    for key in persones:
        print(key, persones[key]['first_name'], persones[key]['last_name'])
    
