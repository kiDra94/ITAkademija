import socket
#importujemo socket bibiloteku koja je zadužena za osnove mrežne komunikacije u Pythonu i pomoću koje možemo kreirati sokete

server_port = 21060
#definisemo port preko kojeg će se odvijati komunikacija 
#portovi koji se zadaju na serverskoj i klijentskoj strani moraju biti isti

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Kreiramo objekat tipa soket sa parametrima 
#AF_INET – Ovim parametrom označavamo verziju internet protokola preko kojeg će se komunikacija odvijati. U ovom slučaju je to IPv4.
#SOCK_DGRAM – Ovim parametrom definišemo kog tipa će soket biti. U ovom slučaju, pošto je reč o UDP protokolu, tip soketa je UDP datagram (SOCK_DGRAM).

input_s='abcdefABCDEF'
#definisemo poruku

client_socket.sendto(bytes(input_s, encoding='utf8'), ('127.0.0.1', server_port))
#saljemo poruku pomocu sendto metode:
# prvi argument je poruka koju želimo da pošaljemo tipa bajt, u UTF-8 kodnom rasporedu
# drugi argument je torka od dva elementa, koja sadrži adresu na koju šaljemo, kao i port procesa na mašini koja se nalazi iza te adrese. U našem slučaju, adresa je 127.0.0.1.


povratni_string, address = client_socket.recvfrom(65535)
#u promenljivoj address su nam adresa i port servera, a u promenljivoj input_s_modified se nalazi odgovor servera
'''bafer predstavlja pomoćnu memoriju i u ovom slučaju ta memorija se koristi za smeštanje odgovora
servera. Vrednost koju smo prosledili (65535) nije slučajna i predstavlja veličinu bafera izraženu u bajtovima. 
Takođe, ta cifra je po specifikaciji protokola teorijski limit veličine poruke koja se može preneti UDP-om. 
Ako pokušamo da pošaljemo poruku veću od limita, doći će do greške''' 


print ('[CLIENT] Response from server {}, is: \n'.format(address))
#Ispisujemo poruku sa servera, odn. adresu i string koji dekodiramo

print("Izmenjen string: {}".format(povratni_string))
#Ispisujemo poruku sa servera

#zatvaramo rucno soket koji sluzi za slanje 
client_socket.close()
