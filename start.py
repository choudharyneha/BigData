#!/usr/bin/python
import os,commands
c=commands.getstatusoutput("nmap -sP 192.168.56.0-255 -n|grep 'Nmap scan'|awk '{print $5}'")
y=open('b.txt',mode='wr')
y.write(c[1])
y.close()
fh=open('b.txt',mode='r')
lines=fh.read()
words=lines.split()
for x in words:
	if x=='192.168.56.1' or x=='192.168.56.100':
		pass
	elif x=='192.168.56.101':
		os.system('hostnamectl set-hostname nn')
	else:	
		os.system('sshpass -p redhat ssh -l root {} hostnamectl set-hostname dn'.format(x))
