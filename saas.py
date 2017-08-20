#!/usr/bin/python2

import os,time,sys,commands,fileinput,socket

os.system('dialog --radiolist "check" 20 50 7  1 "Firefox" off 2 "VLC" off 3 "Webcam" off 4 "Tigerviewer" off 5 "VirtualBox" off 6 "Telnet" off 7 "EXIT" on 2>/root/Desktop/cloud/information/saas.txt')

f1=open('/root/Desktop/cloud/information/saas.txt')
ch=f1.read()
f1.close()

if ch=='1':
	os.system('ssh -X root@192.168.43.253 firefox')
	execfile ('/root/Desktop/cloud/menu.py')
elif ch=='2':
	os.system('ssh -X root@192.168.43.253 vlc')
	execfile ('/root/Desktop/cloud/menu.py')
elif ch=='3':
	os.system('ssh -X root@192.168.43.253 cheese')
	execfile ('/root/Desktop/cloud/menu.py')
elif ch=='4':
	os.system('ssh -X root@192.168.43.253 vncviewer')
	execfile ('/root/Desktop/cloud/menu.py')
elif ch=='5':
	os.system('ssh -X root@192.168.43.253 virt-manager')
	execfile ('/root/Desktop/cloud/menu.py')
elif ch=='6':
	os.system('yum install telnet* -y')
	os.system('systemctl restart telnet-server')
	os.system('systemctl enable telnet-server')
	os.system('systemctl status telnet-server')	
	execfile ('/root/Desktop/cloud/menu.py')
elif ch=='7':	
	os.system('exit')
	execfile ('/root/Desktop/cloud/menu.py')
close()
