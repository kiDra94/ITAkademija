a = 2
if(a==3):
    print("JESTE 3")
else:
    print("NIJE 3 nego je",a) #ovo je jedan blok; zato sto pripada IFu; linija ispod nije dio bloka, posto ne zavisi od IF
print("procitaj komentar")

print(type(a)) #type provjerava kojeg je tipa a, u ovom slucaju INT
b = 9.3 
print(type(b)) # b je float
c = "Nesto"
print(type(c)) # c je str
d = True
print(type(d)) # d je bool; kad imas samo 2 mogucnosti (da ili ne)
print(a+b) #pretvara u ovom slucaju sve u isti tip kako bi mogao da sabere!; izvrsava inplicitnu konverziju
#print(b+c) #TypeError: unsupported operand type(s) for +: 'float' and 'str'; nije moguce izvrsiti konverziju 
print(str(b)+c) #posto linja 16 ne moze sama zbog stringa, moramo da sami izvrsimo konverziju
print(int(b)) # konverzija iz floata u int, odsjeca zaraz

s = input("Unesi neki broj: ") #korisnik mora da unese broj, konzola ispod
print(s) 
print(type(s)) #str!

# Python program to print the list of all keywords

# importing the module
import keyword

# printing the keywords
print("Python keywords are...")
print(keyword.kwlist)


'''e = int(input("Unesi prvi broj: "))
f = int(input("Unesi drugi broj: "))
g = e + f
print(g)
print(type(g)) vidi fajl calculator!
'''
