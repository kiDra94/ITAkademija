import socket
#importujemo socket bibiloteku koja je zadužena za osnove mrežne komunikacije u Pythonu i pomoću koje možemo kreirati sokete
import pickle
#importujemo biblioteku koja služi za serializovanje i uklanjanje serializacije Python objektnih struktura


server_port = 21060
#definisemo port preko kojeg će se odvijati komunikacija 
#portovi koji se zadaju na serverskoj i klijentskoj strani moraju biti isti

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Kreiramo objekat tipa soket sa parametrima 
#AF_INET – Ovim parametrom označavamo verziju internet protokola preko kojeg će se komunikacija odvijati. U ovom slučaju je to IPv4.
#SOCK_DGRAM – Ovim parametrom definišemo kog tipa će soket biti. U ovom slučaju, pošto je reč o UDP protokolu, tip soketa je UDP datagram (SOCK_DGRAM).

server_socket.bind(('127.0.0.1', server_port))
#Pomocu metode bind procesu naše aplikacije dodeljujemo broj porta na kome ce se osluskivati

print ('[SERVER] Listening at: {}'.format(server_socket.getsockname()))
#Ispisujemo adresu i port soketa preko kog osluskujemo



#Kako bi server u pravom momentu prepoznao primanje poruke, mora u svakom trenutku da proverava da li je poruka stigla pa koristimo beskonacnu petlju
while True:
    #Cuvamo poruku i adresu koju smo dobili od servera 
    message, address = server_socket.recvfrom(65535)

    #raspakovanje podataka
    lista = pickle.loads(message)
    
    #modfikacija
    modified_message=[]

    for el in lista:
        if el not in modified_message:
            modified_message.append(el)
    
    #pakovanje podataka
    d=pickle.dumps(modified_message) 

    #slanje podataka na client
    server_socket.sendto(bytes(d), address)

#zatvaramo soket rucno
server_socket.close()
