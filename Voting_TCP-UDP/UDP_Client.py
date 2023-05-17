import socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 5000
vote = input("Enter your vote\n A\tB\t\tC\n")
c.sendto(vote.encode(), (host, port))
print(c.recvfrom(1024)[0].decode())
c.close()
