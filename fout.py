import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('news.eweka.nl', 119))

print("1", s)
s.close()
print("2", s)

s.sendall(b"HELP\r\n\r\n")
data = s.recv(1024)
print(data)
s.close()


