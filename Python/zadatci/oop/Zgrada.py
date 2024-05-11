#isti cas kao opp5 i opp6
#dodaj za svaku klasu jos po neku stavku cisto da vjezbas
#definise tip koji predstavlja vlasnika
class Vlasnik:

    def __init__(self, ime, prezime, jmbg):
        self.__ime = ime
        self.__prezime = prezime
        self.__jmbg = jmbg

    def __str__(self):
        return 'Ime i prezime: {} {} JMBG: {}'.format(self.__ime,self.__prezime, self.__jmbg)
   
    def jmbg(self):
        return self.__jmbg

# da li ime ili prezime sadrzi kljucnu rec
    def ime_sadrzi(self, upit):
        ime_ok = self.__ime.find(upit) != -1
        prezime_ok = self.__prezime.find(upit) != -1
        return ime_ok or prezime_ok

# definise tip koji predstavlja stanove
class Stan:

    def __init__(self, m2, sprat):
        self.__m2 = m2
        self.__sprat = sprat
        self.__vlasnik = None

    def __str__(self):
         st = '{}m2 spr. {}'.format(self.__m2, self.__sprat)
         return '{}. {}'.format(st, str(self.__vlasnik))

    def vlasnik(self):
        return self.__vlasnik

    def promeni_vlasnika(self, novi_vlasnik):
        self.__vlasnik = novi_vlasnik

    def povrsina(self):
        return self.__m2

class Zgrada:
 
    def __init__(self, adresa, stanovi):
        self.__adresa = adresa
        self.__stanovi = stanovi
 
    def __str__(self):
        opis = [str(stan) for stan in self.__stanovi]
        return '{}\n---\n{}\n---\n'.format(self.__adresa, opis)
 
    def dodaj_stan(self, stan):
        self.__stanovi.append(stan)
 
    # vraca recnik sa vlasnicima koji zadovoljavaju upit
    # i njihovim stanovima
    def stanovi_vlasnika(self, upit):
        vlasnik_stanovi = {} # recnik sa stanovima po vlasniku
        for stan in self.__stanovi:
            v = stan.vlasnik()
            if v != None and v.ime_sadrzi(upit):
                v_stanovi = vlasnik_stanovi.get(v.jmbg(), [])
                v_stanovi.append(stan)
                vlasnik_stanovi[v.jmbg()] = v_stanovi
        return vlasnik_stanovi
 
 
if __name__=='__main__':
    v1 = Vlasnik("Ana","Ivanovic","3435346457457")
    print(v1)
    print(v1.jmbg())
    print(v1.ime_sadrzi("nov"))
    st = Stan(70,3)
    st.promeni_vlasnika(v1)
    print(st)
    v2 = Vlasnik("Novak","Djokovic","3333333333333")
    st.promeni_vlasnika(v2)
    print(st)
    st1 = Stan(80,5)
    st1.promeni_vlasnika(v1)
    print(st1)
    zgrada = Zgrada('Radnicka 4', [st, st1])
    print("-------------------")
    v3 = Vlasnik("Simo", "Perin", "5414151566")
    v4 = Vlasnik("Jovo", "Simin", "5414654566")
    v5 = Vlasnik("Pero", "Jovin", "5416518788")
    st2 = Stan(65,3)
    st3 = Stan(213,10)
    st4 = Stan(54,6)
    st5 = Stan(180,9)
    st2.promeni_vlasnika(v3)
    st3.promeni_vlasnika(v4)
    st4.promeni_vlasnika(v5)
    st5.promeni_vlasnika(v2)
    zgrada.dodaj_stan(st2)
    zgrada.dodaj_stan(st3)
    zgrada.dodaj_stan(st4)
    zgrada.dodaj_stan(st5)
    print(zgrada)
