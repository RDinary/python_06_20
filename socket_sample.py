import socket

site = 'www.int-college.co.il'

a = socket.gethostbyname(site)
print(a)

b = socket.gethostbyname_ex(site)
print(b)

site = input("enter site: ")
# validation: if site is legal then print
try:
    print(socket.gethostbyname(site))
except socket.gaierror:
    print("first, build this website")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 80

s.connect((site, port))
request = "GET / HTTP/1.1\r\nHOST: " + site + "\r\n\r\n"
s.sendall(request.encode())
result = s.recv(1500)
with open("result_file.txt", "w") as rf:
    rf.write(result.decode())

myserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myserver.bind(("0.0.0.0", 1234))
myserver.listen(1)

while True:
    print("waiting")
    client, address = myserver.accept()
    print(f"Hello {address}")
    while result := client.recv(1024):
        print("client sent: " + result.decode())
    client.close()
