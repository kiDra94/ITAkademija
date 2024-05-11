def showAllView(lista):
    print ('U bazi imamo {} proizvoda'.format(len(lista)))
    for item in lista: print ("\t- {} {} {}".format(item['id_proizvoda'],item['ime_proizvoda'],item['cena_proizvoda'] ))

def ukupanRacun(lista):
    s=0
    for item in lista:
        s+=item['cena_proizvoda']
    print("Ukupna cena je {}".format(s))


def startView():
    print ('MVC - example start:')
def endView():
    print ('End.')
