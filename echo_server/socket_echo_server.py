# FROM:
# https://pymotw.com/2/socket/tcp.html

# TO RUN SERVER:
# python ./socket_echo_server.py
# THEN RUN CLIENT IN A DIFFERENT WINDOW:
# python ./socket_echo_client.py

#!/Users/jasonflorack/.virtualenvs/usaddress/bin/python

import socket
import sys

import json
import usaddress

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stdout, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stdout, 'SERVER: waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stdout, 'SERVER: connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            # 'recv' information:
            # https://stackoverflow.com/questions/40448937/socket-recv-buffer-size
            # and
            # https://stackoverflow.com/questions/1708835/python-socket-receive-incoming-packets-always-have-a-different-size
            data = connection.recv(2056)
            print >>sys.stdout, 'SERVER: received "%s"' % data
            if data:
                print >>sys.stdout, 'SERVER: sending data back to the client'
                parsed_address = json.dumps(usaddress.tag(data))
                connection.sendall(parsed_address)
            else:
                print >>sys.stdout, 'SERVER: no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()
