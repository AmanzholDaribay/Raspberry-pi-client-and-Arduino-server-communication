Raspberry pi as a client and Arduino as a server Communication using sockets and ESP8266 Wifi Module
- 

This repository contains solutions to the following tasks:
- 
1. Interface a temperature sensor and a dc motor to Arduino Uno board
2. Running UNO as a server and Raspberry Pi as a client, display the
temperature sensor value on Raspberry terminal every 5 seconds. Display the
temperature value on the UNO serial monitor also.
3. Modify the program in such as way that, when the temperature is above
15C, the DC motor is turned on based on the command from the client
(Raspberry)
4. Log the time, temperature and motor status (ON/OFF) in a database at the
client

The files:
- 
- **Arduino_Server.ino** Arduino as a Server, considering above tasks (completed-all version)
- **rasClient1.py** RaspberryPi as a Client; answer for the task3
- **rasClient2.py** RaspberryPi as a Client; answer for the task4
- **Simple_server.py** code for basic server, applicable both for PC and Raspberry Pi
- **ESP8266_AT_command.pdf** contains mostly used AT commands for ESP8266
 
 Before Running:
 - 
 - Properly make connection of Arduino and ESP8266 Wifi Module:
 Use Arduino as usb-uart converter first, meaning directly connect ESP8266's Rx & Tx to the Arduino's Rx & Tx
 - Then check the connection by changing the baud rate and NL&CR in the Serial terminal.
 Then change the baud rate to 9600
 - After connect ESP8266 to the artificial Rx & Tx (pins 10 and 11 on Arduino)
 - Then make proper connections as it has been asked in task1 above.
 - Establish Raspberry Pi side
 
 To Run:
 -
 - First run Arduino_Server.ino in PC using Arduino software and observe Serial console,
 where you get IP address(ip_address) of your Arduino server
 - Second run Raspberry Pi side in console as: python task3(RaspberryPi_client).py ip_address
 - Try to play 
 
  
 
Acknowledgments
-
I thank Professor Vipin Kizheppatt at School of Engineering at Nazarbayev University in Astana, Kazakhstan for having a class of Internet of Things, during which this project has been done!