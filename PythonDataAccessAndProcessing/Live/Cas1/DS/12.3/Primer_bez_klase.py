import random
def kreiraj():
    return [random.randint(0, 10) for _ in range(10)]
def obrada(lista):
    lista.sort()
    lista.reverse()
def pisi(lista):
    print(lista)

if __name__ == "__main__":
    lista = kreiraj()
    obrada(lista)
    pisi(lista)
