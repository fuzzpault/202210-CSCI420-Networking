import socket
import threading

port_number = 5555
ip_address = '127.0.0.1'
#ip_address = '10.17.102.208'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_ready = False

def listenThread():
	global s
	global sock_ready
	while not sock_ready:
		pass
	while True:
		(msg, addr) = s.recvfrom(1024)
		msg = msg.decode('ascii')
		print(msg)

listener = threading.Thread(target=listenThread)
listener.start()

while True:
	message = input("Give me some text")
	s.sendto(message.encode('ascii'), (ip_address, port_number))
	sock_ready = True

	