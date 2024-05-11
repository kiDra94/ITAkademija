import socket
import pickle

server_port = 21060
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', server_port))
print ('[SERVER] Listening at: {}'.format(server_socket.getsockname()))
while True:
    message, address = server_socket.recvfrom(65535)
    
    #raspakovanje podataka
    modified_message = pickle.loads(message)

    #modifikacija
    #modified_message=modified_message*modified_message

    #pakovanje podataka
    d=pickle.dumps(modified_message) #dodato
    
    print ('[SERVER] The client at {}, originally sent: {}'.format(address, repr(message)))

    #slanje podataka na client
    server_socket.sendto(bytes(d), address)

server_socket.close()
