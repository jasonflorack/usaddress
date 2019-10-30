# FROM:
# https://pymotw.com/2/socket/tcp.html

# TO RUN SERVER:
# python ./socket_echo_server.py
# THEN RUN CLIENT IN A DIFFERENT WINDOW:
# python ./socket_echo_client.py

import json
import random
import socket
import sys


class SocketEchoClient:
    def __init__(self):
        """A Socket Client that sends an address to a server which parses the sent string and returns it, parsed, in JSON"""

        # Create a list of addresses to be sent at random to the server
        addresses = [
            '123 Main St. Suite 100 Chicago, IL',
            '137 Ripplewood Drive, Greece NY, 14616',
            '4039 S Peoria St. Chicago IL 60609 Cook',
            '135th St. & New Ave., Lemont, IL, 60439',
            '7303 Burleson Road Omni Suite 201 Austin TX 78744',
            ' 6205 Best Friend Road Suite D, Norcross, GA 30071',
            '10300 W Charleston, #13-351, Las Vegas NV 89135,',
            '11 Golden Shore Dr., Ste. 340 Long Beach ,CA 90802'
        ]

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 10000)
        print >>sys.stdout, 'CLIENT: connecting to %s port %s' % server_address
        sock.connect(server_address)

        try:
            # Send data
            # message = raw_input()
            msg_no = random.randrange(len(addresses))
            message = addresses[msg_no]
            print >>sys.stdout, 'CLIENT: sending "%s"' % message
            sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(2056)
                if not data:
                    print >>sys.stderr, 'CLIENT: received no data from server...'
                    break
                amount_received += len(data)
                print >>sys.stdout, 'CLIENT: received "%s"' % data

        finally:
            print >>sys.stdout, 'CLIENT: closing socket'
            sock.close()
