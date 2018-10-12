#Use the programme as
#python myclient.py ip_Address_of_Server_in_xx.xx.xx.xx_format

import socket
import sys
import time
import datetime

#argv is a list of command-line parameters
#Elements in this list is of String type
#First parameter (argv[0]) is the name of your programme itself
#In this programme argv[1] will be the IP of ther server
ip_address = sys.argv[1]
port_number = 80

#for first iteration
#Open a file to store the data received from the server
f = open("myDatabase.db","w")
f.write('Current Time, Tempreture, Motor Status' + '\n')
#Go to an infinite loop
while 1:
        try:
                #First Command
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#create a socket
                s.connect((ip_address,port_number))
                
		#Once connection is successful, server is
		#supposed to send some data.
		#Receive that data
                
                message = "temp" + "\n"
                header = 'GET / HTTP/1.1\nHost: ' +ip_address+ '\n'
        #message = "123"
                whole = header + message
                s.send(whole.encode())
                
                #delay
                data = s.recv(1024)
                now = datetime.datetime.now().strftime("%I:%M%p on %B %d %Y")
                f.write(now + ',')
                f.write(data.decode() + ',')
                #print(data.decode())
                temp = float(data.decode())
               
		#Print the received data on the screen
                print("Server:",data.decode())
                
                time.sleep(5)
                s.close()
                
                #Second Command
                if (temp > 50):
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#create a socket
                    s.connect((ip_address,port_number))
                    message = "DCON" + "\n"
                    header = 'GET / HTTP/1.1\nHost: ' +ip_address+ '\n'
                    whole = header + message
                    s.send(whole.encode())
                    #delay
                    #data = s.recv(1024)
                    #Print the received data on the screen
                    #print("Server:",data.decode())
                    f.write('DCON' + '\n')
                    s.close()
                    
                else:
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#create a socket
                    s.connect((ip_address,port_number))
                    message = "DCOF" + "\n"
                    header = 'GET / HTTP/1.1\nHost: ' +ip_address+ '\n'
                    whole = header + message
                    s.send(whole.encode())
                    #delay
                    #data = s.recv(1024)
                    #Print the received data on the screen
                    #print("Server:",data.decode())
                    f.write('DCOF' + '\n')
                    s.close()
                    
        
                time.sleep(5)
                
                    
                #print(type(data.decode()))
                
		#Write the received data to a file. Put a
		#new line at the end so that next data comes
		#in next line
                # f.write(data.decode()+"\n")
		#Ask the user to enter some message through keyboard
                # message = input("Client:")
		#If the user enters "quit", quit the programme,
		#otherwise send the data entered by the user to 
		#the client
                # if message != "quit":
                #     #s.send(message.encode())
                #     s.close()
                # else:
                   # f.close() #Close the file and connection before
                #s.close() #closing the programme
                # break     #Break from the infinite while loop
        except: #If any exception happens during send the data
                f.close() #close the file and connection and close
                s.close() #the programme
                print("Error Connection lost")
                break



