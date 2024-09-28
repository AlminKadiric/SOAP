import socket 
import time 
from random import random 


sSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sSocket.bind(("localhost",8005))
sSocket.listen()
print("Server is listening......")
conn, addr = sSocket.accept()
conn.send(b"DObrodosli u igru crtanja slova")
brojRedova = conn.recv(256).decode("utf-8").strip()
brojKolona = conn.recv(256).decode("utf-8").strip()
if brojRedova.isdigit() and brojKolona.isdigit():  # Validate that inputs are digits
    brojRedova = int(brojRedova)
    brojKolona = int(brojKolona)
else:
    print("Received invalid input for rows or columns")
    conn.send(b"Invalid input for rows or columns")

for red in range(brojRedova):
    for kolona in range(brojKolona):
        if red == 0 or kolona == brojKolona //2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
sSocket.close()
