import socket
import sys
port = 63453
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    print("Successfully connected")
except socket.error as err:
    print(f"an {err} has occurred. Please try again")


server.bind(("",port))
print("Socket binded to: ",port)
count = 0


while True:
    server.listen(5)
    print("Waiting for connection...")
    c, addr = server.accept()
    count+=1
    print("Got connection from ", addr)
    c.send("Thank you for connecting".encode())
    message = c.recv(1024).decode()
    print(message)
    
    if message == "thanks for letting me connect":
        c.send("No Problem bro".encode())
        
    else:
        c.send("Nice manners Bro :(".encode())

    symbol_list = ["+", "-", "*", "/"] 
    integer1 = c.recv(1024).decode()
    integer2 = c.recv(1024).decode()
    symbol = c.recv(1024).decode()
    if symbol not in symbol_list:
        c.send("Symbol Not Applicable\nClosing the connection".encode())
    else:
        integer1 = int(integer1)
        integer2 = int(integer2)
        if symbol == "+":
            result = integer1 + integer2
        elif symbol == "-":
            result = integer1 - integer2
        elif symbol == "*":
            result = integer1 * integer2
        else:
            result = integer1 / integer2
        print(f"Result for client {count} is {result}")
        c.send(str(result).encode())
    print(f"Connection with client {count} completed successfully")


    
    #server.close()
    #break

    
"""if server <0:
    print("Error")
    sys.exit()
print("SUccessfully connected")"""