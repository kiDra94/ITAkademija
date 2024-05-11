import socket
import pickle

server_port = 21060
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

input_s = [1,5,6,3,4,8,0,3,2,5]

d=pickle.dumps(input_s)

client_socket.sendto(bytes(d), ('127.0.0.1', server_port))
input_s_modified, address = client_socket.recvfrom(65535)

modified_message = pickle.loads(input_s_modified)


print ('[CLIENT] Response from server {}, is: {}, type of modified message is {}'.format(address, modified_message,type(modified_message)))


client_socket.close()