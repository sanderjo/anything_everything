import platform
import os

def windows_get_ipv4_octets():
	cmd = "netsh interface ipv4 show ipstats"
	for thisline in os.popen(cmd).readlines():
		if thisline.find("In Receives")>=0:
			value = int(thisline.strip().split()[-1])
			return value

def windows_get_ipv6_octets():
	cmd = "netsh interface ipv6 show ipstats"
	for thisline in os.popen(cmd).readlines():
		if thisline.find("In Receives")>=0:
			value = int(thisline.strip().split()[-1])
			return value

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
					return(int(value))

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
					return(int(value))



if platform.system() == "Windows":
	print("Windows!!!")
	ipv4 = windows_get_ipv4_octets()
	ipv6 = windows_get_ipv6_octets()
	print(ipv4, ipv6, "\nIPv6 percentage of total traffic:", int(100*ipv6/(ipv4+ipv6)),"%")
elif platform.system() == "Linux":
	print("Linux")
	ipv4=linux_get_ipv4_octets()
	ipv6=linux_get_ipv6_octets()
	print(ipv4, ipv6, "\nIPv6 percentage of total traffic:", int(100*ipv6/(ipv4+ipv6)),"%")





