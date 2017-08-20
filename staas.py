import commands
import socket,os
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
os.system('dialog --menu "Select your Services" 10 30 3  1 "Object Storage"  2 "Block Storage"  3 "EXIT"  2>/root/Desktop/cloud/information/staas.txt')

sip="192.168.43.253"
sport=1234

f1=open('/root/Desktop/cloud/information/staas.txt')
ch=f1.read()
f1.close()

if ch=='1':
	execfile('/root/Desktop/cloud/choice/staas1.py')
	

	
elif ch=='2':
	execfile('/root/Desktop/cloud/choice/staas2.py')
	
elif ch=='3':
	execfile('/root/Desktop/cloud/menu.py')
	
