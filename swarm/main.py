import socket 

localIP = 192.168.1.14
localPort = 20001

slave_a_ip = 192.168.1.115
slave_b_ip = 192.168.1.64
slave_c_ip = 192.168.1.161

bufferSize = 1024

msgFromServer = "hello Esp Slaves"

bytesToSend = str.encode(msgFromServer)


# first creat datagram socket

udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# bind to address and ip

udp_server_socket.bind(localIP, localPort)

print(" Udp Server Up and Listening ")

# Listening for incoming Datagram

slace_a_data = []

slave_b_data = []

slave_c_data = []

def send(msg, addr):
	udp_server_socket.sendto(msg, addr)

def listen():
	byte_addr_pair = udp_server_socket.recvfrom(bufferSize)
	msg = byte_addr_pair[0]
	address = byte_addr_pair[1]
	return(msg)

while True :

	todo=listen()

