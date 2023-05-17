import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("UDP Socket created succesfully")

host = '127.0.0.1'
port = 5000

s.bind((host, port))
print(f"Server socket is binded to {port}")
print("Server is on")

A=0
B=0
C=0
n=0

while n<2:
    data, addr = s.recvfrom(1024)
    k = data.decode()
    print("Received 1 vote")
    print("Got data from ",addr)
    if (k == 'A'):
        A+=1
    elif (k =='B'):
        B +=1
    elif (k == 'C'):
        C+=1
    else:
        s.sendto("Wrong Vote".encode(), addr)
        n-=1
    s.sendto("Your vote has been counted\n Thank you for voting".encode(), addr)
    n+=1

s.close()        
print("The votes are : \n")
print(f"A={A}, B={B}, C = {C}")
