#!/usr/bin/python2
import socket, os
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
ip="192.168.56.101"
port=456
s.bind((ip,port))
x=s.recvfrom(1000)
print x 
