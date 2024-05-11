with open('reci1.txt','r') as ulaz:
    podaci=ulaz.readlines()
    
with open('reci2.txt','w') as izlaz:
    for rec in podaci:
        slovo1=rec[0]
        slovo2=rec[1]
    
        if slovo1!=slovo2:
            ispis=slovo1+slovo2 + '\n'
            izlaz.write(ispis)
        
    
