# tcp-client1.py
# Paul Talaga
#
# Oct 20, 2022
#
# Example python TCP client to send and receive data
# to the tcp-server.py program.
# Uses the with feature to close the connection in the event
# of a crash or exit.

import socket

server_ip = '127.0.0.1'
port = 5555

host = '127.0.0.1'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect( (server_ip, port))
	while True:
		message = input("What do you want to send?")
		s.sendall(message.encode('ascii'))
		rcv = s.recv(1024)
		print(rcv.decode('ascii'))
	s.close()