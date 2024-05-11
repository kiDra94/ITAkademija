sam = 'aoeiu'
rec = 'Idemo dalje danas'.lower()
sam_skup = set(sam)
print(sam_skup)
rec_skup = set(rec)
print(rec_skup)
print(sam_skup.intersection(rec_skup))
print(''.join(sam_skup.intersection(rec_skup)))

def zajednicki(sam: str, rec: str) -> str:
    return ''.join(set(sam).intersection(set(rec)))

print(zajednicki(sam,rec))