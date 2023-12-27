echo "Traffic, down resp up, in MB:"
awk ' /IpExt: [0-9]/ { printf("IPv4: %d %d\n", int($8/1048576), int($9/1048576)) }' /proc/net/netstat
awk ' /Ip6InOctets/ { printf("IPv6: %d ", int ($NF/1048576)) } /Ip6OutOctets/ { printf("%d\n", int ($NF/1048576)) } ' /proc/net/snmp6

