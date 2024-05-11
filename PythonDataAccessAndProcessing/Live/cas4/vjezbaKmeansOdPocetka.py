import random
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt


def generisi_tacke(broj_tacaka):
    lista_tacaka = []
    for i in range(broj_tacaka):
        lista_tacaka.append((100*random.random(), 100*random.random()))
    return lista_tacaka

#bez numpy moze i ovako
#X = unzipeed_list = list(zip(*lista_tacaka))
#zip list uzima x koordinate i stavlja u jednu torku, y koordinate i stavlja u drugu torku
#plt.scatter(X[0], X[1], s=50)

def crtaj(lista_tacaka, lista_centara):
    T = np.array(lista_tacaka)
    C = np.array(lista_centara)
    #print(T)
    #print(C)
    plt.scatter(T[:,0], T[:,1],c="blue", s=50)
    plt.scatter(C[:,0], C[:,1],c="red", s=70)
    plt.show()

def crtaj_poslije_podjele(lista_tacaka, lista_centara, d):
    T = np.array(lista_tacaka)
    C = np.array(lista_centara)
    #print(T)
    #print(C)
    plt.scatter(T[:,0], T[:,1],c=list(d.values()), s=50) #oznacava boju na osnovu indexa centra kome pripada
    plt.scatter(C[:,0], C[:,1],c="red", s=70)
    plt.show()

def generisi_centre(broj_centara):
    lista_centara = []
    for i in range(broj_centara):
        lista_centara.append((20*random.random()+40, 20*random.random()+40)) # centri izmedju 40-60 da se ne poklapaju
    return lista_centara

def dodeli_tackama_centre(lista_tacaka,lista_centara):
    '''d = {}
    for i in lista_tacaka:
        d[i] = 0'''
    d = {i:0 for i in lista_tacaka}
    for i in range(len(lista_tacaka)):
        mini = rast(lista_tacaka[i],lista_centara[0]) #mi smo proglasili da je mini rastojanje, rastojanje od 0og centra
        index = 0
        for j in range(1, len(lista_centara)): #ide od 1 posto je 0 vec proglaseno, tj poredi sa centrom 1 2 i 3
            if rast(lista_tacaka[i],lista_centara[j]) < mini:
                mini = rast(lista_tacaka[i],lista_centara[j]) 
                index = j
        d[lista_tacaka[i]] = index
    return d

def pronadji_nove_centre(d): #mozemo isto da prosljedimo broj centara kao argument pronadji_nove_centre(d, broj_centara)
    bc = len(set(list(d.values()))) # pravimo listu svih klaster, set brise duplikate, len od 0,1,2,3 je 4!
    #print(bc)
    tacke_od_centara = [[i for i in d if d[i]==j] for j in range(bc)]
    #print(sum(len(i) for i in tacke_od_centara)) #provjera koliko tacaka imamo!
    #umjesto centar0x, centar0y  = list(zip(*tacke_od_centara[0])) --> moze i da se napravi np.array
    centar0x, centar0y  = list(zip(*tacke_od_centara[0])) #pravi 2 liste, jednu sa x i jednu sa y koordinatama
    #print(np.mean(centar0x), np.mean(centar0y))
    nova_lista_centara = []
    for i in range(bc):
        centarX, centarY  = list(zip(*tacke_od_centara[i]))
        nova_lista_centara.append((np.mean(centarX), np.mean(centarY)))
    return nova_lista_centara
    
def crtanje_sa_pomjeranjem_centara(stari_centri):
    while(True):
        novi_centri = pronadji_nove_centre(d)
        crtaj_poslije_podjele(lista_tacaka, novi_centri, d)
        if novi_centri == stari_centri:
            break
        stari_centri = novi_centri

def rast(a,b): #rastojanje!!!!
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    

if __name__ == '__main__':
    broj_tacaka = 200
    broj_centara = 4
    lista_tacaka = generisi_tacke(broj_tacaka)
    stari_centri = generisi_centre(broj_centara) #prvi centri koje generisemo
    crtaj(lista_tacaka, stari_centri)
    d = dodeli_tackama_centre(lista_tacaka, stari_centri)
    crtaj_poslije_podjele(lista_tacaka, stari_centri, d)
    crtanje_sa_pomjeranjem_centara(stari_centri)


