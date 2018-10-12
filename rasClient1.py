import socket
import sys
import time 
import datetime

ip_address = sys.argv[1]
port = 80

f = open('myDatabase.db', 'w')
f.write('Time, Tempreture, Condition' + '\n')


#we do need try and error for continuing the code in the
#exception part, otherwise if there has been an error occured
#lots of things can be lost
while 1:
	try: 
		#Creation of a connection and message sending...
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((ip_address,port))

		message = 'temp' + '\n'
		header = 'GET...' + '\n'
		whole = header + message

		s.send(whole.encode())

		#Recieving...
		data = s.recv(1024)
		temp = float(data.decode())

		time.sleep(5)
		s.close()

		#New Command...
		if (temp > 15):
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((ip_address,port))
			message = 'DCON' + '\n'
			header = 'GET...' + '\n'
			whole = header + message

			s.send(whole.encode())
			s.close()

		else:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((ip_address,port))
			message = 'DCOF' + '\n'
			header = 'GET...' + '\n'
			whole = header + message

			s.send(whole.encode())
			s.close()

		time.sleep(5)

	except:
		s.close()
		f.close()
		print("Connection Failed")
		break



