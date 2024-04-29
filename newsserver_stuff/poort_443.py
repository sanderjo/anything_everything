#!/usr/bin/env python3

'''
import socket
import ssl

# Server details
server_host = 'news.newshosting.com'
server_port = 563

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL/TLS
ssl_socket = ssl.wrap_socket(client_socket, ssl_version=ssl.PROTOCOL_TLS)

# Connect to the server
ssl_socket.connect((server_host, server_port))

try:
    # Send data to the server
    ssl_socket.sendall(b'QUIT\r\n')

    # Receive data from the server
    data = ssl_socket.recv(1024)
    print(f'Received from server: {data.decode()}')

finally:
    # Close the connection
    ssl_socket.close()

'''

import socket
import ssl
import time
import sys

def connect_to_ssl_socket(host, port, timeout):
    # Create a socket
    client_socket = socket.create_connection((host, port))

    # Create an SSL context
    ssl_context = ssl.create_default_context()

    # Wrap the socket with SSL
    ssl_socket = ssl_context.wrap_socket(client_socket, server_hostname=host)

    return ssl_socket

def main():
    try:
        host = sys.argv[1]
    except:
        host = "news.newshosting.com"

    try:
        port = sys.argv[2]
    except:
        port = 563
    timeout = 5
    print(host, port, end=" ")

    try:
        # Connect to the SSL socket
        ssl_socket = connect_to_ssl_socket(host, port, timeout)

        # Your code to interact with the SSL socket goes here
        # For example, you can send and receive data using ssl_socket.send() and ssl_socket.recv()

        # ...
        data = ssl_socket.recv(1024)
        print("Received:", data.decode('utf-8'), end="")

    except socket.error as e:
        print(f"Error: {e}")
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    finally:
        # Close the SSL socket
        if 'ssl_socket' in locals():
            ssl_socket.close()

if __name__ == "__main__":
    main()


'''
import socket
import ssl

# Set the server and port
server_address = ('news.newshosting.com', 563)

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create an SSL context
ssl_context = ssl.create_default_context()

# Wrap the socket with SSL
ssl_socket = ssl_context.wrap_socket(sock, server_hostname='news.newshosting.com', timeout=5)

try:
    # Connect to the server
    ssl_socket.connect(server_address)
    print("Connected to", server_address)

    # Now you can send and receive data through ssl_socket
    # For example:

    data = ssl_socket.recv(1024)
    print("Received:", data.decode('utf-8'))

finally:
    # Close the socket
    ssl_socket.close()


'''
