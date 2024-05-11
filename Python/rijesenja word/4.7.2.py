#Prvi nacin 
# Tako sto spajamo konkatenacijom karaktere cifara i +
# Na kraju moramo skratiti string za 1 karakter kako ne bismo imali + kao poslednji karakter
def napravi():
    s=''
    for i in range(1,10):
        s+=str(i)+'+'
    print(s[:-1])

#Drugi nacin
# Tako što u praznu listu dodajemo stringove koji predstavljaju karaktere cifara
# Na kraju spajamo elemente liste u jedan string između kojih će se nalaziti karakter +
def napravi2():
    lista=[]
    for i in range(1,10):
        lista.append(str(i))

    krajnj_string = '+'.join(lista)
    print(krajnj_string)

napravi()
napravi2()        
