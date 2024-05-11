matrica=[]
for i in range(2):
    l1=[]
    for j in range(3):
        l1.append(int(input("Unesite element reda {0:d} kolone {1:d}: ".format(i+1,j+1) ) ) )
    matrica.append(l1)
    print("")


for i in range(2):
    for j in range(3):
        print(matrica[i][j],end=' ')  
    print("\n")
