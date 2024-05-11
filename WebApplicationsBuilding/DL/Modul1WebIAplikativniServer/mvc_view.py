def showAllView(list):
    print ('In our db we have {} books. Here they are:'.format(len(list)))
    for item in list: print ("\t- {}".format(item['title']))
     
def startView():
    print ('MVC - example start:')
 
def endView():
    print ('End.')
