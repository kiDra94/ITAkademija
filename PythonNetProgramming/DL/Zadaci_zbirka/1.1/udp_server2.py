import socket 
#importujemo socket bibiloteku koja je zadužena za osnove mrežne komunikacije u Pythonu i pomoću koje možemo kreirati sokete

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
    #poruku pretvaramo u string
    #message=str(message)
    #message = message.decode('utf8')
    message = message.decode('utf8')
    string=message.swapcase().replace(' ', '*')

    
    #ispisujemo sta je client poslao i sa koje adrese
    print ('[SERVER] The client at {}, originally sent: {}'.format(address, repr(message)))
    
    #saljemo poruku poruku u obliku bajt objekta u UTF-8 kodnom rasporedu, zajedno sa adresom na koju šaljemo
    server_socket.sendto(bytes('Server is sending back: "{}".'.format(string), encoding='utf8'), address)

#zatvaramo soket rucno
server_socket.close()
