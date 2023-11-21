#!/usr/bin/env python3
# Use iperf3 to measure downstream Internet speed
# Reports in Mbps (which is something else than MB/s)
# Only works on Linux, with iperf3 binary & python module installed

import iperf3 # needs iperf3 binary and iperf python module.

print("Let's go ...")
client = iperf3.Client()
client.duration = 3 # seconds
client.num_streams = 20
client.server_hostname = 'ams.speedtest.clouvider.net'
client.port = 5206
client.reverse=True # Downstream
result = client.run() # run the test

print("Downstream speed [Mbps]", int(result.received_Mbps))

