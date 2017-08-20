#!/usr/bin/python2

import os,sys,commands,time,socket

os.system('dialog --menu "Select your choice" 20 50  5  1 "Saas"  2 "Staas"  3 "Iaas"  4 "Caas"  5 "Paas"   2>/root/Desktop/cloud/information/ch.txt')

f1=open('/root/Desktop/cloud/information/ch.txt')
choice=f1.read()
f1.close()

if choice == "1":
	execfile('/root/Desktop/cloud/choice/saas.py')
elif choice == "2":
	execfile('/root/Desktop/cloud/choice/staas.py')
elif choice == "3":
	execfile('/root/Desktop/cloud/choice/iaas.py')
elif choice == "4":
	execfile('/root/Desktop/cloud/choice/caas.py')
elif choice == "5":
	execfile('/root/Desktop/cloud/choice/paas.py')

else:	
	os.system('dialog --menu "Select your choice" 20 50 5  1 "Saas"  2 "Staas"  3 "Iaas"  4 "Caas"  5 "Paas"  2>/root/Desktop/cloud/infomation/ch.txt')
