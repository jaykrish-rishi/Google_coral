from periphery import LED
import socket
import time

localIP = "192.168.1.14"
localPort = 20001
bufferSize = 1024

msg_from_server = "Hello Esp Client - you can control LED"
bytesToSend = str.encode(msg_from_server)

byteAddressPair = []

#create a datagram socket 

udp_server_socket = socket.socket(family = socket.AF_INET, type=socket.SOCK_DGRAM)

#bind to address and ip 

udp_server_socket.bind((localIP,localPort))

print("UDP server up and LIstening")

# listening for incoming datagrams

def led_onoff(value):
	#led0 = LED("led0", False)
	led1 = LED("led", True)

	if value == True :
		led1.write(True)
		led0.write(True)
	elif value == False :
		led1.write(False)
		ledd0.write(False)

while(True):
	byteAddressPair = udp_server_socket.recvfrom(bufferSize)
	message = byteAddressPair[0]
	address = byteAddressPair[1]
	clientMsg = "Message From Client :{}".format(message)
	clientIP = "Client IP Address : {}".format(address)
	print(clientMsg)
	print(clientIP)

	#sending a reply to client 
	udp_server_socket.sendto(bytesToSend ,address)

	if message == b'N' :
		led_onoff(True)
		time.sleep(0.5)
		msg = " Server Leds ON"
		print(msg)
		udp_server_socket.sendto(str.encode(msg), address)
		time.sleep(2)

	if message == b'F' :
		led_onoff(False)
		time.sleep(0.5)
		msg = " Server Leds Off"
		print(msg)
		udp_server_socket.sendto(str.encode(msg), address)

