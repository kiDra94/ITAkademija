def showAllView(lista):
    print ('In our db we have {} persons. Here they are:'.format(len(lista)))
    for item in lista: print ("\t- {}".format(item['ime']))
def startView():
    print ('MVC - example start:')
def endView():
    print ('End.')
