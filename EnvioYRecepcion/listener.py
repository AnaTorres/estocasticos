import os
from socket import *

#import socket import fcntl import struct
def get_ip_address(ifname):
    s = socket.sockt   (socket.AF_INET,socket.SOCK_DGRAM)         
    return socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),
    0x8915, #SIOCGIFADDR
    struct.pack('256s', ifname[:15]) )[20:24])
    get_ip_address('eth0') # '192.168.0.110'



def recibir():     
    
    host = "" # set to IP address of target computer
    port = 13000
    buf = 1024
    addr = (host, port)
    print addr    
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    (data, addr) = UDPSock.recvfrom(buf)
    print "Received message: " + data    

    (ip, addr) = UDPSock.recvfrom(buf)
    print "Received message2: " + ip    

    UDPSock.close()
    return data,ip

def enviar(file1,ip):
    print "Received message3: " + file1     
    host = ip
    port = 13000
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    data=""
    archi=open(file1,'r')
    linea=archi.readline();
    while linea!="":
       data= data + "\n" + linea           
       linea=archi.readline()
    archi.close()
    UDPSock.sendto(data, addr)
    
    archi=open(file1,'w')
    archi.write('no hay nada')
    archi.close()
    UDPSock.close()



def main():
 
    while True:    
        name=recibir()
        print name
        enviar(name[0],str(name[1]))

main()



