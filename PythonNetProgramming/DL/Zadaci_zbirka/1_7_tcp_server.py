import socket
PORT = 35780
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', PORT))
server_socket.listen(1)
while True:
    print ('[TCP_SERVER] Listening at: {}'.format(server_socket.getsockname()))
    conn_socket, conn_sockname = server_socket.accept()
    
    print ('[TCP_SERVER] Connection is accepted from: {}'.format(conn_sockname))
    print ('[TCP_SERVER] Socket connects: server_socket: {} and conn_socket: {}'.format(conn_socket.getsockname(), conn_socket.getpeername()))
    
    message = conn_socket.recv(1024)
    print ('[TCP_SERVER] The client_socket at {}, originally sent  "{}"'.format(conn_socket.getpeername(), message.decode('utf8')))
    
    message=str(message)
    
    print(message[-2])
    if(message[-2]=='.'):
        odgovor='Da'
    else:
        odgovor='Ne'

    conn_socket.sendall(bytes(odgovor, encoding = 'utf8'))
    conn_socket.close()
    print ("[TCP_SERVER] Reply sent, closing client's socket.")

server_socket.close()
