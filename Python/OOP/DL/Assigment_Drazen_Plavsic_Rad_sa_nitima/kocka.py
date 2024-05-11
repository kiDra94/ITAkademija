import threading 

class Kocka():

    def __init__(self, stranica):
        self.stranica = int(stranica)
  
    def zapremina(self): 
        v = self.stranica ** 3
        print(f"Zapremina kocke iznos {v}")
    
    def duzina(self): 
        duzina = self.stranica * 12
        print(f"Duzina kocke iznos {duzina}") 
    
if __name__ == "__main__":
    k = Kocka(10)
    k1 = Kocka(5)
    t1 = threading.Thread(target=k.zapremina) 
    t2 = threading.Thread(target=k.duzina) 
    t3 = threading.Thread(target=k1.zapremina) 
    t4 = threading.Thread(target=k1.duzina) 

    t2.start()
    t1.start()
    t4.start()
    t3.start()

    t2.join()
    t1.join()
    t4.join()
    t3.join()

    print("Gotovo!!!")

