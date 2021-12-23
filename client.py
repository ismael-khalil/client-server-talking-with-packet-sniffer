import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''           #the IP address of the server shoul be added here
port = 6666

sock.connect((host, port))
print(sock.recv(1024).decode())
sock.close()
