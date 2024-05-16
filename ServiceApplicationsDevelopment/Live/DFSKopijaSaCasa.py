import xml.etree.ElementTree as ET

tree = ET.parse('country_data2.xml')
root = tree.getroot()
print(root.tag)
#print(list(root))
#for dete in list(root):
    #print(dete.tag)
lista = []
def pret_u_dub(cvor):
    deca = list(cvor)
    for i in deca:
        print(i.tag)
        if bool(i.attrib):
            print(i.attrib)
        if i.text is not None and str(i.text).strip()!="": #and str(i.text).strip()!="" sklanja sve bijeline i \n
            print(i.text)
        lista.append(str(i.text).strip())
        pret_u_dub(i)

pret_u_dub(root)
#!!!! nije provalio da je lista prazna!!!
print(lista)