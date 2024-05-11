class Osoba(object):
    osobe=[]
    def __init__(self, maticni_broj=None, ime = None, godina_upisa = None):
        while True:
            odg=input("Da li zelite da unesete novu osobu(da/ne): ")
            if odg=='da' or odg=='Da' or odg=="DA":
                osoba={}
                osoba['maticni_br']=int(input("Unesite maticni br: "))
                osoba['ime']=input("Unesite ime: ")
                osoba['godiina_upisa']=input("Unesite godinu upisa")

                self.osobe.append(osoba)
            else:
                break

    def getAll(self):
        return self.osobe
