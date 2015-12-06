import sys

def reunir(tipo):
    arch0=open(tipo+'0.txt','r')
    arch1=open(tipo+'1.txt','r')
    arch2=open(tipo+'2.txt','r')
    arch3=open(tipo+'3.txt','r')
    arch4=open(tipo+'4.txt','r')
    arch5=open(tipo+'5.txt','r')
    arch6=open(tipo+'6.txt','r')
    arch7=open(tipo+'7.txt','r')
    arch8=open(tipo+'8.txt','r')
    first=arch0.readlines()
    second=arch1.readlines()
    third=arch2.readlines()
    fourth=arch3.readlines()
    fifth=arch4.readlines()
    six=arch5.readlines()
    seven=arch6.readlines()
    eight=arch7.readlines()
    nine=arch8.readlines()
    outputText=''
    for i in range(len(first)):
        outputText=outputText+str(first[i])
    outputText=outputText+'\n'
    for i in range(len(second)):
        outputText=outputText+str(second[i])
    outputText=outputText+'\n'
    for i in range(len(third)):
        outputText=outputText+str(third[i])
    for i in range(len(fourth)):
        outputText=outputText+str(fourth[i])
    for i in range(len(fifth)):
        outputText=outputText+str(fifth[i])
    for i in range(len(six)):
        outputText=outputText+str(six[i])
    for i in range(len(seven)):
        outputText=outputText+str(seven[i])
    for i in range(len(eight)):
        outputText=outputText+str(seven[i])
    for i in range(len(nine)):
        outputText=outputText+str(seven[i])
    outputText=outputText+'\n'
    output=open('agente.py','w')
    output.write(outputText)
    output.close()

tip =raw_input('tipo: ')
reunir(tip)