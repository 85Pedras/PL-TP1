import sys
import re

# Estruturas intermédias
candidatos = set()
parentesDict = dict()

# Definições auxiliares
def parentes(lista):
    for elem in lista:
        obs = elem[3]
        parentes = re.findall(r',((?i:Irmao)|(?i:Tio)|(?i:Primo)).+?\.',obs)
        if(len(parentes) > 0):
            candidatos.add(elem[1])
            for parente in parentes:
                if parentesDict.get(parente):
                    parentesDict[parente] += 1
                else:
                    parentesDict[parente] = 1  
        
    print("Número de parentes: ",parentesDict)
    print("Número total de candidatos com parentes eclesiasticos: ",len(candidatos))

def maisFrequente(dict):
    keys = dict.keys()
    max = -1
    maxKey = ""
    for key in keys:
        if(dict[key] > max):
            max = dict[key]
            maxKey = key

    print("O parente eclesiastico mais frequente é o:",maxKey)



#Ler todo o conteúdo do xml
processos = open("processos.xml",encoding="utf8")
conteudo = processos.read()

#Número de candidatos com parentes eclesiásticos
if res := re.findall(r'<processo\s(.|\n)+?<nome>([\w\s]+)<\/nome>(.|\n)+?<obs>(.*?)<\/obs>(.|\n)+?<\/processo>',conteudo):
    parentes(res)
    maisFrequente(parentesDict)
else:
    print("Erro")


