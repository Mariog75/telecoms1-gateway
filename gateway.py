import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 50000)
gateway_address = ('localhost', 40000)
buffer = 1024
# Bind the socket to the port
print("Gateway starting up on port ", gateway_address)

sock.bind(gateway_address)

while True:
    print("\nGateway waiting to receive message")
    data, address = sock.recvfrom(buffer)

    print("Gateway received ", (len(data)), " bytes from ", address)
    print(data)

    if data:
        sent = sock.sendto(data, server_address)
        print("Gateway sent ", sent, " bytes to ", server_address)
