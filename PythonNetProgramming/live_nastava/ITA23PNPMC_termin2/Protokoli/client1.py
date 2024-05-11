import socket

#pokreni server ovdje, onda preko cmd pokreni clyent, tek onda ce se server ugasiti

sClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sClient.connect(("127.0.0.1",8005))
sClient.close()