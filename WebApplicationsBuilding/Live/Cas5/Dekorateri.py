def neka_funkcija():
    print("Neka funkcija")

def vrati_prosirenu_funkciju(polazna_funkcija):
    def prosirena_funkcija():
        polazna_funkcija()
        print("Dodatak")
    return prosirena_funkcija

a = vrati_prosirenu_funkciju(neka_funkcija)
a()
vrati_prosirenu_funkciju(neka_funkcija)()

#neka_funkcija()

