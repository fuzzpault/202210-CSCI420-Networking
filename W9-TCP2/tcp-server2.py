# tcp-server2.py
#
# Paul Talaga
#
# Oct 25, 2022
# Example python TCP server able to handle multiple 
# simultaneous connections with threads.

import socket
import threading

socket_list = []

def TCPworker(sockets):
	(client_socket, addr) = sockets[-1]
	while True:
			print("Got accept, waiting for packet")
			try:
				msg = client_socket.recv(1024)
				msg = msg.decode('ascii')
				print(msg)
				#msg += ", huh, that's interesting! num clients:"
				#msg += str(len(sockets))
				#client_socket.sendall(msg.encode('ascii'))
				for (other_s, _) in sockets:
					other_s.sendall(msg.encode('ascii'))
			except Exception as e:
				print("Client disconnected")
				break
	sockets.remove( (client_socket, addr) )


port = 5556
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind( ('0.0.0.0', port) )    # address already in use?
	s.listen(0)
	while True:
		print("Waiting for accept")
		client_socket, addr = s.accept()
		print("Got accept from " + str(addr))
		socket_list.append( (client_socket, addr) )
		thread = threading.Thread(target=TCPworker, args=[socket_list])
		thread.start()
		