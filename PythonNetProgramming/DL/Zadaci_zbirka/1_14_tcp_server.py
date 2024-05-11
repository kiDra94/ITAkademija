import socket
import pickle

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
    
    modified_message=pickle.loads(message)
   
    
    print ('[TCP_SERVER] The client_socket at {}, originally sent  "{}"'.format(conn_socket.getpeername(), str(message)))
    for k,v in modified_message.items():
        print(k,v)

server_socket.close()
