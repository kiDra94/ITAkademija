import socket
import pickle
PORT = 35781
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect(('127.0.0.1', PORT))
print ("[CLIENT] Client's has received from server its dedicated socket: {}".format(client_socket.getsockname()))

s="Hellooooo OOO"
d=pickle.dumps(s)

client_socket.sendall((d)) 
reply = client_socket.recv(1024)
modified_message = pickle.loads(reply)
print ('[CLIENT] Response from the server: ', reply)
client_socket.close()
