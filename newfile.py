import socket
cSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cSocket.connect(("localhost",8005))

cSocket.send(b"Hey man, whats up?")
cSocket.sendall(b"Are u there?")


cSocket.close()
