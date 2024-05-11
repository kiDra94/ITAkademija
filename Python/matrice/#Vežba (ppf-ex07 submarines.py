#Vežba (ppf-ex07 submarines.py)
m = 10
submariens = [3,5,3,6,7,6,8,6,2,1,2,2]
sub = []
'''nije mi jasno kako da ugradim podmornicu u petlju; 
jasno mi je da se jedna podmornica krece od submariens[0:3] tj na svaka 4 parceta slica, 
ali nikkao da provalim kako da ugradim u petlju. znam da se ova donja petlja moze isto napisatu s jednim printomm,
ali sam ostavio odvojeno posto msm da nece mozda raditi ako dodam podmornice, da se ne buni sto za iste koordinate
ima vise vrijednosti (da ima " " i podmornicu)'''
for y in range(m):
    for x in range(m):
        if y == 0 or x == 0 or y == m-1 or x == m-1:
            print("*", end="") # U zavisnosti od verzije koju koristite mozete dodati end="" kako biste dobili ispis samo u jednom redu, odn. print ne bi ispisao novi red posle ispisa karaktera
        else:
            print(" ", end="") # U zavisnosti od verzije koju koristite mozete dodati end="" kako biste dobili ispis samo u jednom redu, odn. print ne bi ispisao novi red posle ispisa karaktera
    print("")
# potrebno je da napravite funkciju koja ce da ispita da ako nije granica da li se tacna nalazi unutar podmornice ili izvan. Ako se nalazi unutar onda ispisujemo broj a ako ne onda ispisujemo razmak

# do sada ste dobili ovaj izgled
# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********

# mozete nastaviti na ovaj nacin ili uraditi ga na ovaj drugi nacin:

# Ovde transformišemo niz submariens u listu torki submarines. Svaka torka sadrži četiri elementa: (x1, y1, x2, y2), koji predstavljaju koordinate početne i krajnje tačke svake podmornice.
submarines = [(submariens[i], submariens[i+1], submariens[i+2], submariens[i+3]) for i in range(0, len(submariens), 4)]

'''
Ova funkcija prima x, y koordinate i listu submarines. Njen zadatak je da proveri da li se tačka sa datim koordinatama nalazi na nekoj od podmornica.
enumerate(submarines) vraća parove (index, (x1, y1, x2, y2)) za svaku podmornicu, gde je index redni broj podmornice u listi.
Za svaku podmornicu, proveravamo da li je vertikalna (ako su x1 i x2 isti) ili horizontalna (u suprotnom). Ako tačka pripada podmornici, funkcija vraća True i broj podmornice (index + 1, jer indeksiranje u Pythonu počinje od 0).'''

def is_submarine_part(x, y, submarines):
    for index, (x1, y1, x2, y2) in enumerate(submarines):
        if x1 == x2:
            # Vertikalna podmornica
            if x == x1 and y1 <= y <= y2:
                return True, index + 1
        else:
            # Horizontalna podmornica
            if y == y1 and x1 <= x <= x2:
                return True, index + 1
    return False, 0


'''
Ovaj deo koda crta matricu. Dve ugnježdene petlje prolaze kroz svaku koordinatu matrice (x, y).
Ako je x ili y na ivici matrice (0 ili m-1), ispisuje se * kako bi se formirao okvir.
Ako tačka nije na ivici, proveravamo da li je deo podmornice koristeći funkciju is_submarine_part.
Ako je tačka deo podmornice, ispisuje se broj podmornice. U suprotnom, ispisuje se prazan prostor (" ").
print("") na kraju svake unutrašnje petlje prelazi u novi red, formirajući strukturu matrice.'''
for y in range(m):
    for x in range(m):
        if y == 0 or x == 0 or y == m-1 or x == m-1:
            print("*", end="")
        else:
            is_sub, sub_number = is_submarine_part(x, y, submarines)
            if is_sub:
                print(sub_number, end="")
            else:
                print(" ", end="")
    print("")







'''Vežba (ppf-ex07 displaymatrix.py)
Vežba (ppf-ex07 knight.py)
Vežba (ppf-ex07 transform.py)
ove 3 vjezbe nisam ni pocinjao posto sam ubjedjen da bez shvatanja kako da dodajem elemente u matrici nema svrhe da probavam'''
#Vežba (ppf-ex07 matrixaddition.py)

# a = [[3,5,3],[6,7,6],[8,6,2]]
# b = [[3,5,3],[6,7,6],[8,6,2]]
# c = []
# for i in range(len(a)):
#     d = []
#     for j in range(len(a[0])):
#         d.append((a[i][j]) + (b[i][j]))
#     c.append(d)
# for i in c:
#     print(i)
# #ne znam da li je ovo najelegantniji nacin za rijesiti, pa ako moze bolje posaljite kod
# #Vežba (ppf-ex07 matrixmul.py)
# a = [1, 2]
# b = [[3, 4], [5, 6]]

# b0 = sum(row[0] for row in b)
# b1 = sum(row[1] for row in b)

# rezultat = [a[0] * b0, a[1] * b1]

# print(rezultat)

# #ja sam ovdje unakrsno sabrao b pa onda to sve pomnozio sa a; siguran sam da to moze i lijepse pa ako ste radi da mi objasnite bio bih zahvalan


