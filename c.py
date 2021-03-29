import sys
import re

nomes = []
parentesDict = dict()

def parentes(lista):
    for elem in lista:
        obs = elem[3]
        parentes = re.findall(r',((?i:Irmao)|(?i:Tio)|(?i:Primo)).+?\.',obs)
        print(parentes)
        if(len(parentes) > 0):
            nomes.append(elem[1])
            for parente in parentes:
                if parentesDict.get(parente):
                    parentesDict[parente] += 1
                else:
                    parentesDict[parente] = 1  
        
    print(parentesDict)
    print(len(nomes))


#Ler todo o conteúdo do xml
processos = open("processos.xml",encoding="utf8")
conteudo = processos.read()
# print(conteudo)

#Número de candidatos com parentes eclesiásticos
# candidatos = set()
if res := re.findall(r'<processo\s(.|\n)+?<nome>([\w\s]+)<\/nome>(.|\n)+?<obs>(.*?)<\/obs>(.|\n)+?<\/processo>',conteudo):
    #print(res)
    # for elem in res:
    #     print(elem)
    #print(len(res))
    parentes(res)
else:
    print("Erro")


