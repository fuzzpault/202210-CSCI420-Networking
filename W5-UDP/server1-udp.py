import socket

port_number = 5555
ip_address = '0.0.0.0'

clients = {}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind( (ip_address, port_number) )

while True:
	print("Waiting for message...")
	(msg, addr) = s.recvfrom(1024)
	msg = msg.decode('ascii')
	clients[addr[0]] = msg
	print("Got '{}' from {}".format(msg, addr))
	#msg = msg + " Ha!"
	#msg = msg.upper()
	msg = ""
	
	for k in clients.keys():
		print("{}: {}".format(k, clients[k]))
		msg += "{}: {}".format(k, clients[k]) + "\n"
	s.sendto(msg.encode('ascii'), addr)





print(msg)