import socket

server_port = 21060

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(('127.0.0.1', server_port))

print ('[SERVER] Listening at: {}'.format(server_socket.getsockname()))

while True:
    message, address = server_socket.recvfrom(65535)
    message=str(message)
    string=''
    #Prolazimo petljom kroz svaki karakter stringa message
    for el in message:
        #Pomocu metode isupper() proveravamo da li karakter predstavlja veliko slovo
        if(el.isupper()):
            #Pomocu metode lower() menjamo karakter tako da predstavlja malo slovo
            string+=el.lower()
        #Pomocu metode islower() proveravamo da li karakter predstavlja veliko slovo
        if(el.islower()):
            #Pomocu metode upper() menjamo karakter tako da predstavlja veliko slovo
            string+=el.upper()
        #Pomocu metode isspace() proveravamo da li karakter predstavlja razmak
        if(el.isspace()):
            string+='*'

    string=str(string)
    print ('[SERVER] The client at {}, originally sent: {}'.format(address, repr(message)))
    server_socket.sendto(bytes('Server is sending back: "{}".'.format(string), encoding='utf8'), address)

server_socket.close()
