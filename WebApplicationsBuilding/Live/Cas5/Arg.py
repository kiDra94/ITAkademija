def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

myfunc(2, 7, 9, 10)

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

myfunc2(a=3, b=7, c="Simboli")

def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()


myfunc3(2, 7, 9, 10, a=3, b=7, c="Simboli")