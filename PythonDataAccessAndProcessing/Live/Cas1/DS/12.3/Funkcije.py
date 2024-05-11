def apply(func: object, value: object) -> object:
    return func(value)


apply(print, 42)  # 42

print(apply(print, 42))  # 42 None

print(apply(id, 42))  # neki_int

print(apply(type, 42))  # <class 'int'>

print(apply(len, "Marwin"))  # 6

print(apply(type, apply))  # <class 'function'>


def outer():
    def inner():
        print('This is inner.')

    print('This is outer, invoking inner.')
    inner()  # unutrasnja funkcija se moze pozvati samo unutar spoljasnje


outer()

print("-----------------------")


def outer():
    def inner():
        print('This is inner.')

    print('This is outer, returning inner.')
    return inner  # ovo ne poziva funkciju inner vec je samo vraca


i = outer()
print(type(i))
i()

print("-----------------------")


def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()


def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()


def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()


myfunc(2, 7, 9, 10)

myfunc2(a=3, b=7, c="Simboli")

myfunc3(2, 7, 9, 10, a=3, b=7, c="Simboli")

print("----------------------------------")

def neka_funkcija():
    print("Neka funkcija")

def vrati_prosirenu_funkciju(polazna_funkcija):
    def prosirena_funkcija():
        polazna_funkcija()
        print("Dodatak")
    return prosirena_funkcija

a = vrati_prosirenu_funkciju(neka_funkcija)() 

vrati_prosirenu_funkciju(neka_funkcija)()

neka_funkcija()

# vrati_prosirenu_funkciju - dekorater
# polazna_funkcija - dekorisana funkcija