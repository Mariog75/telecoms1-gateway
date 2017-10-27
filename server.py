import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 50000)
client_address = ('localhost', 40789)
print("starting up on port ", server_address, file=sys.stderr)

sock.bind(server_address)

while True:
    print("\nwaiting to receive message", file=sys.stderr)
    data, address = sock.recvfrom(40789)

    print("received ", (len(data)), " bytes from ", address, file=sys.stderr)
    print(data, file=sys.stderr)

    if data:
        ack_bit = b'1'
        sent = sock.sendto(ack_bit, client_address)
        print("sent ", sent, " bytes back to ", client_address, file=sys.stderr)t
