# importujemo biblioteku koja nam omogućava rad sa WebSocketima
import socketio  
 
ime = input("Tvoje ime je:") 
prezime=input("Tvoje prezime je:")

#WebSocket klijent objekat ćemo instancirati socketio.Client() pozivom i taj objekat smestiti u promenljivu sio_client
sio_client = socketio.Client()

#Definisemo funkciju za slanje poruka serveru
def send_msg():
    while True:
        poruka = input("Poruka: ")
        #funkcijom emit šaljemo (emitujemo) događaj sa porukom ka serveru.
        sio_client.emit('my_message', {'msg': poruka, 'name':ime,'surname':prezime})
        '''U ovoj funkciji su nam bitna dva parametra. 
        Prvi od njih, tipa string, predstavlja ime događaja koji šaljemo. Za to ime događaja na serverskoj strani treba da postoji funkcija sa istim takvim imenom koja će rukovati tim događajem. 
        Drugi parametar je tipa rečnik (u našem primeru je tipa rečnik, ali može biti str, bytes, list ili dict); preko njega možemo poslati željene podatke – u ovom slučaju želimo da pri svakom slanju pošaljemo korisnikovu poruku, kao i njegovo ime. 
        Dakle, ako emitujemo događaj po imenu my_message, na serverskoj strani moramo imati funkciju def my_message(): pass.'''
        
        sio_client.sleep(1) 
        #Cekamo sekund i opet pitamo korisnika da posalje poruku
 
#Funkciju connect dekorišemo sio_client.event funkcijom kako bi predstavlala dogadjaj
@sio_client.event
def connect():
    print('connection established')
    
    #ako se konektuje klient poziva se metoda send_msg za slanje poruka serveru
    send_msg() 

 
#Povezivanje na sam server ćemo jednostavno učiniti metodom sio_client.connect() kojoj prosleđujemo soket na koji se povezujemo (ip adresa:port).
sio_client.connect('http://localhost:5000')

 
sio_client.wait() 
#Cekamo dok server ne prekine konekciju
