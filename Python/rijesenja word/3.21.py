meseci = {'jan': 31, 'feb': 28, 'mart': 31, 'april': 30, 'maj': 31, 'jun': 30, 'jul': 31, 'aug': 31, 'sept': 30, 'okt': 31, 'nov': 30, 'dec': 31 }

vrednosti=[]
kljucevi=[]

for kljuc in meseci:
    kljucevi.append(kljuc)
    vrednosti.append(meseci[kljuc])
    
print(kljucevi)
print(vrednosti)