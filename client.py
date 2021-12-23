import socket

sock = socket.socket()
host = ''           #the IP address of the server shoul be added here
port = 6666

sock.connect((host, port))
print(sock.recv(1024).decode())
sock.close()