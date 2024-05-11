import random

tajni_broj=random.randint(1,100)


while True:
    broj=int(input('Unesite broj: '))
    if tajni_broj==broj:
        print('Bravo! Pogodio si broj, to je bio broj ',tajni_broj)
        break
    elif tajni_broj<broj:
        print("Tajni broj je manji od unetog broja")
    else:
        print("Tajni broj je veci od unetog broja")
