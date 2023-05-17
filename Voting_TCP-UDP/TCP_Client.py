import socket 

c =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 1234
c.connect((host, port))
print(c.recv(1024).decode())
vote = input("\nEnter your vote \n A\tB\tC\n")
c.send(vote.encode())
print(c.recv(1024).decode())

c.close()
