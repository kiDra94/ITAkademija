korpa={'banane':53,'jabuke':55,'jagode':59,'visnje':52,'pomorandze':56}

voce=input('Unesite ime voca koje zelite da izbacite: ')
if voce in korpa:
    #Prvi nacin brisanja para iz recnika
    korpa.pop(voce)
    
    #Drugi nacin
    #del(korpa[voce])
    
    print(korpa)
else:
    print('Voce se ne nalazi u korpi')