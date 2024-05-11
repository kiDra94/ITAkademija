def funkcija(f):
    return f

def f():
    return 7

def f2(l):
    return sum(l)

izlazna_funkcija = funkcija(f())
print(izlazna_funkcija)
print(funkcija(f)())
izlazna_funkcija = funkcija(f2)
print(izlazna_funkcija([3, 4, 5]))
print(funkcija(f2)([3, 4, 5]))

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
