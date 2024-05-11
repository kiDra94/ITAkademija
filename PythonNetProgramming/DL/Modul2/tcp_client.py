import socket
port = 35789
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", port))
print("Client recived socket {}".format(client_socket.getsockname()))
client_socket.sendall(bytes("Hello, there, server!", encoding="utf8"))
input_s_modified = client_socket.recv(1024)
print("Server answerd {}".format(input_s_modified.decode("utf8")))
client_socket.close()