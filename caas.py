import commands
import socket,os,time
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
port=5555
s.bind(("",port))
os.system('dialog --infobox "Hello guys WELCOME your *Container as a Service* " 10 30')

time.sleep(1)
os.system('dialog --radiolist "Select your OS Name:" 30 40 2  ubuntu "OS" on centos  "OS" off  2>/root/Desktop/cloud/information/caas_os.txt')
os.system('dialog --inputbox "Enter numbers of OS: " 10 30  2>/root/Desktop/cloud/information/caas_os_no.txt')
os.system('dialog --infobox "*Container as a Service*" 10 30')
time.sleep(2)


sip="192.168.43.253"
sport=1237
f1=open('/root/Desktop/cloud/information/caas_os.txt')
name=f1.read()
print type(name)
s.sendto(name,(sip,sport))

f2=open('/root/Desktop/cloud/information/caas_os_no.txt')
no=f2.read()
print type(no)
s.sendto(no,(sip,sport))
no=int(no)
#print type(no)
#time.sleep(4)
print "select os to run :\n "
count = 0	
while count < no:
		print name,count
		count+=1

count=0

while count < no:
	c=str(count)	
	arg="/root/Desktop/os"+c+".sh"
	ip=count+2
	ip=str(ip)
	arg2="ssh 172.17.0."+ip	
	print arg
	print arg2
	c=open(arg,"w")
	c.write(arg2)
	c.close()
	count+=1
execfile ('/root/Desktop/cloud/menu.py')
