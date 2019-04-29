import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    # Send data
    ct = 0
    while True:
        message = 'This is the message.  It will be repeated.' + '[' + bytes(ct) + ']'
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)
        ct += 1

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
    
        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data
        
        time.sleep(1)

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()


