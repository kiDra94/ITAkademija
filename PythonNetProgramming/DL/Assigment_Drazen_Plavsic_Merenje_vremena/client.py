import socket
import time

server_port = 21060
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

messages = [
    "Hello, server!",               
    str(12345),                     
    str(3.14),                      
    "Provjeravanje razlicitih velicina poruka!"]

for input_s in messages:
    start_time = time.time()
    client_socket.sendto(bytes(input_s, encoding='utf8'), ('127.0.0.1', server_port))
    input_s_modified, address = client_socket.recvfrom(65535)
    end_time = time.time()
    response_time = end_time - start_time
    print('[CLIENT] Response from server {}, is: "{}"'.format(address, str(input_s_modified.decode('utf8'))))
    print('[CLIENT] Response time: {:.6f} seconds'.format(response_time))

client_socket.close()