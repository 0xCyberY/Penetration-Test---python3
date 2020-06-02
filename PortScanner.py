#mporting the socket library and making a simple socket.
import socket    
 
host = input('Enter the IP address to scan the open ports:\n')

try:#This block is for exception handling in python
    
    for port in range(1,1000):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #The socket.AF_INET refers to the address family ipv4. 
        #The SOCK_STREAM means connection oriented TCP protocol.
        socket.setdefaulttimeout(1)
        #To change the port NO. in 1 sec.
        result = s.connect_ex((host,port))
        #TO opens up a TCP connection to the hostname on the port number .
        #and assign it to result.
        if result == 0:
            print("The port {} is open.".format(port))
except:
    print("ERROR!!")
