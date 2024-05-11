with open('brojevi2.txt','r') as ulaz:
    lines = ulaz.readlines()

with open('parni.txt','w') as izlaz:
    for l in lines:
        broj=int(l[0])    
        if broj%2==0:
            izlaz.write(l[0]+' PARAN\n')
        else:
            izlaz.write(l[0]+' NEPARAN\n')

    


    
