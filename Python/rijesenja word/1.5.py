s1=input("Unesite prvi string: ")
s2=input("Unesite drugi string: ")

#Prvi nacin samo ispisom elemenata.
#Ispisace se prvi string pa karakter zarez zatim pa onda drugi string kada ih razdvajamo zarezom
print(s1,',',s2)

#Drugi nacin
#konkatenacija stringova-sabiranje odn. spajanje stringova
print(s1+','+s2)    

#Treci nacin
#Koriscenjem format ispisa
print("{0:s},{1:s}".format(s1,s2))

#Cetvrti nacin
print("{},{}".format(s1,s2))

#Peti nacin
print("%s,%s"%(s1,s2))

