class Majka:

    def __init__(self,a,b):
        self.__a = a
        self.b = b

    def ispis(self):
        print(f"{self.__a} {self.b}") #__a znaci da je privatan objekat i da se ne moze direktno pristupiti

    def __str__(self):
        return f"{self.__a} {self.b}"

if __name__ == '__main__':
    obj = Majka(9,7)
    print(obj.__dict__)
    #print(obj.__a) #izbacuje gresku, posto je objekat privatan!
    print(obj.b)
    obj.ispis()
    print(obj)
