import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
host = '127.0.0.1'
port = 1234
s.bind((host, port))
print("TCP Socket binded to %s" %(port))
s.listen(5)
print("Socket is listening")

A=0
B=0
C=0
n=0
while n < 2:
    c, addr = s.accept()
    print("Got connection from ",addr)
    c.send("Welcome to voting portal ".encode())
    k = c.recv(1024).decode()
    print("Received 1 vote")
    if (k == 'A'):
        A+=1
    elif (k =='B'):
        B +=1
    elif (k == 'C'):
        C+=1
    else:
        c.send("Wrong Vote".encode())
        n-=1
    c.send("Your vote has been counted, thank you for voting".encode())
    n+=1
    c.close()
s.close()
print("Total votes : ")
print(f"A = {A}, B = {B}, C = {C}")
