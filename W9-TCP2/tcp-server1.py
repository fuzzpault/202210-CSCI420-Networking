# tcp-server1.py
#
# Paul Talaga
#
# Oct 20, 2022
# Example python TCP server able to only handle
# one conversation at a time.
# Uses exception handling to catch when a user disconnects.

import socket

port = 5555
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind( ('0.0.0.0', port) )
	s.listen(0)
	while True:
		print("Waiting for accept")
		client_socket, addr = s.accept()
		while True:
			print("Got accept, waiting for packet")
			try:
				msg = client_socket.recv(1024)
				msg = msg.decode('ascii')
				print(msg)
				msg += ", huh, that's interesting!"
				client_socket.sendall(msg.encode('ascii'))
			except Exception as e:
				print("Client disconnected")
				break