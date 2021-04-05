import sys
import re

# Estruturas intermedias
candidatos = set()
parentesDict = dict()
idsProcessos = set()

# Definicoes auxiliares
def contaParente(parentes):
    for parente in parentes:
        if parentesDict.get(parente):
            parentesDict[parente] += 1
        else:
            parentesDict[parente] = 1

def parentes(lista):
    for (idP,_,nome,_,obs) in lista:
        if(idP in idsProcessos):
            pass
        else:
            idsProcessos.add(idP);
            parentes = re.findall(r',((?i:Irmao)|(?i:Tio)|(?i:Primo)).*?\.',obs)
            if(len(parentes) > 0):
                candidatos.add(nome)
                contaParente(parentes)  
            else:
                pass
        
    print("Numero de parentes: ",parentesDict)
    print("Numero total de candidatos (diferentes) com parentes eclesiasticos (irmao, tio ou primo): ",len(candidatos))

def maisFrequente(dict):
    keys = dict.keys()
    max = -1
    maxKey = ""
    for key in keys:
        if(dict[key] > max):
            max = dict[key]
            maxKey = key

    print("O parente eclesiastico mais frequente e o:",maxKey)


# FLUXO PRINCIPAL DO PROGRAMA

#Ler todo o conteudo do xml
processos = open("processos.xml",encoding="utf8")
conteudo = processos.read()

if res := re.findall(r'<processo id="(\d+)">(.|\n)*?<nome>([\w\s]+)<\/nome>(.|\n)*?<obs>(.*?)<\/obs>',conteudo):
    parentes(res)
    maisFrequente(parentesDict)
else:
    pass

processos.close()


