import socket
import pickle

PORT = 35780
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect(('127.0.0.1', PORT))
print ("[CLIENT] Client's has received from server its dedicated socket: {}".format(client_socket.getsockname()))

input_s={'hello':"World",
        'socket':'Server',
        'received':'Data'}
d=pickle.dumps(input_s)
client_socket.sendall(d)


client_socket.close()
