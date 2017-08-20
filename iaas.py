import commands
import socket,os,time
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
port=4444
s.bind(("",port))
os.system('dialog --inputbox "Enter Your Name: " 10 30 2>/root/Desktop/cloud/information/iaas_name.txt')
os.system('dialog --radiolist "Select your OS Name:" 30 40 2  Ubuntu "OS" on Cirros  "OS" off 2>/root/Desktop/cloud/information/iaas_os.txt')
os.system('dialog --radiolist "Specify OS size(GiB): " 30 40 3 5 "GiB" on  10  "GiB" off 20  "GiB" off 2>/root/Desktop/cloud/information/iaas_size.txt')
os.system('dialog --radiolist "CPU:" 20 30 2 1 "CPU" on  2 "CPU" off 2>/root/Desktop/cloud/information/iaas_cpu.txt')
os.system('dialog --radiolist "RAM:" 20 30 2 1024 "MB" on 2048  "MB" off 2>/root/Desktop/cloud/information/iaas_ram.txt')



sip="192.168.43.253"
sport=1236

f1=open('/root/Desktop/cloud/information/iaas_name.txt')
name=f1.read()
#print type(name)
s.sendto(name,(sip,sport))

f2=open('/root/Desktop/cloud/information/iaas_os.txt')
os=f2.read()
#print type(os)
s.sendto(os,(sip,sport))

f3=open('/root/Desktop/cloud/information/iaas_size.txt')
size=f3.read()
#print type(size)
s.sendto(size,(sip,sport))

f4=open('/root/Desktop/cloud/information/iaas_cpu.txt')
cpu=f4.read()
#print type(cpu)
s.sendto(cpu,(sip,sport))

f5=open('/root/Desktop/cloud/information/iaas_ram.txt')
ram=f5.read()
#print type(ram)
s.sendto(ram,(sip,sport))



time.sleep(2)
print "Welcome your new OS is ready to open!!"
time.sleep(3)
commands.getstatusoutput("firefox http://192.168.43.253:80/vnc/?ip=192.168.43.6'&'port=4444" )
execfile ('/root/Desktop/cloud/menu.py')
close()


	

