import numpy
from scipy import stats

print("MEAN - MEDIAN - MODE")

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.mean(speed)
print("mean ", x)

x = numpy.median(speed)
print("median ", x)

x = stats.mode(speed)
print(x)


def aritmeticka_sredina(lista):
    return sum(lista) / len(lista)


def medijana(lista):
    lista.sort()
    return lista[len(lista) // 2] if len(lista) % 2 else (lista[len(lista) // 2] + lista[len(lista) // 2 - 1]) / 2


def most_frequent(lista):
    return max(set(lista), key=lista.count)


print("Mean: ", aritmeticka_sredina(speed))

print("Median: ", medijana(speed))

print("Mode: ", most_frequent(speed))

print("------------------------- PERCENTILE ----------------------------")

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
x = numpy.percentile(ages, 75)
print(x)

x = numpy.percentile(ages, 90)
print(x)


def perc(ages, proc):
    ages.sort()
    return ages[int(len(ages) * proc)]


print(perc(ages, 0.75))

print(perc(ages, 0.90))

print("---------------------------- VARIJANSA - STANDARDNO_ODSTUPANJE ---------------------")

speed = [32, 111, 138, 28, 59, 77, 97]

x = numpy.var(speed)  # varijansa
print(x)

x = numpy.std(speed)  # standardno odstupanje
print(x)

from math import sqrt


def var_std(lista):
    prosek = sum(lista) / len(lista)
    dis = 0
    for i in lista:
        dis += (i - prosek) ** 2
    dis /= len(lista)
    return dis, sqrt(dis)


print(var_std(speed))
