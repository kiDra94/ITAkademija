class Proizvod(object):
    def __init__(self, id_proizvoda = None, ime_proizvoda = None, cena_proizvoda=None):
        self.id_proizvoda = id_proizvoda
        self.ime_proizvoda = ime_proizvoda
        self.cena_proizvoda=cena_proizvoda

    def getAll(self):
        proizvodi = [{'id_proizvoda':1,'ime_proizvoda':'banane', 'cena_proizvoda':200},
            {'id_proizvoda':2,'ime_proizvoda':'jabuke', 'cena_proizvoda':250},
            {'id_proizvoda':3,'ime_proizvoda':'kruske', 'cena_proizvoda':100},
            {'id_proizvoda':4,'ime_proizvoda':'jagode', 'cena_proizvoda':500}]
        return proizvodi