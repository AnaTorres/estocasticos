# Reader
import os
import sys
import random
import fcntl
import struct
import time
#import socket
from socket import *

def get_ip_address():
    archi=open('ip.txt','r')
    linea=archi.readline();
    archi.close()
    return linea

def write(name,s):
	#data = []
	
	#name = raw_input('Enter name of text file:') + '.txt'
	try:
		print "Updating " + name +" file\n"		
		file = open(name, 'w')
		file.write(s)
		file.close()
	except:
		print "Something went wrong! can\'t tell what?"
		#sys.exit(0)

def recibir(filename):
	host = ""
	data = ""
	port = 13000
	buf = 1024
	addr = (host, port)
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	UDPSock.bind(addr)
#	UDPSock.settimeout(1)
	print "5 secs to Wait to recive messages...\n"
	try:
		(data, addr) = UDPSock.recvfrom(buf)
	except:
		"TimeOut"
	if data != "empty" and data != "":
		write(filename,str(data))
	UDPSock.close()
        return data

def enviar(info, addr):
	host = addr # set to IP address of target computer
	port = 13000
	addr = (host, port)
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	UDPSock.sendto(info, addr)
	UDPSock.close()
	#os._exit(0)

def askInfo(filename):
    data = []
    i = 0
    archi=open(filename,'r')
    for line in archi:
	data.append(line.strip('\n'))
	i = i + 1    
    return data

def main():
    message = recibir("encryptedmessage.txt")
    keys = recibir("keys.txt")
    print message, keys

main()
