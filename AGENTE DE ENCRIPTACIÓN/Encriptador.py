#Lenguaje de entrada
from sys import stdin
import re
import time
import random
import RSA


entry_language=[" ","!","\"","#","$","%","&","\'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?",
                "@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","]","^","_","`",
                "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~","\\","\n"]
inputPattern = re.compile('([[a-z]*[A-Z]*[0-9]*[\s]*!*"*[#]*[$]*%*&*[\']*[(]*[)]*[\*]*[+]*[,]*[.]*[-]*[.]*[/]*[:]*[;]*[<]*[>]*[=]*[?]*[`]*[{]*[|]*[~]*[}]*]*){1,300}')

#Fin lenguaje de entrada
#Lenguaje de salida

exit_language=["0","1","2","3","4","5","6","7","8","9","\n"]
exitPattern = re.compile('([0-9]+[\s]*)')
#Fin lenguaje de salida
#Funcion de salida

def writeMessage(text):
    archive=open('encrypted message.txt','w')
    archive.close()
    archive=open('encrypted message.txt','a')
    archive.write(text)
    archive.close()


#Fin funcion de salida
#Estados
def readMessage(name):            ##Lee el mensaje del archivo txt, mientras no encuentre una linea vacía las lee y evalua si es válido su ingreso
    print 'ESTOY EN READ MESSAGE'
    archive=open(name,'r')         
    line=archive.readlines()        
    line2=""
    for i in line:
        line2=line2+i
    archive.close()
    return line2


def evalueEntry(text,identifier):
    print 'ESTOY EN EVALUE ENTRY'
    #identifier= se define en este punto la manera en que se halla el identificador
    if (identifier == 1):
    #Entrada / Expresiones regulares
        if (re.match(inputPattern,text)):
            return 1
        else:
            return 0 
        
    elif (identifier==2):
    #Entrada/ arreglo
        correct = True
        
        for i in text:
            if ( (i in entry_language) == False):
                correct=False
                break
        if( correct == True):
            return True
        else:
            return False

def evalueExit(text,identifier):
    #identifier= se define en este punto la manera en que se halla el identificador
    
    if(identifier==1):
    #Salida / Expresiones regulares    
        
        if (re.match(exitPattern,text)):
            return 1
        else:
            return 0
    elif(identifier==2):
    #Salida / arreglo
        correct = True
            
        for i in text:
            if ( (i in exit_language) == False):
                correct=False
                break
        if( correct == True):
            return 1
        else:
            return 0

def encrypt(text):
    ent=[]
    textoPlano = []
    c = []
    tp = text.strip().split()
    palabras = []
    for i in range(len(tp)):
        palabras.append(tp[i])
    for i in range(len(palabras)):
        for j in range(len(palabras[i])):
            textoPlano.append(ord(palabras[i][j]))              
    e,d,n = RSA.generarLlave()
    for i in range(len(textoPlano)):
        m = textoPlano[i]
        c.append(RSA.powerMod (m,e,n))
    for i in range(len(c)):
            print c[i]
    return c

states = {'1': readMessage, '2':evalueEntry, '3':encrypt, '5':evalueExit, '6':writeMessage}
#Fin estados
#Funcion de transicion
def main(nameArchive):
    text=states.get('1')(nameArchive)
    print text
    #evalueEntry =states.get('2')(text,1)
    
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
    evalueE =evalueEntry(nameArchive,identif)
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
    print 'termine bien :D'
    #decidir fin

    
    print evalueE
    if(evalueE==1):
        print 'Entró al if'
        textEncrypt=states.get('3')(text)
        for i in range(len(textEncrypt)):
            print textEncrypt[i]
    else:
        return False
    stringEncrypt= ''    
    for a in range(len(textEncrypt)):
        stringEncrypt = stringEncrypt + str(textEncrypt[a]) + ' '
    print stringEncrypt
    #evalueExit = states.get('5')(stringEncrypt,1)

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
    evalueEx =evalueExit(stringEncrypt,identif)
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
    print 'termine bien :D'
    #decidir fin
    
    print evalueEx
    if(evalueEx==1):
        print 'Entró al if de EXIT'
        states.get('6')(stringEncrypt)

#Fin de funcion de transicion

main('archivo.txt')
