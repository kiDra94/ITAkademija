import socket
port = 35789
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", port))
server_socket.listen(1)

while True:
   conn_socket, conn_socketname = server_socket.accept()
   message = conn_socket.recv(1024)
   print("[SERVER] Message recived {}".format(message.decode("utf8")))
   modified_message = str(len(str(message).split(",")))
   print("[SERVER] Message from client: {}".format(modified_message))
   conn_socket.sendall(bytes(modified_message, encoding="utf8"))
   conn_socket.close()
server_socket.close()


