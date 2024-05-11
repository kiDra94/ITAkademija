import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from random import random


class KNN:
    def __init__(self, n):
        self.lista_tacaka = self.generisi_tacke(n)
        self.nova_tacka = (0, 0)
        self.d = self.dodeli_tackama_labele()

    def generisi_tacke(self, broj_tacaka):
        # return [(100 * np.random.normal(), 100 * np.random.normal()) for i in
        # range(broj_tacaka)]  # normalna raspodela tačaka
        return [(200 * random() - 100, 200 * random() - 100) for i in range(broj_tacaka)]  # ravnomerna raspodela tačaka

    def crtaj(self):
        x, y = zip(*self.lista_tacaka)
        plt.scatter(x, y, c=list(self.d.values()), s=50)
        plt.scatter(self.nova_tacka[0], self.nova_tacka[1], c="red", s=70)
        plt.savefig("slika_tacaka.png")
        plt.show()

    def dodeli_tackama_labele(self):
        return {i: 1 if i[0] > 0 else 0 for i in self.lista_tacaka}

    # statička metoda - rastojanje između dve tačke
    def rast(t1, t2):
        return sqrt((t1[0] - t2[0]) ** 2 + (t1[1] - t2[1]) ** 2)

    def rastojanje_od_tacaka(self):
        return {i: KNN.rast(i, self.nova_tacka) for i in self.lista_tacaka}

    def sortiraj_recnik(self, dict):
        keys = list(dict.keys())
        values = list(dict.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        return sorted_dict

    def najblizih_k_tacaka(self, k):
        return list(self.sortiraj_recnik(self.rastojanje_od_tacaka()))[:k]

    def pronadji_labele(self, k):
        return [self.d[i] for i in self.najblizih_k_tacaka(k)]

    def odluka(self, k):
        lista_labela = self.pronadji_labele(k)
        print(lista_labela)
        res = {key: lista_labela.count(key) for key in lista_labela}
        return max(res.items(), key=lambda kv: (kv[1], kv[0]))[0]


if __name__ == "__main__":
    broj_tacaka = 50
    obj = KNN(broj_tacaka)
    obj.crtaj()
    for k in range(3, 15, 2):
        print(f"Klasa odluke za k={k} je", obj.odluka(k))
