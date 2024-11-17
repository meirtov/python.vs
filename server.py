import socket

sock=socket.socket()
ip="10.100.102.21"
port=8080
sock.bind((ip, port))
sock.listen(1)
print("server is listening")
connection, address= sock.accept()
connection.send("hello world".encode())
receivs_messege = connection.recv(1024)
print("recived new messege:()").format(receivs_messege)
connection.close()
sock.close