#importujemo socket bibiloteku koja je zadužena za osnove mrežne komunikacije u Pythonu i pomoću koje možemo kreirati sokete
import socket
import pickle
#importujemo biblioteku koja služi za serializovanje i uklanjanje serializacije Python objektnih struktura


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
input_s={'hello':"World",
        'socket':'Server',
        'received':'Data'}

#pakovanje podataka
d=pickle.dumps(input_s)

#Pomocu metode sendall saljemo ceo podatak i ne brinemo da li ce se poslati ceo ili ne
client_socket.sendall(d)

#zatvaramo rucno soket koji sluzi za slanje
client_socket.close()
