#prvi nacin

drzave_gradovi={
    'Srbija':'Beograd',
    'Hrvatska':'Zagreb',
    'Bosna i Hercegovina':'Sarajevo'
    }


tacnost=False
for kljuc in drzave_gradovi:
    if kljuc=='Srbija':
        tacnost=True
        
if tacnost==True:
    print("Gravni grad Srbije je ",drzave_gradovi['Srbija'])
else:
    print("Drzava Srbija se ne nalazi u rečniku")


#drugi nain

drzave_gradovi={
    'Srbija':'Beograd',
    'Hrvatska':'Zagreb',
    'Bosna i Hercegovina':'Sarajevo'
    }

print(drzave_gradovi.get('Srbija', 'Drzava Srbija se ne nalazi u rečniku'))

