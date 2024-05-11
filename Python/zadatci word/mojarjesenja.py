with open('brojevi2.txt','r') as ulaz:
    podaci=ulaz.readlines()
    
with open('parni.txt','w') as izlaz:
    for l in podaci: 
        broj=int(l[0])  
        if broj%2 == 0:
            izlaz.write(l[0]+ " " + "Paran\n")
        else: 
            izlaz.write(l[0]+ " " + "Neparan\n")
