#!/usr/bin/python2
import os,time
os.system("dialog --infobox ' BIG DATA' 10 30")
time.sleep(2)
os.system("dialog --msgbox 'Press okay to continue' 10 30")
os.system('dialog --inputbox "Enter user name" 10 30 2> /tmp/user.txt')
os.system('dialog --insecure --passwordbox "type password" 10 30 2>/tmp/passwd.txt')
f1=open('/tmp/user.txt')
user=f1.read()
f1.close()
f2=open('/tmp/passwd.txt')
passwd=f2.read()
f2.close()
if user=="neha" and passwd=="redhat":
	execfile('menu.py')
else :
	execfile('login.py')
