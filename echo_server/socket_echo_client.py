# FROM:
# https://pymotw.com/2/socket/tcp.html

# TO RUN SERVER:
# python ./socket_echo_server.py
# THEN RUN CLIENT IN A DIFFERENT WINDOW:
# python ./socket_echo_client.py

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    # message = raw_input()
    # message = "This is the message.  It will be repeated."
    message = "123 Main St. Suite 100 Chicago, IL"
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(2056)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
