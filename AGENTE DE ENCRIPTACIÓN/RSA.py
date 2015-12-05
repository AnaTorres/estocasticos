# This Python file uses the following encoding: utf-8
import os,sys
import random

#Encriptación y desencriptación

def powerMod(mc,ed,n):
    base = mc
    lbinario = listaBinario(ed);
    del lbinario[0]
    if ed < 0:
         del lbinario[0]
    for i in lbinario:
        if i=='1':
            mc = (mc*mc)%n
            mc = (mc*base)%n
        else:
            mc=(mc*mc)%n
    return mc

def listaBinario(ed):
    lista=[]
    binario=bin(ed)
    for i in binario:
        lista.append(i)
    del lista[0]
    del lista[0]
    return lista

def descomponer(n):
    for i in range(2,n):
        if esprimo(i):
            if n%i==0:
                temp=n/i
                if esprimo(temp):
                    p=i
                    q=temp
                    break
    return p, q


def esprimo(numero):
    contador=0
    verificar= False
    for i in range(1,numero+1):
        if (numero%i)==0:
            contador=contador+1
        if contador >= 3:
            verificar=True
            break
    if contador==2 or verificar==False:
        return 1
    else:
        return 0

def encontrarD(n,e):
    p,q = descomponer(n)
    phi = (p-1)*(q-1)
    d = eea(phi,e)
    return d
    

#...Encriptación y desencriptación



#Generar llave

def numPrimos():
    archivo=open("primos.txt")
    lineas=len(open("primos.txt").readlines())
    plinea=random.randrange(lineas)
    qlinea=random.randrange(lineas)
    while(plinea==qlinea):
     qlinea=random.randrange(lineas)
    for i in range(lineas):
        if i==plinea:
            p=int(archivo.next())
        else:
            if i==qlinea:
                q=int(archivo.next())
            else:
                archivo.next()
    archivo.close()
    return p,q

def aleatorioE(phi):
    e = random.randint(2,(phi-1))
    g = gcd(e,phi)
    if(g!= True):
        return aleatorioE(phi)
    else:
        return e
    
def gcd(e,phi):
    r = e % phi
    if (r == 0):
        return False
    if (r == 1):
        return True
    else:
        x  = e / phi
        y = int(x)
        return gcd(phi,r)

def eea(phi,e):
    phiTemp= phi
    listaPhi=[]
    listaE=[]
    listaR=[]
    listaPhi.append(phi)
    listaE.append(e)
    r=1
    
    while(r!=0):
        r = phi % e
        listaR.append(r)
        phi= e
        e = r
        listaPhi.append(phi)
        listaE.append(e)
    x = 0
    gh = -len(listaPhi)
    i=-2
    while(i>=gh):
        a = listaPhi[i]
        b = listaE[i]
        y =  (-(a*x)+1)/b
        x = y
        i = i -1
    return y%phiTemp

#...Generar llave

def generarLlave():
    p,q = numPrimos()
    n = p * q
    phi = (p-1)*(q-1)
    e = aleatorioE(phi)
    d = eea(phi,e)
    archive=open('llaves.txt','w')
    archive.close()
    archive=open('llaves.txt','a')
    publica = str(e) + ' ' + str(n) + '\n'
    privada = str (d) + ' ' + str(n)
    archive.write(publica)
    archive.write(privada)
    archive.close()
    #print '\nLlave pública: (',e,',',n,')'
    #print 'Llave privada: (',d,',',n,')'
    return e,d,n 

#def encriptar(text):


    
def desencriptar():
    try:
        ent=[]
        textoPlano = []
        c = []
        print '\nAQUÍ SE VA A DESENCRIPTAR'
        print '\nSelecciones el modo de desencriptar'
        print '\n1. Ingresando la llave pública y la llave privada'
        print '2. Ingresando únicamente la llave pública'
        op = int(input())
        print'Ingrese la llave pública (cada término separado por un espacio (e,n))'
        llaveP = sys.stdin.readline().strip().split()
        e = int(llaveP[0])
        n = int(llaveP[1])
        if op == 1:
            print'Ingrese la llave privada (cada término separado por un espacio (d,n))'
            llave = sys.stdin.readline().strip().split()
            d = int(llave[0])
        elif op == 2:
            d = encontrarD(n,e)
        else:
            print'Opción inválida\nIntente de nuevo \n\n'
            desencriptar()
        print 'Ingrese el texto cifrado \nInstrucciones: ingrese los números separados entre sí por un espacio \nal terminar de ingresar el mensaje presione enter y obtendrá el mensaje original.'
        ent = sys.stdin.readline().strip().split()
        for i in range(len(ent)):
            c.append(int(ent[i]))
        for i in range(len(c)):
            temp = c[i]
            textoPlano.append(powerMod(temp,d,n))
        print '\nMensaje original: \n'
        try:
            for i in range(len(textoPlano)):
                print chr(textoPlano[i])
        except ValueError:
            for i in range(len(textoPlano)):
                print textoPlano[i]
    except ValueError:
        print'Opción inválida\nIntente de nuevo \n\n'
        desencriptar()    
    
def main():
    try:
        print '\nBienvenido al sistema de encriptación RSA \n    Por favor seleccione una opción'
        print '\n1.Encriptar \n2.Desencripar \n3.Salir'
        T= int(sys.stdin.readline())
        if (T==1):
            encriptar('hola')
            main()
        elif (T==2):
            desencriptar()
            main()
        elif (T==3):
            print 'Hasta pronto :D'
        else:            
            print 'Opcion inválida\nIntente de nuevo \n\n'
            main()
    except ValueError:
        print'Opción inválida\nIntente de nuevo \n\n'
        main()





