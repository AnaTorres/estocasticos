import sys
import re


def dividir(fileName):
    archAgent=open(fileName,'r')
    lineIdentif=archAgent.readline()
    letraIdentif=''
    lenguajeEntr=''
    if(re.search('#Encriptar',lineIdentif)):
        letraIdentif='ae'   #agente que encripta
        lenguajeEntr='#Encriptar \n'
    else:
        letraIdentif='ad'
        lenguajeEntr='#Desencriptar \n'
    
    line= archAgent.readline()
    variable=False
    if(re.search('#Lenguaje de entrada',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        if(re.search('#Lenguaje de entrada',line)):
            variable=True;
    #print 'wiiii'
    lenguajeEntr=lenguajeEntr+'#Lenguaje de entrada\n'
    
    variable=False
    if(re.search('#Fin lenguaje de entrada',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        lenguajeEntr=lenguajeEntr+line
        if(re.search('#Fin lenguaje de entrada',line)):
            variable=True;

    archLengEntr=open(letraIdentif+'0.txt','w')
    archLengEntr.write(lenguajeEntr)
    archLengEntr.close()

    #Lenguaje de salida
    line= archAgent.readline()
    variable=False
    lenguajeSalida=''
    if(re.search('#Lenguaje de salida',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        if(re.search('#Lenguaje de salida',line)):
            variable=True;
    #print 'wiiii'
    lenguajeSalida=lenguajeSalida+'#Lenguaje de salida\n'
    
    variable=False
    if(re.search('#Fin lenguaje de salida',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        lenguajeSalida=lenguajeSalida+line
        if(re.search('#Fin lenguaje de salida',line)):
            variable=True;

    archLengSal=open(letraIdentif+'1.txt','w')
    archLengSal.write(lenguajeSalida)
    archLengSal.close()

    #Funcion de salida
    line= archAgent.readline()
    variable=False
    funcSal=''
    if(re.search('#Funcion de salida',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        if(re.search('#Funcion de salida',line)):
            variable=True;
    #print 'wiiii'
    funcSal=funcSal+'#Funcion de salida\n'
    
    variable=False
    if(re.search('#Fin funcion de salida',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        funcSal=funcSal+line
        if(re.search('#Fin funcion de salida',line)):
            variable=True;

    archLengFunSal=open(letraIdentif+'2.txt','w')
    archLengFunSal.write(funcSal)
    archLengFunSal.close()

    #Estados
    line= archAgent.readline()
    variable=False
    estados=''
    if(re.search('#Estados',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        if(re.search('#Estados',line)):
            variable=True;
    #print 'wiiii'
    estados=estados+'#Estados\n'

    cont=30
    variable=False
    if(re.search('#Fin estados',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        estados=estados+line
        cont=cont-1
        if(re.search('#Fin estados',line) or cont<=0):
            variable=True;
    
    archLengEst=open(letraIdentif+'3.txt','w')
    archLengEst.write(estados)
    archLengEst.close()

    cont=30
    estados1=''
    variable=False
    if(re.search('#Fin estados',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        estados1=estados1+line
        cont=cont-1
        if(re.search('#Fin estados',line) or cont<=0):
            variable=True;

    archLengEst=open(letraIdentif+'4.txt','w')
    archLengEst.write(estados1)
    archLengEst.close()

    estados2=''
    cont=30
    variable=False
    if(re.search('#Fin estados',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        estados2=estados2+line
        cont=cont-1
        if(re.search('#Fin estados',line) or cont<=0):
            variable=True;

    archLengEst=open(letraIdentif+'5.txt','w')
    archLengEst.write(estados2)
    archLengEst.close()

    #Funcion de transicion
    line= archAgent.readline()
    variable=False
    funcTrans=''
    if(re.search('#Funcion de transicion',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        if(re.search('#Funcion de transicion',line)):
            variable=True;
    #print 'wiiii'
    funcTrans=funcTrans+'#Funcion de transicion\n'
    
    variable=False
    cont=34
    if(re.search('#Fin de funcion de transicion',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        funcTrans=funcTrans+line
        cont=cont-1
        if(re.search('#Fin de funcion de transicion',line) or cont<=0):
            variable=True;

    archLengTrans=open(letraIdentif+'6.txt','w')
    archLengTrans.write(funcTrans)
    archLengTrans.close()

    variable=False
    cont=34
    funcTrans2=''
    if(re.search('#Fin de funcion de transicion',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        funcTrans2=funcTrans2+line
        cont=cont-1
        if(re.search('#Fin de funcion de transicion',line) or cont<=0):
            variable=True;

    archLengTrans=open(letraIdentif+'7.txt','w')
    archLengTrans.write(funcTrans2)
    archLengTrans.close()

    variable=False
    cont=34
    funcTrans3=''
    if(re.search('#Fin de funcion de transicion',line)):
        variable=True;
    while variable!=True:
        line=archAgent.readline()
        funcTrans3=funcTrans3+line
        cont=cont-1
        if(re.search('#Fin de funcion de transicion',line) or cont<=0):
            variable=True;

    archLengTrans=open(letraIdentif+'8.txt','w')
    archLengTrans.write(funcTrans3)
    archLengTrans.close()

    #print 'wiiii >:DDDDD'

    

tip =raw_input('Archivo a dividir: ')
dividir(tip)
    
        
