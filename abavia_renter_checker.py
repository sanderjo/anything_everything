import sys
import telnetlib

HOST = sys.argv[1]

'''
$ telnet 94.232.116.140 nntp
Trying 94.232.116.140...
Connected to 94.232.116.140.
Escape character is '^]'.
200 Usenet.nl S.r.l.
quit
205 Bye. 22 bytes written, 0 accounted.
Connection closed by foreign host.
'''


tn = telnetlib.Telnet(HOST, 119, 3)

'''
tn.read_until(b"200")
tn.read_until()

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"quit\n")
'''

#print(tn.read_all())

print(tn.read_until(b"\n"))
#print(tn.read_all().decode('ascii'))

tn.write(b"quit\n")