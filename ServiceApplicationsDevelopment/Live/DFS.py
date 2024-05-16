#depth first search , prvo pretraga u dubinu
import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()
print(root.tag)
# print(list(root)) #ispisuje listu neposredne djece od root-a

# for dete in list(root):
    # print(dete.tag)


lista = []
#rekurzivna pretraga u dubinu
def pret_u_dubinu(cvor):
    deca = list(cvor)
    for i in deca:
        print(i.tag) # ipsisuje imena tagova
        if bool(i.attrib): # vraca true ako postoji, u sustnini znaci, if i.attrib true!
            print(i.attrib) # ispisuje kljuc vrijednost atributa, ako ga ima
        # if bool(i.text): #isot kao ispod
        if i.text is not None and str(i.text).strip()!="": #and str(i.text).strip()!="" sklanja sve bijeline i \n
            print(i.text)
        lista.append(str(i.text).strip())
        pret_u_dubinu(i)



if __name__ == "__main__":
    pret_u_dubinu(root)
    #lista ne readi!!!!
    print(lista)