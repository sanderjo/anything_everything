#!/usr/bin/env python3

import sys
import socket
import ssl


TEST_HOSTNAME = sys.argv[1]
TEST_PORT = 563 # NNTPS
TEST_IP = sys.argv[2]
SOCKET_TIMEOUT = 4


def check_certificate(hostname, port=443):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)

    try:
        conn.connect((hostname, port))
        cert = conn.getpeercert()

        # Check the certificate
        if cert:
            print("Certificate Details:")
            for key, value in cert.items():
                print(f"{key}: {value}")
        else:
            print("No certificate found.")

    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except socket.error as e:
        print(f"Socket Error: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    ip_address = "your_ip_address_here"  # Replace with the IP address you want to connect to
    check_certificate(ip_address)

sys.exit(0)

'''
import sys
import socket
import ssl


TEST_HOSTNAME = sys.argv[1]
TEST_PORT = 563 # NNTPS
TEST_IP = sys.argv[2]
SOCKET_TIMEOUT = 4

#addrinfo = happyeyeballs(TEST_HOSTNAME, TEST_PORT, SOCKET_TIMEOUT)


sock = socket.socket(socket.AF_INET)
sock.settimeout(SOCKET_TIMEOUT)
sock.connect((TEST_IP, TEST_PORT))
secure_sock = context.wrap_socket(sock, server_hostname=TEST_HOSTNAME)
'''