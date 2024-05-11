import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from random import random


def generisi_tacke(broj_tacaka):
    # return [(100 * np.random.normal(), 100 * np.random.normal()) for i in
    # range(broj_tacaka)]  # normalna raspodela tačaka
    return [(200 * random() - 100, 200 * random() - 100) for i in range(broj_tacaka)]  # ravnomerna raspodela tačaka

def crtaj(lista_tacaka, nova_tacka, boja_tacaka):
    x, y = zip(*lista_tacaka)
    plt.scatter(x, y, c=boja_tacaka, s=50)
    plt.scatter(nova_tacka[0], nova_tacka[1], c="red", s=70)
    plt.savefig("slika_tacaka.png")
    plt.show()

def dodeli_tackama_labele(lista_tacaka):
    return {i:1 if i[0] > 0 else 0 for i in lista_tacaka}

def rast(t1,t2):
    return sqrt((t1[0]- t2[0])**2 + (t1[1]- t2[1])**2)

def rastojanje_od_tacaka(lista_tacaka, nova_tacka):
    return {i: rast(i, nova_tacka) for i in lista_tacaka}

def sortiraj_recnik(dict): 
    keys = list(dict.keys())
    values = list(dict.values())
    sorted_value_index = np.argsort(values) #
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
    return sorted_dict

def najblizih_k_tacaka(lista_tacaka, nova_tacka, k):
    '''p = rastojanje_od_tacaka(lista_tacaka, nova_tacka)
    s = sortiraj_recnik(p)
    return list(s)[:k]'''
    return list(sortiraj_recnik(rastojanje_od_tacaka(lista_tacaka, nova_tacka)))[:k]

def pronadji_labele(lista_tacaka, nova_tacka, k, d):
    return [d[i] for i in najblizih_k_tacaka(lista_tacaka, nova_tacka, k)]

def odluka(lista_tacaka, nova_tacka, k, d):
    res = {key: pronadji_labele(lista_tacaka, nova_tacka, k, d).count(key) for key in pronadji_labele(lista_tacaka, nova_tacka, k, d)}
    return max(res.items(), key=lambda kv: (kv[1], kv[0]))[0]

if __name__=="__main__":
    broj_tacaka = 50
    lista_tacaka = generisi_tacke(broj_tacaka)
    d = dodeli_tackama_labele(lista_tacaka)
    nova_tacka = (0, 0)
    crtaj(lista_tacaka, nova_tacka, list(d.values()))
    k = 5
    # print(rastojanje_od_tacaka(lista_tacaka, nova_tacka))
    # print("########################")
    # print(sortiraj_recnik(rastojanje_od_tacaka(lista_tacaka, nova_tacka))) #sortirao je rijecnik po rastojanjima!
    # print(najblizih_k_tacaka(lista_tacaka, nova_tacka, 5))
    # print(pronadji_labele(lista_tacaka, nova_tacka, k, d))
    # print(odluka(lista_tacaka, nova_tacka, k, d))
    for k in range(3, 15, 2): #range od 3 do 15 sa korakom 2
        print(f"Klasa odluke za k={k} je", odluka(lista_tacaka, nova_tacka, k, d))