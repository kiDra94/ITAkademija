#polazna ideja da se pravi samo jedan objekat; ide se preko metode!!!
#class moze da se zove kako hoce; npr konekcija!
class Singelton:
    
    instanca = None

    def __init__(self) -> None:
        Singelton.instanca = self

    @staticmethod
    def instanciraj():
        if Singelton.instanca == None:   
            Singelton()
        return Singelton.instanca
a = Singelton()
print(id(a))
b = Singelton()
print(id(b))
c = Singelton.instanciraj()
print(id(c))
d = Singelton.instanciraj()
print(id(d))
'''ovo je korisno ako hocemo da imamo samo jedan objeket, npr log in; stalno poziva vec postujuci objekat!
instanciraj provjera da li je instanca = none; tj ako objekat ne postoji on ga pravi, ako postoji koristi istu
memorijsku lokaciju; u sustini stalno vidimo iste objekte!!!'''
print("--------------------------------------")
#privatni konstruktor; python ga simulira
class Singelton_private:
    
    instanca = None

    def __init__(self) -> None:
        if Singelton_private.instanca != None:
            raise Exception ("This class is a singelton")
        else:
            Singelton_private.instanca = self

    @staticmethod
    def instanciraj():
        if Singelton_private.instanca == None:   
            Singelton_private()
        return Singelton_private.instanca
a = Singelton_private()
print(id(a))
#b = Singelton_private() #puca program, posta ne moze da ga pravi, posto objekat vec postji
#print(id(b))
c = Singelton_private.instanciraj()
print(id(c))
d = Singelton_private.instanciraj()
print(id(d))
#jedan objekat se moze praviti preko konstruktura; svi ostali se svode na taj 1 posto init provjerava da li objekat postoji!!!
print("--------------------------------------")