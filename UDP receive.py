from datetime import datetime
import socket

localIP     = "192.168.1.79"
localPort   = 32645
bufferSize  = 1024
msgFromServer       = "Hello UDP Client"
path = "UDP_messages.txt"

bytesToSend = str.encode(msgFromServer)

 
# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams

for i in range(10): 
	
	date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')	
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]
	
	clientMsg = "Message from Client:{}".format(message)
	clientIP  = "Client IP Address:{}".format(address)
	
	file = open(path,"a")
	file.write('Date : ' + date + '   Température : ' + format(message) + '°C \n')
	file.close()
	
	print(clientMsg)
	print(clientIP)
	i+=1
