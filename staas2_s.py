import commands
import socket,os,string
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
port=1235
s.bind(("",port))

  
disk=s.recvfrom(10)
print disk[0]


size=s.recvfrom(10)
print size


commands.getstatusoutput("iptables -F; setenforce 0")
asd=commands.getstatusoutput("sudo lvcreate --name "+disk[0]+" --size "+size[0]+"M myvg")
print asd
commands.getstatusoutput("sudo touch /"+disk[0]+".conf")
commands.getstatusoutput("sudo chmod 777 /"+disk[0]+".conf")
f=open('/'+disk[0]+'.conf', 'w')
f.write("<target "+disk[0]+">\n\t\tbacking-store /dev/myvg/"+disk[0]+"\n</target>\n")
f.close()

b=commands.getstatusoutput("sudo mv /"+disk[0]+".conf /etc/tgt/conf.d/")
print b[0]
c=commands.getstatusoutput("systemctl restart tgtd")
if c[0] == 0:
	s.sendto("ok",(disk[1][0], 3333))
else:
	s.sendto("not", (disk[1][0], 3333 ))

