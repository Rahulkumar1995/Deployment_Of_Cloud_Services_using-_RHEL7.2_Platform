import commands
import socket,os,time
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
port=3333
s.bind(("",port))
os.system('dialog --inputbox "Enter Disk Name: " 10 30 2>/root/Desktop/cloud/information/staas2_disk.txt')
os.system('dialog --inputbox "Specify size(MB): " 10 30 2>/root/Desktop/cloud/information/staas2_size.txt')

sip="192.168.43.253"
sport=1235

f1=open('/root/Desktop/cloud/information/staas2_disk.txt')
disk=f1.read()
s.sendto(disk,(sip,sport))
f2=open('/root/Desktop/cloud/information/staas2_size.txt')
size=f2.read()
s.sendto(size,(sip,sport))


print "ok"
drecv=s.recv(1024)
print drecv
if drecv=="ok":

	a = commands.getstatusoutput("sudo iscsiadm --mode discoverydb --type sendtargets    --portal 192.168.43.253 --discover")
	print a
	time.sleep(1)
	print "sudo iscsiadm --mode node --targetname "+disk+" --portal 192.168.43.253:3260 --login"
	b =commands.getstatusoutput("sudo iscsiadm --mode node --targetname "+disk+" --portal 192.168.43.253:3260 --login")
	print b
	time.sleep(2)	
	execfile ('/root/Desktop/cloud/menu.py')

