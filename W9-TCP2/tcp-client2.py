# tcp-client2.py
# Paul Talaga
#
# Oct 25, 2022
#
# Example python TCP client to send and receive data
# to the tcp-server2.py program.
# This uses threads to print a new message from the server
# while waiting for user input.

import socket
import threading

server_ip = '127.0.0.1'
port = 5556

def listen(socket):
	while True:
		rcv = s.recv(1024)
		print(rcv.decode('ascii'))

host = '127.0.0.1'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect( (server_ip, port))
	thread = threading.Thread(target=listen, args=[s])
	thread.start()
	while True:
		message = input("What do you want to send?")
		s.sendall(message.encode('ascii'))
		
	s.close()