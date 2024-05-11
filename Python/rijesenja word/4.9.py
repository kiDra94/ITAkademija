def dekoracija(funkcija):

    def wrapper():
        print("***************************")
        funkcija()
        print("***************************")

    return wrapper

@dekoracija
def moja_funkcija():
    print("Zdravo")

moja_funkcija()
