#!/usr/bin/env python3

'''
Find public IPv4 and IPv6 of this client
'''


import requests
import socket

testhost = "self-test.sabnzbd.org"

#  easy request:
#r = requests.get("https://" + testhost)
#print(r.content)


testhostipv4 = socket.getaddrinfo(testhost, 443, family=socket.AF_INET, proto=socket.IPPROTO_TCP)[0][4][0] # First ipv4 address of testhost
r = requests.get(f"http://{testhostipv4}/#ipv4" , headers={'host': testhost})
print(r.content.decode('utf-8'))

testhostipv6 = socket.getaddrinfo(testhost, 443, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)[0][4][0] # First ipv6 address of testhost
r = requests.get(f"http://[{testhostipv6}]/#ipv6" , headers={'host': testhost})
print(r.content.decode('utf-8'))
