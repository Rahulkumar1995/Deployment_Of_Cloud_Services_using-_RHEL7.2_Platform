#!/usr/bin/python2

import os,time,sys,commands,fileinput,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)

port=8989
s.bind(("",port))
os.system('dialog --infobox " W3LC0M3 US3R" 10 30')
time.sleep(1)

os.system('dialog --inputbox "Enter UserName" 10 30 2>/root/Desktop/cloud/information/user.txt')
os.system('dialog --insecure --passwordbox "Enter Password" 10 30 2>/root/Desktop/cloud/information/pass.txt')

sip="192.168.43.253"
sport=1234
f1=open('/root/Desktop/cloud/information/user.txt')
user=f1.read()
#print type(user)
s.sendto(user,(sip,sport))
f2=open('/root/Desktop/cloud/information/pass.txt')
password=f2.read()
#print type(password)
s.sendto(password,(sip,sport))
f1.close()
f2.close()
print "OK"
execfile('/root/Desktop/cloud/menu.py')