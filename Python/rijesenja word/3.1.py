s1=input("Unesite prvi string: ")
s2=input("Unesite drugi string: ")

#Ispis stringova i njihovih duzina
print("Prvi string je ",s1,"i njegova duzina je: ",len(s1))
print("Drugi string je ",s2,"i njegova duzina je: ",len(s2))

#Ispis prvih i poslednjih karaktera stringova
print("Prvi karakter stringa: ",s1," je ",s1[0], ' a poslednji je: ',s1[-1])
print("Prvi karakter stringa: ",s2," je ",s2[0], ' a poslednji je: ',s2[-1])

#Konkatenacijom se spajaju stringovi
s=s1+','+s2
print(s)
