#!/usr/bin/env python3

'''
Find public IPv4 and IPv6 of this client
'''


import requests # needed, as it works with cloudflare
import socket

testhost = "self-test.sabnzbd.org"

#  easy request:
r = requests.get("https://" + testhost)
print(r.content)


# connect via IPv4 address
testhostipv4 = socket.getaddrinfo(testhost, 443, family=socket.AF_INET, proto=socket.IPPROTO_TCP)[0][4][0] # First ipv4 address of testhost
r = requests.get(f"http://{testhostipv4}/#ipv4" , headers={'host': testhost})
print(r.content.decode('utf-8'))

# connect via IPv6 address
testhostipv6 = socket.getaddrinfo(testhost, 443, family=socket.AF_INET6, proto=socket.IPPROTO_TCP)[0][4][0] # First ipv6 address of testhost
r = requests.get(f"http://[{testhostipv6}]/#ipv6" , headers={'host': testhost})
print(r.content.decode('utf-8'))

from urllib.request import urlopen
url = "https://jsonplaceholder.typicode.com/todos/1"
with urlopen(url) as response:
    body = response.read()
    print(body)



import urllib.request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
request = urllib.request.Request("https://grimaldis.myguestaccount.com/guest/accountlogin", headers=headers)
r = urllib.request.urlopen(request).read()
print(r.decode('utf-8'))

import sys
sys.exit(0)

url = "http://" + testhost
print(url)
with urlopen(url) as response:
    body = response.read()
    print(body)
