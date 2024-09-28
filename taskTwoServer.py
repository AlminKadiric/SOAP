import socket 
import time 
import random 



sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockoptI(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSocket.bind(("localhost",8005))
sSocket.listen()
print("Server is listening..... ")
conn,addr = sSocket.accept()
conn.send(b"Hello and welcome! This is a guessing game!")
zamisljeniBroj = random.randint(1,6)
korisnikovBroj = int(conn.recv(256).decode("utf-8"))

if zamisljeniBroj == korisnikovBroj:
    conn.send(bytes(f"Pogodili ste tacan broj je {zamisljeniBroj}").encode("utf-8"))
else:
    conn.send(bytes(f"Fulili ste!!!"))
sSocket.close()
