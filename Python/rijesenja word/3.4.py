s='a.b.c.d.e'

#Razdvajanje stringa. Povratna vrednost je lista ciji su elementi stringovi
l=s.split('.')
#Pravimo prazan string koji cemo da kreiramo spajanjem stringova liste
print(l)
s1=''
for el in l:
    s1=s1+el
print(s1)
