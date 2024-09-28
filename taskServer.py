import socket 
import time 

sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockoptI(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSocket.bind(("localhost",8005))
sSocket.listen()
print("Server is listening..... ")
conn,addr = sSocket.accept()
conn.send(b"Hello and welcome")
prviBroj = int(conn.recv(256).decode("utf-8"))
drugiBroj = int(conn.recv(256).decode("utf-8"))
conn.send(bytes(f"{prviBroj+drugiBroj}","utf-8"))
sSocket.close()




