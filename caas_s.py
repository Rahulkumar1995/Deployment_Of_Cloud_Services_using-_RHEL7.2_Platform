import commands
import socket,os,string,random,time
global s
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
port=1237
s.bind(("",port))
v=0
  
name=s.recvfrom(100)
print name
no=s.recvfrom(10)
no=no[0]
no="".join(no)
no=int(no)
print no

x=name[0]
x="".join(x)
if x=="ubuntu":
	id="28f902fc8675"
elif x=="caas":
	id="4534ed2856d3"

count=0
time.sleep(3)
while count < no:
	po = random.randint(5900,5999)
	ss=str(count)
	s.sendto(str(po),("",1237))
	time.sleep(1)
	b="docker run -it -d --name="+name[0]+ss+"  -p "+str(po)+":22  -v /container:/container "+str(id)
	print b	
	os.system(b)
	count+=1	



