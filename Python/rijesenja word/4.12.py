

def characters(s):
    for x in s:
        #metoda koja proverava da li karkater predstavlja slovo.
        if x.isalpha():
            yield x
            
            
s=input('Unesite string koji ce sadrzati i brojeve i karaktere: ')
for e in characters(s):
    print(e)