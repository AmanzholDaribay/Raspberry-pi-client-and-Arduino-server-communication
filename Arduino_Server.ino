//Arduino + ESP8266 Wifi module as a SERVER

//Since the program is coming from USB, and then converted to UART,
//then directed to Tx-RX and ATmega328p (microcontroller at Arduino);
//Thus, two UART connections can interfere with each other,
//as a result, it is better to have additional artificial UART connection
//between Arduino and ESP8266, while there is a simple UART between
//PC and Arduino.

#include <SoftwareSerial.h>
const int motor = 3;
//SoftwareSerial is used for 'artifical' UART (serial) connection
SoftwareSerial mySerial(10,11); //10-RX, 11-TX
const char* ssid = "ssid";
const char* password = "password";
String response = "";

//STEP1: Setup of Configurations
void setup(){
	//Serial configurations...
	Serial.begin(9600);
	mySerial.begin(9600);

	//Connecting to ESP8266...
	mySerial.println("AT");
	delay(1000);
	while(mySerial.available()){
		char c = mySerial.read(); //read char by char
		response += c;
	}

	if (response.substring(7,9) == "OK"){
		Serial.println("Success!");
	}
	else {
		Serial.println("Failed!");
	}


	//Setting operation mode...
	//1 is setting as a server
	mySerial.println("AT+CWMODE_CUR=1");
	delay(1000);
		while(mySerial.available()){ //to wait for the response from ESP8266
		mySerial.read();
		}

	//Here you can include command to list availbale internet points

	//Connecting to internet...
	mySerial.println("AT+CWJAP_CUR=\"ssid\",\"password\"");
	delay(5000);
		while(mySerial.available()){ //to wait for the response from ESP8266
			mySerial.read();
		}
	Serial.println("Connected to WiFi");

	//Setting module to multiple connections...
	mySerial.println("AT+CIPMUX=1");
	delay(2000);
		while(mySerial.available()){
			mySerial.read();
		}

	//Creating TCP server...
	mySerial.println("AT+CIPSERVER = 1,80"); //1 is for enabling and 80 is port
	delay(2000);
		while(mySerial.available()){
			mySerial.read();
		}
	Serial.println("Server started!");

	//Getting IP address of the server...
	//After creating a server, it has been assigned IP address
	mySerial.println("AT+CIFSR");
	delay(2000);
		while(mySerial.available()){
			mySerial.read();
		}
}
