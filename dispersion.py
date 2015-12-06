import random
import os
from socket import *
import time

def cantidad_ips():
    count=0.0
    archi=open('ips.txt','r')
    linea=archi.readline();
    while linea!="":
		count=count+1.0
		linea=archi.readline() 
    archi.close()
    return count

def seleccionar_ip():
    count = cantidad_ips() 
    ran=random.uniform(0,count)
    aux=0
    archi=open('ips.txt','r')
    linea=archi.readline();
    while aux<round(ran):
        linea=archi.readline();
        aux=aux+1.0
    archi.close()
    return linea 


def enviar(file1,ip):
#    host = seleccionar_ip()        
    host = ip
    port = 13001
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)

    data=""
    archi=open(file1,'r')
    linea=archi.readline();
    while linea!="":
       data= data + linea + "\n"          
       linea=archi.readline() 
    archi.close()
    print 'Sending files:\t' + file1
     
    archi=open(file1,'w') 
    archi.write('empty')
    archi.close()

    UDPSock.sendto(file1, addr)   
    UDPSock.sendto(data, addr)  
  
    UDPSock.close()


def recibir_confirmacion():
    host = ""
    data = ""
    port = 13001
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    UDPSock.settimeout(2)
    try:
        (bandera, addr) = UDPSock.recvfrom(buf)
        data=bandera        
    except:
        print ""

    UDPSock.close()
    return data

def enviar_confirmacion(ip):
    host = ip
    port = 13001
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    
    UDPSock.sendto(get_ip_address(), addr)    
    UDPSock.close()

def get_ip_address():
    archi=open('ip.txt','r')
    linea=archi.readline();
    archi.close()
    return linea


def askInfo(filename):
    data = []   
    archi=open(filename,'r')
    for line in archi:
        data.append(line.strip('\n'))  
    return data



def main():    
    files = askInfo("FilesToAsk.txt")
    print "============================="
    for filename in files:
        confirmacion=""
        print filename
        while confirmacion=="":	        
            ip=seleccionar_ip()
	    print "====================================\n\n"
            print "tring to stablish comunication with:\t" + ip
            enviar_confirmacion(ip)     
            confirmacion=recibir_confirmacion()
            if confirmacion!="":
                print "Sending Data:\t" + ip
                enviar(filename,ip)    
                time.sleep(.01)
            else:
                print "Communication Failed\t: " + ip


main()
