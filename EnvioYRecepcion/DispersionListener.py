import os
import sys
import random
import fcntl
import struct
import time
from socket import *

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

def recibir():
    host = ""
    data = ""
    port = 13001
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    (name, addr) = UDPSock.recvfrom(buf)
    print name
    (data, addr) = UDPSock.recvfrom(buf)
    #print data
    if data != "\nempty" and data != "":
        write(name,str(data))
    UDPSock.close()


def enviar(ip):

    host = ip
    port = 13001
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    #print addr
    UDPSock.sendto("bandera", addr)
    UDPSock.close()


def recibir_pedido():
    host = ""
    data = ""
    port = 13001
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    (ip, addr) = UDPSock.recvfrom(buf)
    #print ip
    UDPSock.close()
    return ip


def main():
    while True:   
        ip=recibir_pedido()
	print "incoming comunication form:\t" + ip
        enviar(ip)
	print "Responding ip to handle communication:\t"
        recibir()
	print "reciving data from:\t" + ip
        

main()   





