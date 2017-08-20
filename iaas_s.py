import commands
import socket,os,string
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
port=1236
s.bind(("",port))

  
name=s.recvfrom(10)
print name[0]

os=s.recvfrom(10)
print os[0]

size=s.recvfrom(10)
print size[0]

cpu=s.recvfrom(10)
print cpu[0]

ram=s.recvfrom(10)
print ram[0]

commands.getstatusoutput("iptables -F; setenforce 0")


a = commands.getstatusoutput("virt-install --hvm --name "+name[0]+" --memory "+ram[0]+" --disk=/"+name[0]+".img,size="+size[0]+" --vcpus "+cpu[0]+" --cdrom /"+os[0]+".iso      --graphics vnc,listen=0.0.0.0,port=5977 --noautoconsole")
print a

print "/root/Desktop/cloud/websockify-master/run -D 192.168.43.253:4444  192.168.43.253:5977"

b=commands.getstatusoutput("python /root/Desktop/cloud/websockify-master/run -D 192.168.43.253:4444 192.168.43.253:5977")
print b


