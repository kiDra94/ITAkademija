matrica=[]

for i in range(3):
    l1=[]
    for j in range(3):
        l1.append(int(input("Unesite element reda {0:d} kolone {1:d}: ".format(i+1,j+1) ) ) )
    matrica.append(l1)
    print("")                   


br=0
for i in range(3):
    for j in range(3):
        if(matrica[i][j]<0):
            br+=1
            
            
print("Broj negativnih elemenata je ",br)

