import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from random import randint
from random import random

class KNN:
    def __init__(self, n, k, nova_tacka):
        self.__n = n # broj tacaka
        self.__k = k # k najblizih suseda
        self.__nova_tacka = nova_tacka
        self.__lista_tacaka = self.__generisi_tacke()
        self.d = self.__dodeli_tackama_labele() # recnik - tacka:labela

    
    # function to set value of _age 
    def set_k(self, a): 
        self.__k = a 
        

    # privatna metoda
    def __generisi_tacke(self):
        #return [(100 * np.random.normal(), 100 * np.random.normal()) for i in
        #range(broj_tacaka)]  # normalna raspodela tačaka
        return [(200 * random() - 100, 200 * random() - 100) for i in range(self.__n)]  # ravnomerna raspodela tačaka

    def crtaj(self):
        x,y = zip(*self.__lista_tacaka)
        plt.scatter(x, y, c=list(self.d.values()), s=50)
        plt.scatter(self.__nova_tacka[0],self.__nova_tacka[1], c="red", s=70)
        plt.show()

    def __dodeli_tackama_labele(self):
        return {i:1 if i[0]>0 else 0 for i in self.__lista_tacaka}

    @staticmethod
    def rastojanje_izmedju_dve_tacke(t1, t2):
        return sqrt((t1[0]-t2[0])**2+(t1[1]-t2[1])**2)

    # rastojanje nove tacke od svih tacaka
    def rastojanje_od_tacaka(self):
        return {i:KNN.rastojanje_izmedju_dve_tacke(i,self.__nova_tacka) for i in self.__lista_tacaka}

    # sortiranje recnika sa rastojanjima do tacaka
    def sortiraj_recnik(self,d):
        keys = list(d.keys())
        values = list(d.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        return sorted_dict

    # izvlacenje prvih k najblizih tacaka 
    def najblizih_k_tacaka(self):
        return list(self.sortiraj_recnik(self.rastojanje_od_tacaka()))[:self.__k]

    # vraca labele najblizih k tacaka
    def pronadji_labele(self):
        return [self.d[i] for i in self.najblizih_k_tacaka()]
    
    def odluka(self):
        lista_labela = self.pronadji_labele()
        print(lista_labela)
        res = {key: lista_labela.count(key) for key in lista_labela}
        return max(res.items(), key=lambda kv: (kv[1], kv[0]))[0]


if __name__=="__main__":
    knn = KNN(50, 5, (0,0)) # (br_tacaka, k, nova_tacka)
    knn.crtaj()
    for k in range(3,21,2): # k = 3,5,7,9,...,19
        knn.set_k(k)
        print(knn.odluka())
     


    