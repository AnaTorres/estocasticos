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
    #print addr    
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    (data, addr) = UDPSock.recvfrom(buf)
    print "\n\n-> Message Recived."    

    (ip, addr) = UDPSock.recvfrom(buf)
    print "Ip:\t" + ip    

    UDPSock.close()
    return data,ip

def enviar(file1,ip):
    host = ip
    port = 13000
    addr = (host, port)
    print addr
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    data=""
    archi=open(file1,'r')
    linea=archi.readline();
    while linea!="":
       data= data + linea           
       linea=archi.readline()
    archi.close()
    UDPSock.sendto(data, addr)
    
    archi=open(file1,'w')
    archi.write('empty')
    archi.close()
    UDPSock.close()



def main():
 
    while True:    
        name=recibir()
        enviar(name[0],str(name[1]))
main()
