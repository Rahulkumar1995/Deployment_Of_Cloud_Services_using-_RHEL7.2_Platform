import commands,socket,thread,sys,time,os
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
port=4444
s.bind(("",port))
s.listen(5)	
def myc(c):
	c.send ("\t\t welcome to menu \n")
	c.send ("*Note - Close your terminal type key [exit] \n")
	c.send("Are you agree to Continus process [y/n]: ")
	software= c.recv(100)
	print software
	if software.strip()=="y": 
		while True:		
			c.send("[root@server ~]# ")
			cmd = c.recv(100)
			acmd = cmd.strip()
			if acmd == "exit":
					c.close()
					c.send('/root/Desktop/cloud/menu.py')
			else:
					out=commands.getstatusoutput(acmd)[1]
					c.send (out + "\n")
	elif software.strip()=="n":				
		c.send ('/root/Desktop/cloud/menu.py')
	c.close()
	
while True:
	c,addr = s.accept()
	thread.start_new_thread(myc, (c,))
