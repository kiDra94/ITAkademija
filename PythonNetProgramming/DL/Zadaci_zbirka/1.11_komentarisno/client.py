import socket
#importujemo socket bibiloteku koja je zadužena za osnove mrežne komunikacije u Pythonu i pomoću koje možemo kreirati sokete
import pickle
#importujemo biblioteku koja služi za serializovanje i uklanjanje serializacije Python objektnih struktura

server_port = 21060
#definisemo port preko kojeg će se odvijati komunikacija 
#portovi koji se zadaju na serverskoj i klijentskoj strani moraju biti isti

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Kreiramo objekat tipa soket sa parametrima 
#AF_INET – Ovim parametrom označavamo verziju internet protokola preko kojeg će se komunikacija odvijati. U ovom slučaju je to IPv4.
#SOCK_DGRAM – Ovim parametrom definišemo kog tipa će soket biti. U ovom slučaju, pošto je reč o UDP protokolu, tip soketa je UDP datagram (SOCK_DGRAM).

input_s = 12 
#definisemo poruku

#pakovanje podatka
d=pickle.dumps(input_s)

#slanje podatka na server
client_socket.sendto(bytes(d), ('127.0.0.1', server_port))

#primanje podatka sa servera
input_s_modified, address = client_socket.recvfrom(65535)

#raspakovanje podatka
modified_message = pickle.loads(input_s_modified)

print ('[CLIENT] Response from server {}, is: {}, type of modified message is {}'.format(address, modified_message,type(modified_message)))
#Ispisujemo poruku sa servera

#zatvaramo rucno soket koji sluzi za slanje 
client_socket.close()