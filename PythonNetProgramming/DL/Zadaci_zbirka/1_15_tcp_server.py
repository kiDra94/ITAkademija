import socket, sys

import pickle

PORT = 35781
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', PORT))
server_socket.listen(1)
while True:
    print ('[TCP_SERVER] Listening at: {}'.format(server_socket.getsockname()))
    conn_socket, conn_sockname = server_socket.accept()
    print ('[TCP_SERVER] Connection is accepted from: {}'.format(conn_sockname))
    print ('[TCP_SERVER] Socket connects: server_socket: {} and conn_socket: {}'.format(
        conn_socket.getsockname(), conn_socket.getpeername()))
    message = conn_socket.recv(1024)
    
    string = pickle.loads(message)

    recnik={}
    for slovo in string:
        if slovo not in recnik:
            recnik[slovo]=1
        else:
            recnik[slovo]+=1

    
    d=pickle.dumps(recnik)
    conn_socket.sendall((d))
    conn_socket.close()
    print ("[TCP_SERVER] Reply sent, closing client's socket.")

server_socket.close()

