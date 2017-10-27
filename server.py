import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 50000)
client_address = ('localhost', 40789)
print("Server starting up on port ", server_address)

sock.bind(server_address)

while True:
    print("\nServer waiting to receive message")
    data, address = sock.recvfrom(40789)

    print("Server received ", (len(data)), " bytes from ", address)
    print(data)

    if data:
        ack_bit = b'1'
        sent = sock.sendto(ack_bit, client_address)
        print("Server sent ", sent, " bytes back to ", client_address)
