import socket
sock = socket.socket()
sock.connect(("10.100.102.21", 8080))
message = sock.recv(1024)
print("recived new message:()".format(message))
sock.send("good bye".encode())
sock.close()