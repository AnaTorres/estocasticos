import socket 
import fcntl 
import struct
from subprocess import Popen, PIPE
from datetime import datetime



def create_file(name):
    archi=open(name,'w')
    archi.close()

def create_files():
     create_file('ip.txt')
     create_file('ips.txt')
     create_file('archivo.txt')
     create_file('encryptedmessage.txt')
     create_file('keys.txt')
      
     files = askInfo("FilesToAsk.txt")
     for filename in files:
         create_file(filename)

def save_ips_address():
    ips="" 

    for ip in range(0,50):    
        ipAddress = '192.168.0.'+str(ip)
        subprocess = Popen(['/bin/ping','-c 1','-w 1',ipAddress], stdout=PIPE, stdin=PIPE, stderr=PIPE)

        stdout,stderr = subprocess.communicate(input=None)

        if "bytes from" in stdout:
            ips= ips + ipAddress + "\n" 
        

    archi=open('ips.txt','w')
    archi.write(ips)    
    archi.close()  


def save_ip_address(ifname): 
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    archi=open('ip.txt','w')
    archi.write(socket.inet_ntoa(fcntl.ioctl( 
        s.fileno(), 
        0x8915, # SIOCGIFADDR 
        struct.pack('256s', ifname[:15]) 
    )[20:24]))    
    archi.close() 
   
def askInfo(filename):
    data = []
    archi=open(filename,'r')
    for line in archi:
        data.append(line.strip('\n'))    
    return data



def main():
    create_files()
    save_ip_address('eth0')    
    save_ips_address()
        
main()   
    




