n = int(input("Unesite ceo broj:"))
 
s=0                          
   
for i in range(1, n+1):  
    if i % 6 == 0:       
        s = s + i       
          
print("Suma =", s)