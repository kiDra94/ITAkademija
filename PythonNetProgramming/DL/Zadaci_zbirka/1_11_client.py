import socket
import pickle

server_port = 21060
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

input_s = {'a':1}

#pakovanje podatka
d=pickle.dumps(input_s)

#slanje podatka na server
client_socket.sendto(bytes(d), ('127.0.0.1', server_port))

#primanje podatka sa servera
input_s_modified, address = client_socket.recvfrom(65535)

#raspakovanje podatka
modified_message = pickle.loads(input_s_modified)

print ('[CLIENT] Response from server {}, is: {}, type of modified message is {}'.format(address, modified_message,type(modified_message)))