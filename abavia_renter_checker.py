import sys
import telnetlib

try:
    HOST = sys.argv[1]
except:
    HOST = "94.232.116.140"

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

def get_nntp_welcome(HOST):

    try:
        tn = telnetlib.Telnet(HOST, 119, 1)
        welcome_msg = tn.read_until(b"\n").decode()[4:].strip()
        #print(welcome_msg)
        tn.write(b"quit\n")
        return welcome_msg
    except:
        return None

subnet = "94.232.116."
for i in range(111,255):
    ip = subnet + str(i)
    response = get_nntp_welcome(ip)
    if response:
        print(ip, response)