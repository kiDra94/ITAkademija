#Napravili smo calculator modul i sada ga pozivamo
import calculator

a=int(input("Unesite prvi ceo broj: "))
b=int(input("Unesite drugi ceo broj: "))

#Poziva se metoda saberi iz modula calculator
sabirak=calculator.saberi(a,b)
print("{}+{}={}".format(a,b,sabirak))

razlika=calculator.oduzmi(a,b)
print("{}-{}={}".format(a,b,razlika))

proizvod=calculator.pomnozi(a,b)
print("{}*{}={}".format(a,b,proizvod))

kolicnik=calculator.podeli(a,b)
print("{}/{}={}".format(a,b,kolicnik))

