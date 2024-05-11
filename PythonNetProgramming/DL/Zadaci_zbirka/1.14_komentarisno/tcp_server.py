#importujemo socket bibiloteku koja je zadužena za osnove mrežne komunikacije u Pythonu i pomoću koje možemo kreirati sokete
import socket
import pickle
#importujemo biblioteku koja služi za serializovanje i uklanjanje serializacije Python objektnih struktura


#pravimo prvi soket
##definisemo port preko kojeg će se odvijati komunikacija 
PORT = 35780
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Sam soket ćemo povezati na lokalnu adresu i port našeg uređaja komandom bind()
server_socket.bind(('127.0.0.1', PORT))
#Metoda listen() prima jedan parametar tipa int sa minimalnom vrednošću 1, gde taj broj predstavlja broj konekcija dozvoljenih ovom soket
server_socket.listen(1)

#Kako bi server u pravom momentu prepoznao primanje poruke, mora u svakom trenutku da proverava da li je poruka stigla pa koristimo beskonacnu petlju
while True:
    #Ispisujemo adresu i port soketa 
    print ('[TCP_SERVER] Listening at: {}'.format(server_socket.getsockname()))
    #Ova metoda je jedinstvena za TCP protokol i vraća novi soket objekat (novi soket objekat i njegovu adresu) – koji ćemo u kodu zvati conn_socket, jedinstven samo tom klijentu koji je uspostavio konekciju. 
    conn_socket, conn_sockname = server_socket.accept()
    
    #ispisujemo novi soket objekat
    print ('[TCP_SERVER] Connection is accepted from: {}'.format(conn_sockname))
    #ispisujemo tačnu adresu i port datog soketa i udaljenu adresu i port na koji je soket povezan
    print ('[TCP_SERVER] Socket connects: server_socket: {} and conn_socket: {}'.format(conn_socket.getsockname(), conn_socket.getpeername()))
    
    # serverski soket dolazi u stanje čekanja na prijem nove poruke koristeći metodu recv() i onda prima poruku kada je dobije
    message = conn_socket.recv(1024)
    
    #raspakovanje podataka
    modified_message=pickle.loads(message)
    
    #ispisujemo udaljenu adresu i port na koji je soket povezan i poruku
    print ('[TCP_SERVER] The client_socket at {}, originally sent  "{}"'.format(conn_socket.getpeername(), str(message)))
    
    #ispisujemo recnik
    for k,v in modified_message.items():
        print(k,v)

#zatvaramo rucno spoljasni soket
server_socket.close()
