#Otvara se fajl sa pisanje
with open('izlaz2.txt','w') as f:
    f.write('Pera\n')
    f.write('Peric')
    
    #Drugi nacin
    f.write('Pera\nPeric')
    
    #Treci nacin
    f.write('Pera' + '\n' + 'Peric')
    