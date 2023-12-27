#!/usr/bin/env python3

'''
Prints the amounts of IPv4 and IPv6 traffic, plus percentage IPv6 of total traffic

'''

import platform
import os

def windows_get_ipv4_octets():
	cmd = "netsh interface ipv4 show ipstats"
	for thisline in os.popen(cmd).readlines():
		if thisline.find("In Receives")>=0:
			return int(thisline.strip().split()[-1])


def windows_get_ipv6_octets():
	cmd = "netsh interface ipv6 show ipstats"
	for thisline in os.popen(cmd).readlines():
		if thisline.find("In Receives")>=0:
			return int(thisline.strip().split()[-1])


def linux_get_ipv4_octets():
	'''
	$ cat /proc/net/netstat  | grep IpExt | awk '{ print $8 }'
	InOctets
	24471754
	'''
	with open("/proc/net/netstat") as filein:
		for line in filein.readlines():
			if line.find("IpExt")>=0:
				value = line.split()[7]
				if value.isnumeric():
					return int(value)
	# we should not get here:
	return 0

def linux_get_ipv6_octets():
	'''
	$ cat /proc/net/snmp6 | grep Ip6InOctets
	Ip6InOctets                     	241448401
	'''
	with open("/proc/net/snmp6") as filein:
		for line in filein.readlines():
			if line.find("Ip6InOctets")>=0:
				value = line.strip().split()[-1]
				if value.isnumeric():
					return int(value)
	# we should not get here:
	return 0



if platform.system() == "Windows":
	print("Windows!!!")
	ipv4 = windows_get_ipv4_octets()
	ipv6 = windows_get_ipv6_octets()
	percentage_ipv6 = int(100*ipv6/(ipv4+ipv6))
	print(ipv4, ipv6, "\nIPv6 percentage of total traffic:", percentage_ipv6 ,"%")
elif platform.system() == "Linux":
	print("Linux")
	ipv4 = linux_get_ipv4_octets()
	ipv6 = linux_get_ipv6_octets()
	percentage_ipv6 = 100*ipv6/(ipv4+ipv6)
	print(f"IPv4 giga-octets {ipv4/1024/1024/1024:.2f}, IPv6 giga-octets {ipv6/1024/1024/1024:.2f}")
	print(f"IPv6 percentage of total traffic: {percentage_ipv6:.2f} %")
else:
	print("sorry, other, non-supported platform", platform.system())





