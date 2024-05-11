#cas 7 matrice
a = [4, 3, 6, 8, 1, 2, 1]
print(a[::-1])
print(a[-1::-1])

mat = [[1,2],[2,3],[3,7]]
print(mat[1:])
print(mat[1:][1])
print(mat[1:][1][1])

a = [[]]*3 # pravi 3 prazne liste na istoj adresi!
print(a)
a[0].append(1)
#u ovom slucaju dodaje svuda keca zato sto je kroz mnozenje sve liste na istoj adresi
print(a[0]) #[1]
print(a) # [[1], [1], [1]]
#alternativa
b = [[],[],[]]
b[0].append(1)
print(b) #[[1], [], []]
# u ovom sluicaju ne djele istu memorisku adresu zato dodaje samo u b[0]

a = [2,3]
b = a
print(id(a))
print(id(b))
#ista je id adresa kad se ovako odradi
b[0] = 7
print(a) # a se mijenja zato sto su b i a na istoj adresi!!!
#rijesenje
a = [2,3]
b = a.copy() # kopira listu na novoj memorijskoj lokaciji!!!
print(id(a))
print(id(b))
b[0] = 7
print(a)
#pogledaj fajl matrice kopija sa casa!!!!









