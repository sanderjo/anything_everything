#!/usr/bin/env python3
# Use iperf3 to measure downstream Internet speed
# Reports in Mbps (which is something else than MB/s)
# Only works on Linux, with iperf3 binary & python module installed

import iperf3 # needs iperf3 binary and iperf python module.

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
        client = iperf3.Client()
    except:
        return None
    client.duration = duration # seconds
    client.num_streams = 20
    client.server_hostname = server
    client.port = 5206
    client.reverse=True # Downstream
    try:
        result = client.run() # run the test
        # ... after some time:
        Mbps = int(result.received_Mbps)
        return Mbps
    except:
        return None

if __name__ == "__main__":
    print("Let's go ...")
    print("Downstream speed [Mbps]", iperf3_downstream_speed("ams.speedtest.clouvider.net", 1))
    print("Downstream speed [Mbps]", iperf3_downstream_speed("fra.speedtest.clouvider.net", 1))
    print("Downstream speed [Mbps]", iperf3_downstream_speed("nyc.speedtest.clouvider.net", 1))
    print("Downstream speed [Mbps]", iperf3_downstream_speed("la.speedtest.clouvider.net", 1))

    print("Downstream speed [Mbps]", iperf3_downstream_speed())
