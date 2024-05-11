n = int(input("Unesite duzinu horizontalne stranice: "))
m = int(input("Unesite duzinu vertikalne stranice: "))
 
for i in range(0,  m):      
    for j in range(0, n):   
        if (i == 0 or i == m - 1 or j == 0 or j == n - 1):  
            print("*", end='')     
        else:
            print(" ", end='')     
    print("")