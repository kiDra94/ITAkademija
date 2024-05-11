import threading 
  
def calculate_cube(num): 
    print("Cube: {}".format(num * num * num)) 
  
def calculate_square(num): 
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": # if the main program started do this:
    # creating thread 
    t1 = threading.Thread(target=calculate_square, args=(10,)) 
    t2 = threading.Thread(target=calculate_cube, args=(10,)) 
  
    # start thread 1 
    t1.start() 
    # start thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!")

class Osoba:
    def __init__(self,ime,prezime,godine):
        self.ime=ime
        self.prezime=prezime
        self.godine=godine
         
    def ispis_imena(self):
        print("Osoba se zove : ",self.ime, " ", self.prezime)
     
    def ispis_godina(self):
        print("Osoba ima ",self.godine,' godina')
         
 
osoba1=Osoba('Pera','Peric',19)
if __name__ == "__main__": 
    t1 = threading.Thread(target=Osoba.ispis_imena, args=(osoba1,)) 
    t2 = threading.Thread(target=osoba1.ispis_godina) 
   
    t1.start() 
    t2.start()
     
    t1.join()
    t2.join()