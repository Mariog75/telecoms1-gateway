import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 50000)
gateway_address = ('localhost', 40000)
# Bind the socket to the port
print("starting up on port ", gateway_address, file=sys.stderr)

sock.bind(gateway_address)

while True:
    print("\nwaiting to receive message", file=sys.stderr)
    data, address = sock.recvfrom(40789)

    print("received ", (len(data)), " bytes from ", address, file=sys.stderr)
    print(data, file=sys.stderr)

    if data:
        sent = sock.sendto(data, server_address)
        print("sent ", sent, " bytes to ", server_address, file=sys.stderr)
