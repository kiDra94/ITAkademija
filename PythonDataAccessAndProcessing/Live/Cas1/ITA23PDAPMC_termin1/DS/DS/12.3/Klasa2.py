import random


class Rad_sa_listom:
    def kreiraj(self):
        return [random.randint(0, 10) for _ in range(10)]

    def obrada(self, lista):
        lista.sort()
        lista.reverse()

    def pisi(self, lista):
        print(lista)


if __name__ == "__main__":
    obj = Rad_sa_listom()
    lista = obj.kreiraj()
    obj.obrada(lista)
    obj.pisi(lista)
