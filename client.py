import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_address = ('localhost', 40789)
gateway_address = ('localhost', 40000)
sock.bind(client_address)
message = "hello"

b = message.encode('utf-8')
# Send data
print ("CLient is sending" , b)
sent = sock.sendto(b, gateway_address)

# Receive response
print("CLient is waiting to receive")
data, server = sock.recvfrom(4096)
print("Client received ", data)

