import commands
import socket,os,time
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
port=2222
s.bind(("",port))

os.system('dialog --inputbox "Enter Disk Name: " 10 30 2>/root/Desktop/cloud/information/staas1_disk.txt')
os.system('dialog --inputbox "Specify size(MB): " 10 30 2>/root/Desktop/cloud/information/staas1_size.txt')

sip="192.168.43.253"
sport=12345


f1=open('/root/Desktop/cloud/information/staas1_disk.txt')
disk=f1.read()
s.sendto(disk,(sip,sport))
f2=open('/root/Desktop/cloud/information/staas1_size.txt')
size=f2.read()
s.sendto(size,(sip,sport))


print "ok"
drecv=s.recv(1024)
print drecv
if drecv=="ok":
	a = commands.getstatusoutput("sudo mkdir /media/"+disk)
	print a
	time.sleep(1)
	print 'sudo mount 192.168.43.253:/media/'+disk+'   /media/'+disk+''
	b = commands.getstatusoutput("sudo mount 192.168.43.253:/media/"+disk+"   /media/"+disk+" ")
	print b
	time.sleep(2)