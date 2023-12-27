#!/usr/bin/env python3

'''
Find public IPv4 and IPv6 of this client
'''


import requests # needed, as it works with cloudflare
import socket
import sys

testhost = "self-test.sabnzbd.org"
testbaseURL = "/"

testhost ="www.appelboor.com"
testbaseURL = "/cgi-bin/what_is_my_ip.py"

'''
$ curl -4 "https://www.appelboor.com/cgi-bin/what_is_my_ip.py?ipv4-forced" 
44.44.54.18

$ curl -6 "https://www.appelboor.com/cgi-bin/what_is_my_ip.py?ipv6-forced" 
2001:4444:ff00:0:3e2d:3615:0:1

'''

# baseurl = "www.appelboor.com/cgi-bin/what_is_my_ip.py"

#  easy request ... but does not specify ipv4 or ipv6:

r = requests.get(f"https://{testhost}/{testbaseURL}?noippreference")
print(r.content.decode('utf-8'))

# force-connect via IPv4 address
testhostipv4 = socket.getaddrinfo(testhost, 443, family=socket.AF_INET, proto=socket.IPPROTO_TCP)[0][4][0] # First ipv4 address of testhost
r = requests.get(f"http://{testhostipv4}{testbaseURL}?ipv4test", headers={'host': testhost}) # http, not https ... TODO get it working with https
print("Public IPv4:", r.content.decode('utf-8'))

# force-connect via IPv6 address
testhostipv6 = socket.getaddrinfo(testhost, 443, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)[0][4][0] # First ipv6 address of testhost
r = requests.get(f"http://[{testhostipv6}]{testbaseURL}?ipv6test", headers={'host': testhost}) # http, not https
print("Public IPv6:", r.content.decode('utf-8'))

