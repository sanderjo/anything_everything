#!/usr/bin/bash
# Set a fixed, short IPv6 on the default interface
# ... by finding the IPv6 subnet that's in use on the interface

date

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
    addressending="1111"
    echo "No parameter as address ending given, so using $addressending"
else
    # use first parameter
    addressending=$1
fi

# get ipv6 default interface, via ip route
interface=`ip -6 route show | grep default | head -1 | awk '{ print $5 }'`
echo "default interface" $interface

# get subnet, again via ip route 
#subnet=`ip -6 route show | grep $interface | grep dev | grep -vi via | head -1 | awk -F/ '{ print $1 }'`
# ip -6 route show | grep  "^2" # all public IPv6 address start with number 2
subnet=`ip -6 route show | grep $interface | grep "^[0-9]"| head -1 | awk -F/ '{ print $1 }'`
echo "subnet" $subnet


# anothervariable="$variablename"Bash_Is"$myvariable"
#addressending="1111" # so the ipv6 address will be ...::1111
address="$subnet$addressending"
echo "address" $address

ip addr show | grep $address > /dev/null  && echo "$address already there on interface" && exit

echo "Good: $address not in use on this host"
# not on interface of this host, but check if in use elsewhere on the LAN

host=$1

# Ping the host
ping -c 2 $address > /dev/null

# Check the return status of the ping command
if [ $? -eq 0 ]; then
    echo "$address already in use. Exiting"
    exit
else
    echo "Good: $address not yet in use on LAN"
fi

if [ "$EUID" -ne 0 ]
  then echo "Please run as root to set address. Exiting"
  exit
fi

# sudo /sbin/ip -6 addr add 2001:4c3c:4301:9900::1/64 dev enx1cbfce2fc36d
command="/sbin/ip -6 addr add "$address"/64 dev "$interface
echo $command
$command
echo $? # 0 is good


ip addr show | grep $address > /dev/null  && echo "$address added on interface" && exit


# todo ... what if connected to another LAN (read: other ipv6 subnet) ... remove the ipv6 address set earlier?
