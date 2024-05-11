matrica=[]

for i in range(3):
    l1=[]
    for j in range(3):
        l1.append(int(input("Unesite element reda {0:d} kolone {1:d}: ".format(i+1,j+1) ) ) )
    matrica.append(l1)
    print("")                   


s=0
for i in range(3):
    for j in range(3):
        if(i==j):
            s=s+matrica[i][j]
            
            
print("Suma elemenata na glavnoj dijagonali je ",s)



