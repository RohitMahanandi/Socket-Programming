import socket
port = 63453
import sys
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
server.connect(("172.16.19.209", port))
#server.bind(("",port))
while True:
    print(server.recv(1024).decode())
    firstmessage = "whatever"
    server.send(firstmessage.encode())
    print(server.recv(1024).decode())
    integer1 = int(input("Enter first Integer: "))
    server.send(str(integer1).encode())
    integer2  = int(input("Enter second Integer: "))
    server.send(str(integer2).encode())
    symbol = input("Enter symbol: ")
    server.send(str(symbol).encode())

    print(server.recv(1024).decode())
    print(f"Connection with server completed successfully")
    server.close()
    break
