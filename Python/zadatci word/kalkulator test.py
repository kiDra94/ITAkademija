import kalkulator

a=int(input("Unesite prvi ceo broj: "))
b=int(input("Unesite drugi ceo broj: "))

sabirak=kalkulator.saberi(a,b)
print("{}+{}={}".format(a,b,sabirak))

razlika=kalkulator.oduzmi(a,b)
print("{}-{}={}".format(a,b,razlika))

proizvod=kalkulator.pomnozi(a,b)
print("{}*{}={}".format(a,b,proizvod))

kolicnik=kalkulator.podjeli(a,b)
print("{}/{}={:.2f}".format(a,b,kolicnik))
