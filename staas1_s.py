import commands
import socket,os,string
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
port=12345
s.bind(("",port))

  
disk=s.recvfrom(10)
print disk[0]


size=s.recvfrom(10)
print size[0]

w=commands.getstatusoutput("sudo lvcreate --name "+disk[0]+" --size "+size[0]+"M myvg")
if w[0]!=0:
	w=commands.getstatusoutput("sudo lvcreate --name "+disk[0]+" --size "+size[0]+"M myvg")
else:
	commands.getstatusoutput("sudo mkfs.ext4 /dev/myvg/"+disk[0])
	v=commands.getstatusoutput("sudo mkdir /media/"+disk[0])
	print (v)
	if v[0]!=0:
		print "folder already exist"
	else:
		
		a=commands.getstatusoutput("mount /dev/myvg/"+disk[0] + " /media/"+disk[0]+"")
		print a	
commands.getstatusoutput('echo "/media/'+disk[0]+'  *(rw)" >> /etc/exports ')
commands.getstatusoutput("systemctl restart nfs")
commands.getstatusoutput('systemctl restart nfs-server')
commands.getstatusoutput("systemctl restart nfs-server.service")
commands.getstatusoutput("systemctl restart nfs-utils.service")
commands.getstatusoutput("systemctl restart nfs-mountd.service")
commands.getstatusoutput("systemctl restart nfs-client.target")
if v[0] == 0:
	s.sendto("ok",(disk[1][0], 2222))
else:
	s.sendto("not", (disk[1][0], 2222 ))


