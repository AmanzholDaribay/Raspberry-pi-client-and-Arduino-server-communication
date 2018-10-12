import socket
import random

ip_address = ""
port_number = 80

#The socket object is created...
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	#it has been attempted to bind the socket with
	#IP and port number
	s.bind((ip_address, port_number))
except:
	print("Error!")

#The socket is listening for request...
s.listen(2) #2 is how many clients can connect


#The request is accepted...
#This loop is for accepting requests
while 1:
	c, addr = s.accept()
	#c is socket type object
	#addr is an address of the sender


	#This loop is for staying in connection with accepted client
	while 1:
		message = "Some message"
		try:
			c.sendall(message.encode())
			message = c.recv(1024)
		except:
			c.close()
			break
