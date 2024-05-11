#OOP
class Auto:
    brzina = 190
    boja = "Crvena"
    agregat = "Diesel"
    broj_mesta = 5

print(Auto.brzina)
print(Auto.broj_mesta)

jugo = Auto()
print(jugo.boja)
pezo = Auto()
print(pezo.boja)

class Auto2:
    def __init__(self,bojanka,brzina = 150):
        self.brzina = brzina
        self.boja = bojanka

    def pisi(self):
        print("Opis: ",self.boja,self.brzina)

    def vrati_boju(self):
        return self.boja
    
    def postavi_boju(self,nova_boja):
        self.boja = nova_boja
    
    def __str__(self):
        return "Osobine su: "+ str(self.brzina)+ " " + self.boja

jugo = Auto2("Plava",200)
print(jugo.boja,jugo.brzina)
pezo = Auto2("Crvena",180)
print(pezo.boja,pezo.brzina)
nn_auto = Auto2("Siva")
print(nn_auto.boja,nn_auto.brzina)
jugo.pisi()
pezo.pisi()
print(jugo.vrati_boju())
print(jugo)
print(jugo.__dict__)
jugo.postavi_boju("Metalik")
print(jugo)
print(jugo.__dict__["brzina"])