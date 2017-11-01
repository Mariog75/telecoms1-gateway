import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 50000)
gateway_address = ('localhost', 40000)
buffer = 1024
print("Server starting up on port ", server_address)

sock.bind(server_address)

while True:
    print("\nServer waiting to receive message")
    data, address = sock.recvfrom(buffer)

    print("Server received ", (len(data)), " bytes from ", address)
    print(data)

    if data:
        ack_bit = 1
        sock.sendto(ack_bit, gateway_address)
        print("Server sent ", sent, " bytes back to ", gateway_address)
