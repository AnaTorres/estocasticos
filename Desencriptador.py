#Lenguaje de entrada
from sys import stdin
import os, re
import time
import random
import RSA

entry_language=['0','1','2','3','4','5','6','7','8','9','\n',' ']
inputPattern = re.compile('([0-9]+[\s]*)')

#Fin lenguaje de entrada
#Lenguaje de salida
exit_language=[" ","!","\"","#","$","%","&","\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?",
                "@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","]","^","_","`",
                "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~","\\","\n"]
exitPattern = re.compile('([[a-z]*[A-Z]*[0-9]*[\s]*!*"*[#]*[$]*%*&*[\']*[(]*[)]*[\*]*[+]*[,]*[.]*[-]*[.]*[/]*[:]*[;]*[<]*[>]*[=]*[?]*[`]*[{]*[|]*[~]*[}]*]*){1,300}')
#Fin lenguaje de salida
#Funcion de salida

def writeMessage(text):
    archive=open('message.txt','w')
    archive.close()
    archive=open('message.txt','a')
    archive.write(text)
    archive.close()

#Fin funcion de salida
#Estados


def readMessage(name): 
    archive=open(name,'r')                  
    line=archive.readlines()                 
    line2=""
    for i in line:
        line2=line2+i
    return line2
    archive.close()

def evalueEntry(text,identifier):
    if(identifier==1):
    #Entrada / Expresiones regulares    
        
        if (re.match(inputPattern,text)):
            return 1
        else:
            return 0

    else:
        if(identifier==2):
    #Entrada / arreglo
            correct = True
            
        for i in text:
            if ( (i in entry_language) == False):
                correct=False
                break
        if( correct == True):
            return 1
        else:
            return 0   

def evalueExit(text,identifier):
    if (identifier == 1):
    #Salida / Expresiones regulares
    

        if (re.match(exitPattern,text)):
            return 1
        else:
            return 0
        
    else:
        if (identifier==2):
    #Salida/ arreglo
            correct = True
        
        for i in text:
            if ( (i in exit_language) == False):
                corerct=False
                break
        if( correct == True):
            return 1
        else:
            return 0

def desEncrypt(text):
    archive=open('keys.txt','r')                  
    line=archive.readlines()                 
    public = line[0]
    private = line[1]
    archive.close()
    ent=[]
    textoPlano = []
    c = []
    llaveP = public.strip().split()
    e = int(llaveP[0])
    n = int(llaveP[1])
    llave = private.strip().split()
    d = int(llave[0])
    ent = text.strip().split()
    for i in range(len(ent)):
        c.append(int(ent[i]))
    for i in range(len(c)):
        temp = c[i]
        textoPlano.append(RSA.powerMod(temp,d,n))
    return textoPlano

states = {'1':readMessage, '2':evalueEntry, '3':desEncrypt, '5':evalueExit, '6':writeMessage}
#Fin estados
#Funcion de transicion
def main(nameArchive):
    text=states.get('1')(nameArchive)
    print text
    
    #decidir inicio
    name='regi.txt'
    fileRegis=open(name,'r')
    line=fileRegis.readline();
    history=line.split(',')
    for i in range(len(history)):
        history[i]=float(history[i])
    ranNum=random.random()
    prob=history[-1]
    identif=2
    if(ranNum<=prob):
        identif=1

    t0=time.clock()
    evalueEntry =states.get('2')(text,identif)
    t=time.clock()-t0
    for i in range(len(history)):
        if(t<history[i]):
            history[i]=t
            if(identif==1):
                prob+=0.001
            else:
                prob-=0.001
            break
    fileRegis.close()
    outText=''
    for i in range(len(history)-1):
        outText=outText+str(history[i])+','
    outText=outText+str(prob)
    fileRegis=open(name,'w')
    fileRegis.write(outText)
    fileRegis.close()
    #decidir fin

    print evalueEntry
    if(evalueEntry==1):
        print 'Entró al if'
        textEncrypt=states.get('3')(text)
        for i in range(len(textEncrypt)):
            print textEncrypt[i]
    else:
        return False
    stringEncrypt= ''    
    for a in range(len(textEncrypt)):
        stringEncrypt = stringEncrypt + chr(textEncrypt[a])
    print stringEncrypt
    #evalueExit = states.get('5')(stringEncrypt,2)
    
    #decidir inicio
    name='regi.txt'
    fileRegis=open(name,'r')
    line=fileRegis.readline();
    history=line.split(',')
    for i in range(len(history)):
        history[i]=float(history[i])
    ranNum=random.random()
    prob=history[-1]
    identif=2
    if(ranNum<=prob):
        identif=1

    t0=time.clock()
    evalueExit = states.get('5')(stringEncrypt,2)
    t=time.clock()-t0
    for i in range(len(history)):
        if(t<history[i]):
            history[i]=t
            if(identif==1):
                prob+=0.001
            else:
                prob-=0.001
            break
    fileRegis.close()
    outText=''
    for i in range(len(history)-1):
        outText=outText+str(history[i])+','
    outText=outText+str(prob)
    fileRegis=open(name,'w')
    fileRegis.write(outText)
    fileRegis.close()
    #decidir fin
    
    print evalueExit
    if(evalueExit==1):
        print 'Entró al if de EXIT'
        states.get('6')(stringEncrypt)
main('encrypted message.txt')
#Fin de funcion de transicion
        

