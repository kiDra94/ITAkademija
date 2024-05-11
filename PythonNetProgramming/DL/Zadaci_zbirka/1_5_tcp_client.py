import socket
PORT = 35780
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect(('127.0.0.1', PORT))
print ("[CLIENT] Client's has received from server its dedicated socket: {}".format(client_socket.getsockname()))

input_s='Hello, there, server!'
client_socket.sendall(bytes(input_s, encoding = 'utf8')) 
reply = client_socket.recv(1024)
print ('[CLIENT] Response from the server: "{}"'.format(reply.decode('utf8')))
client_socket.close()
