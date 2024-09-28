import socket 
sSocket = socket.bind(socket.AF_INET,socket.SOCK_STREAM)
sSocket.bind(("127.0.0.1",8005))
sSocket.listen()
print("Server is listening...")
sSocket.accept()