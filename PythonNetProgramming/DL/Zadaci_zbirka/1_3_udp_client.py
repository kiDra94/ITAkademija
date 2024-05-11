import socket

server_port = 21060

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

input_s = 'Welcome to the 2021 year'

client_socket.sendto(bytes(input_s, encoding='utf8'), ('127.0.0.1', server_port))

povratni_string, address = client_socket.recvfrom(65535)

lista=str(povratni_string).split(" ")
print(lista)

print ('[CLIENT] Response from server {}, is: \n'.format(address))
print("String sadrzi: {} razmaka, {} broja/brojeva".format(lista[0],lista[1]))


client_socket.close()
