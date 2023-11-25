#!/usr/bin/env python3
# Use iperf3 to measure downstream Internet speed
# Reports in Mbps (which is something else than MB/s)
# Only works on Linux, with iperf3 binary & python module installed

import random

'''
"nyc.speedtest.clouvider.net"
"la.speedtest.clouvider.net"
"ams.speedtest.clouvider.net",
"la.speedtest.clouvider.net",
"fra.speedtest.clouvider.net",
"ash.speedtest.clouvider.net",
"nyc.speedtest.clouvider.net",
"speedtest.uztelecom.uz",
"proof.ovh.net",
# "iperf.worldstream.nl",

'''

def iperf3_downstream_speed(server='ams.speedtest.clouvider.net', duration=3):
    try:
        import iperf3 # needs iperf3 binary and iperf python module.
    except:
        return None
    client = iperf3.Client()
    client.duration = duration # seconds
    client.num_streams = 20 # should be enough for ... 2500 Mbps?
    client.server_hostname = server
    client.reverse=True # Downstream

    portlist = list(range(5200, 5209 + 1))
    for _ in range(4):
        myport = random.choice(portlist)
        portlist.remove(myport)
        client.port = myport
        print(server, myport)
        try:
            result = client.run() # run the test
            # ... after some time:
            Mbps = int(result.received_Mbps)
            return Mbps
        except:
            pass
    return None

if __name__ == "__main__":
    print("Let's go ...")
    print("Downstream speed [Mbps]", iperf3_downstream_speed("ams.speedtest.clouvider.net", 3))
    print("Downstream speed [Mbps]", iperf3_downstream_speed("fra.speedtest.clouvider.net", 3))
    print("Downstream speed [Mbps]", iperf3_downstream_speed("nyc.speedtest.clouvider.net", 3))
    print("Downstream speed [Mbps]", iperf3_downstream_speed("la.speedtest.clouvider.net", 3))

    print("Downstream speed [Mbps]", iperf3_downstream_speed())
