import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1234))
with open("newfile.txt") as f:
    for line in f:
        s.sendall(line.encode())
