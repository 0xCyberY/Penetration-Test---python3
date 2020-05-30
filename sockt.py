#Socket programming is a way of connecting two nodes 
# on a network to communicate with each other.

 #mporting the socket library and making a simple socket.
import socket    
 
host = input('Enter the host IP OR loop IP or localhost IP ex:127.0.0.1\n')

port = int(input('Enter the port Number ex: 9999\n'))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#The socket.AF_INET refers to the address family ipv4. 
#The SOCK_STREAM means connection oriented TCP protocol.

#TO opens up a TCP connection to the hostname on the port number .
s.connect((host,port))
