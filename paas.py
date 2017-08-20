import commands
import socket,os,time
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
port=6666
s.bind(("",port))

os.system('dialog --infobox "--Welcome to PAAS-- " 10 30')
time.sleep(2)
os.system('dialog --inputbox "Choose Your Desired Plateform:\n 1.Python\n2.Perl \n3.Ruby\n 10 30 2>/root/Desktop/cloud/information/pchoice.txt')
f1=open('/root/Desktop/cloud/information/pchoice.txt')
ch=f1.read()
f1.close()
if ch=='1':
	os.system("ssh paas1@192.168.43.253")
elif ch=='2':
	os.system("ssh paas2@192.168.43.253")
elif ch=='3':
	os.system("ssh paas3@192.168.43.253")
execfile ('/root/Desktop/cloud/menu.py')
