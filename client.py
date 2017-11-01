import socket
import sys
from random import randint

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
randomGenerator = randint(5000, 50000)
buffer = 1024

client_address = ('localhost', randomGenerator)
gateway_address = ('localhost', 40000)
sock.bind(client_address)
message = 0

while True:
	# Send data
	print ("Client is sending" , message)
	sock.sendto(str(message), gateway_address)

	# Receive response
	print("Client is waiting to receive")
	data, server = sock.recvfrom(buffer)
	print("Client received ", data)

