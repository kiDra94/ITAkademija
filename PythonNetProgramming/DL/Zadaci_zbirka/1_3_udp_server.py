import socket

server_port = 21060

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(('127.0.0.1', server_port))

print ('[SERVER] Listening at: {}'.format(server_socket.getsockname()))

while True:
    message, address = server_socket.recvfrom(65535)
    message=str(message)
    povratni_string=''
    razmaka=0
    brojeva=0
    for i in range(len(message)):
        #Pomocu metode isspace() proveravamo da li karakter predstavlja razmak
        if(message[i].isspace()):
            razmaka+=1
        #Pomocu metode isdigit() proveravamo da li karakter predstavlja cifru
        if(message[i].isdigit()):
            brojeva+=1
    povratni_string+=str(razmaka)+' '+str(brojeva)

    print ('[SERVER] The client at {}, originally sent: {}'.format(address, repr(message)))
    server_socket.sendto(bytes(povratni_string, encoding='utf8'), address)
server_socket.close()
