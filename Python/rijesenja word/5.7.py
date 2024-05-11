#Otvara se fajl sa citanje
with open('tekst.txt','r') as f:
    podaci=f.read()
    for karakter in podaci:
        if karakter==',':
            print('\n')
        else:
            print(karakter,end='')
            #Ako bismo zeleli da se automatski ne ispisuje novi red posle print funkcije mozemo podesiti sa 
            #end koji karakter ce se ispisivati. U ovom slucaju postavljamo prazan string 
