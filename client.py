import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client_address = ('localhost', 40789)
gateway_address = ('localhost', 40000)
sock.bind(client_address)

while True:
    message = input("Enter byte message being sent: ")
    if not message:
        print("closing socket", file=sys.stderr)
        sock.close()
    b = message.encode('utf-8')


    # Send data
    print("sending ", b, file=sys.stderr)
    sent = sock.sendto(b, gateway_address)

    # Receive response
    print("waiting to receive")
    data, server = sock.recvfrom(4096)
    print("received ", data, file=sys.stderr)

