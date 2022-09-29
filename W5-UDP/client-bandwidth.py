import socket
import time

port_number = 5555
#ip_address = '127.0.0.1'
ip_address = '10.17.99.120'

size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

input("Hit enter to send {} bytes".format(size))

message = b'h' * size

while True:
	start = time.time()
	s.sendto(message, (ip_address, port_number))

	(msg, addr) = s.recvfrom(1024)
	end = time.time()
	print("Elapsed time: {} seconds".format(end-start))
	print("{} bytes per second".format(size / (end-start)))