import xml.etree.ElementTree as ET

tree = ET.parse('1.xml')
root = tree.getroot()
print(root.tag)
# print(list(root))
# for dete in list(root):
# print(dete.tag)

lista = []


def pret_u_dub(cvor):
    deca = list(cvor)
    for i in deca:
        print(i.tag)
        if bool(i.attrib):
            print(i.attrib)
            for j in i.attrib.keys():
                print(i.attrib.get(j))
        if i.text is not None and str(i.text).strip() != "":
            print(i.text)
        lista.append(str(i.text).strip())
        pret_u_dub(i)


pret_u_dub(root)
print(lista)
