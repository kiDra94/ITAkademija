import socket
import pickle

server_port = 21060
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', server_port))
print ('[SERVER] Listening at: {}'.format(server_socket.getsockname()))
while True:
    message, address = server_socket.recvfrom(65535)

    lista = pickle.loads(message)
    
    modified_message=[]

    for el in lista:
        if el not in modified_message:
            modified_message.append(el)
    
    d=pickle.dumps(modified_message) 

    server_socket.sendto(bytes(d), address)
server_socket.close()
