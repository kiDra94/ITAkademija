sam = 'aoeiu'
rec = 'Idemo dalje danas'.lower()
sam_skup = set(sam)
rec_skup = set(rec)
print(sam_skup)
print(rec_skup)
print(sam_skup.intersection(rec_skup))
print(''.join(sam_skup.intersection(rec_skup))) #prave ope string!

def zajednicki(sam: str, rec: str) -> str:
    return ''.join(set(sam).intersection(set(rec)))

print(zajednicki('asdjhsa', 'ne bi bilo lose da se to ovako uradi'))