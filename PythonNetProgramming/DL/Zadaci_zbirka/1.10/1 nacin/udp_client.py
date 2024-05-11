import socket
from datetime import datetime

server_port = 21060

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

input_s='Hello, my name is Charlie Chaplin'

curr_time = datetime.now()
formatted_time = curr_time.strftime('%H:%M:%S:%f')
print(formatted_time)

client_socket.sendto(bytes(input_s, encoding='utf8'), ('127.0.0.1', server_port))

povratni_string, address = client_socket.recvfrom(65535)

print ('[CLIENT] Response from server {}, is: \n'.format(address))
print("Izmenjen string: {}".format(povratni_string))

curr_time = datetime.now()
formatted_time = curr_time.strftime('%H:%M:%S:%f')
print(formatted_time)

client_socket.close()
