class Majka:
    def __init__(self,a):
        self.__a = a
    def pisi(self):
        print(self.__a)
    def promeni(self,a):
        self.__a = a
		
m = Majka(5)
m.b = 10 # OVDE SE PRAVI KOPIJA NA NIVOU OBJEKTA m
print(m.b)
#print(m.__a) # NE MOZE POSTO JE ATRIBUT PRIVATAN
m.__a = 7 # OVDE SE PRAVI KOPIJA NA NIVOU OBJEKTA m
print(m.__a) # ISPISUJE SE KOPIJA I SAD PRINT PROLAZI
m.pisi() # ISPISUJE SE NE PROMENJENA VREDNOST PRAVOG ATRIBUTA
m.promeni(9) # SADA JE PROMENJENA VREDNOST
m.pisi()  # ISPISUJE SE PROMENJENA VREDNOST PRAVOG ATRIBUTA