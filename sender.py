#!/usr/bin/python2
import socket,os
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
x=raw_input()
s.sendto(x,("192.168.56.101",456))
