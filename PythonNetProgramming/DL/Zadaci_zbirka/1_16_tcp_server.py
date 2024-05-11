import socket, sys

import pickle

PORT = 35780
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
    
    
    lista=pickle.loads(message)
    p=0
    n=0
    for el in lista:
        if el<0:
            n+=1
        else:
            p+=1
    
    if(p>n):
        rec="Pozitivnih ima vise od negativnih"
    elif(p<n):
        rec="Pozitivnih ima manje od negativnih"
    else:
        rec="Pozitivnih ima isto kao i negativnih"

    print ('[TCP_SERVER] The client_socket at {}, originally sent  "{}"'.format(conn_socket.getpeername(), message))
    modified_message = str(rec)
    conn_socket.sendall(bytes(modified_message, encoding = 'utf8'))
    conn_socket.close()
    print ("[TCP_SERVER] Reply sent, closing client's socket.")

server_socket.close()

