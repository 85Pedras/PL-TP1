import sys
import re

def auxOrd(elem):
    return elem[1]


f = open ("processos.xml",encoding="utf8")
conteudo = f.read()



#Número de processos por ano
auxanos = re.findall(r'<processo id="(\d+)">\n.+\n.+<data>(\d{4})-\d{2}-\d{2}<\/data>',conteudo)
anos = dict()
for elem in auxanos:
    if elem[1] in anos:
        anos[elem[1]].add(elem[0])
    else:
        anos[elem[1]] = set()
        anos[elem[1]].add(elem[0])

for elem in sorted(anos,key=anos.__hash__):
    print("Número de processos no ano ", elem, ": ", len(anos[elem]))



#Lista de processos por ordem cronologica
auxprocessos = re.findall(r'<processo id="(\d+)">\n.+\n.+<data>((\d{4})\-\d{2}\-\d{2})<\/data>\n.+\n.+\n.+\n.+\n.+<\/processo>', conteudo)
processos = set()
for elem in auxprocessos:
    processos.add(elem)
list(processos).sort(key=auxOrd)
k = int(input("Ver processos ordenados cronologicamente por ano (1), todos (2) ou continuar (0)? >> "))
while (k == 1 or k == 2):
    if k == 1:
        a = input("Introduza o ano >> ")
        print("Processos ordenados cronologicamente do ano",a,": ")
        for elem in processos:
            if elem[2] == a:
                print("Processo: ", elem[0])
    else:
        for elem in processos:
            print("Processo: ", elem[0])
    k = int(input("Ver processos ordenados por ano (1), todos (2) ou continuar (0)? >> "))


#Intervalo de datas
data_inicial = sorted(list(processos),key=auxOrd)[0][1]
data_final = sorted(list(processos),key=auxOrd)[len(processos)-1][1]

print(f'Intervalo de datas: {data_inicial} <=> {data_final}')


#Número de séculos
seculos = []
for elem in anos.keys():
    if res := re.match(r'(\d+)00',elem):
        sec = int(res[1])
        if (sec in seculos) == False:
            seculos.append(sec)

    elif res := re.match(r'(\d+)\d{2}',elem):
        sec = int(res[1])+1
        if (sec in seculos) == False:
            seculos.append(sec)
            
print("Séculos: ", sorted(seculos))
print(f'Número de séculos analisados: {len(seculos)}')
f.close()
