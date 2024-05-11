a=int(input("Unesite prvi ceo broj: "))   
b=int(input("Unesite drugi ceo broj: ")) 

print("Prvi broj je %d, drugi broj je %d" %(a,b))

#Prvi nacin korišćenjem pomoćne promenljive
c=a #Pomocna promenljiva sada ima vrednost promenljive a
a=b #Promenljiva a ce sada imati vrednost promenljive b jer njenu vrednost cuvamo u pomocnoj promenljivi
b=c #Promenljiva b ce sada imati vrednost promenljive c (odn. staru vrednost promenljive a) jer njenu vrednost cuvamo u promenljivi a

print("Nakon prve izmene: ")
print("Prvi broj je %d, drugi broj je %d" %(a,b))


#Drugi način-moguće samo u Python-u
a,b=b,a
print("Nakon druge izmene(vrednosti su iste kao na pocetku): ")
print("Prvi broj je %d, drugi broj je %d" %(a,b))
