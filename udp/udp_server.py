import socket

localIP = "192.168.1.14"
localPort = 20001
bufferSize = 1024

msg_from_server = "Hello UDP Client "
bytesToSend = str.encode(msg_from_server)

byteAddressPair = []

#create a datagram socket 

udp_server_socket = socket.socket(family = socket.AF_INET, type=socket.SOCK_DGRAM)

#bind to address and ip 

udp_server_socket.bind((localIP,localPort))

print("UDP server up and LIstening")

# listening for incoming datagrams

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

