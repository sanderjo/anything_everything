#!/usr/bin/bash

# Set a fixed, short IPv6 on the default interface
# ... by finding the IPv6 subnet that's in use

# get ipv6 default interface, via ip route
interface=`ip -6 route show | grep default | awk '{ print $5 }'`
echo $interface

# get subnet, again via ip route 
#subnet=`ip -6 route show | grep $interface | grep dev | grep -vi via | head -1 | awk -F/ '{ print $1 }'`
# ip -6 route show | grep  "^2" # all public IPv6 address start with number 2
subnet=`ip -6 route show | grep $interface | grep "^[0-9]"| head -1 | awk -F/ '{ print $1 }'`
echo $subnet


# anothervariable="$variablename"Bash_Is"$myvariable"
ending="1111" # so the ipv6 address will be ...::1111
address="$subnet$ending"
echo $address

ip addr show | grep $address > /dev/null  && echo "$address already there on interface" && exit


if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# sudo /sbin/ip -6 addr add 2001:4c3c:4301:9900::1/64 dev enx1cbfce2fc36d
command="/sbin/ip -6 addr add "$address"/64 dev "$interface
echo $command
$command
echo $? # 0 is good


ip addr show | grep $address > /dev/null  && echo "$address added on interface" && exit


