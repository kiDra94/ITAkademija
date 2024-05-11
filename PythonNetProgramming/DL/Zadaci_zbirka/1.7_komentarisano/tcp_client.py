#Prve 3 linije TCP klijenta su dosta slične sa UDP klijentom:
#importujemo socket bibiloteku koja je zadužena za osnove mrežne komunikacije u Pythonu i pomoću koje možemo kreirati sokete
import socket
PORT = 35780

#definisemo port preko kojeg će se odvijati komunikacija 
#portovi koji se zadaju na serverskoj i klijentskoj strani moraju biti isti
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Kreiramo objekat tipa soket sa parametrima 
#AF_INET – Ovim parametrom označavamo verziju internet protokola preko kojeg će se komunikacija odvijati. U ovom slučaju je to IPv4.
# SOCK_STREAM – Ovim parametrom definišemo kog tipa će soket biti. U ovom slučaju, pošto je reč o TCP protokolu, tip soketa je TCP datagram (SOCK_STREAM).

#Zahtevamo muđusobnu konekciju pre komunikacije, bez toga nema slanja podataka 
#Metoda connect() prima za parametar n-torku sa dva elementa:
#adresu na kojoj server očekuje konekciju;
#broj porta preko kojeg će se odvijati konekcija.
client_socket.connect(('127.0.0.1', PORT))

#ispisujemo metodom getsockname tačnu adresu i port datog soketa
print ("[CLIENT] Client's has received from server its dedicated socket: {}".format(client_socket.getsockname()))

#definisemo poruku za slanje
input_s='Danas je divan dan.'

#Pomocu metode sendall saljemo ceo podatak i ne brinemo da li ce se poslati ceo ili ne
#Poruka koju želimo da pošaljemo tipa bajt, u UTF-8 kodnom rasporedu
client_socket.sendall(bytes(input_s, encoding = 'utf8')) 

#Odgovor sa servera se dobavlja pomoću recv() metode
reply = client_socket.recv(1024)

#ispisujemo poruku sa servera
print ('[CLIENT] Response from the server: "{}"'.format(reply.decode('utf8')))

#soket zatvaramo rucno metodom close()
client_socket.close()
