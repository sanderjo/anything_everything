# Linux
IPV4=`awk '/IpExt/ { print $8 }' /proc/net/netstat | tail -1`
IPV6=`awk '/Ip6InOctets/{ print $NF }' /proc/net/snmp6`
SUM=$((IPV4 + IPV6))
echo $((100*IPV6 / SUM)) "% IPv6 traffic"



