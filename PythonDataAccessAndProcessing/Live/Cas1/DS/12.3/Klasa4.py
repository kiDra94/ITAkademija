import random


class Rad_sa_listom:

    def __init__(self):
        print("Poziva se konstruktor...")
        self.lista = self.kreiraj()
        # self.lista = [random.randint(0, 10) for _ in range(10)]
    def kreiraj(self):
        return [random.randint(0, 10) for _ in range(10)]

    def obrada(self):
        self.lista.sort()
        self.lista.reverse()

    def pisi(self):
        print(self.lista)

    def __str__(self):
        return str(self.lista)

print(__name__)
if __name__ == "__main__":
    obj = Rad_sa_listom()
    lista = obj.kreiraj()
    obj.obrada()
    obj.pisi()
    print(obj)
