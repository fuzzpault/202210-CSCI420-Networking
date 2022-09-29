import socket

port_number = 5555
ip_address = '0.0.0.0'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( (ip_address, port_number) )

while True:
	print("Waiting for message...")
	(msg, addr) = s.recvfrom(4096)

	print("Got {} bytes from {}".format(len(msg), addr))
	s.sendto(str(len(msg)).encode('ascii'), addr)


