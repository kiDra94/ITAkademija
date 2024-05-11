a=5
b=3

zbir = a + b
razlika = a - b
proizvod = a * b


print(zbir, razlika, proizvod)
#Ispisivanje samo promenljivih

print("Zbir",zbir, "Razlika ",razlika, "Proizvod ", proizvod,'\n') 
#Ispisivanje stringova u kombinaciji sa promenljivama. 
#Karakter \n ispisuje novi red

#Svaka {} se zamenjuje argumentima format metode. Prva zagrada se zamenjuje sa vrednoscu promenljive zbir, druga sa vrednoscu promenljive razlika...
print("Zbir {} Razlika {} Proizvod {}" .format(zbir , razlika , proizvod))

#Mozemo definisati i raspored ispisa time sto pisemo broj unutar zagrade. 
#Prva zagrada bice zamenjena sa prvim argumentom format metode, druga sa 3. argumentom a treca sa 2. argumentom
print("Zbir {0} Proizvod {2} Razlika {1}" .format(zbir , razlika , proizvod))


#Mozemo definisati i tip podatka: d-ceo broj, f-realan broj. 
print("Zbir {0:d} Razlika {1:d} Proizvod {2:d}" .format(zbir , razlika , proizvod))

#Jos jedan nacin ispisa jeste uz pomoć % gde unutar stringa navodimo skraćenicu za tip a posle navodnika navodimo vrednosti koje ce biti ispisane
print("Zbir %d Razlika %d Proizvod %d "%(zbir, razlika, proizvod))
