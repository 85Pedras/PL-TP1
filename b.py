import sys
import re

f = open ("processos.xml",encoding="utf8")
conteudo = f.read()

def auxOrdNomes (elem):
    return len(nomesOrd[elem])

def auxOrdApelidos (elem):
    return len(apelidosOrd[elem])

auxnomes = re.findall(r'<processo id="(\d+)">\n.+\n.+\n.+<nome>(\w+).* \w+<\/nome>',conteudo)
auxapelidos = re.findall(r'<processo id="(\d+)">\n.+\n.+\n.+<nome>\w+.* (\w+)<\/nome>',conteudo)

nomesOrd = dict()
apelidosOrd = dict()


for nome in auxnomes:
    if (nome[1] in nomesOrd):
        nomesOrd[nome[1]].add(nome[0])
    else:
        nomesOrd[nome[1]] = set()
        nomesOrd[nome[1]].add(nome[0])


for apelido in auxapelidos:
    if (apelido[1] in apelidosOrd):
        apelidosOrd[apelido[1]].add(apelido[0])
    else:
        apelidosOrd[apelido[1]] = set()
        apelidosOrd[apelido[1]].add(apelido[0])

k = int(input("Ver frequência de nomes próprios global (1)\nVer frequência de apelidos global (2)\nContinuar (0)\n>> "))
while (k == 1 or k == 2):
    if k == 1:
        print("Frequência de nomes próprios global")
        for elem in sorted(nomesOrd,key=auxOrdNomes,reverse=True):
            print(elem,":",len(nomesOrd[elem]),"vezes.")
    else:
        print("Frequência de apelidos global")
        for elem in sorted(apelidosOrd,key=auxOrdApelidos,reverse=True):
            print(elem,":",len(apelidosOrd[elem]),"vezes.")
    k = int(input("Ver frequência de nomes próprios global (1)\nVer frequência de apelidos global (2)\nContinuar (0)\n>> "))


#Dic de anos
auxanos = re.findall(r'<processo id="(\d+)">\n.+\n.+<data>(\d{4})-\d{2}-\d{2}<\/data>',conteudo)
anos = dict()
for elem in auxanos:
    if elem[1] in anos:
        anos[elem[1]].add(elem[0])
    else:
        anos[elem[1]] = set()
        anos[elem[1]].add(elem[0])


#Lista de séculos
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

print()
for s in sorted(seculos):
    ss = int(s)-1
    auxnomesSec = re.findall(rf'''<data>((({s})00|{ss}0[1-9]|{ss}[1-9]\d)-(0[1-9]|1[0-2])-([0-2][1-9]|3[0-1]))<\/data>\n.+<nome>(\w+).* \w+<\/nome>''',conteudo)
    auxapelidosSec = re.findall(rf'''<data>((({s})00|{ss}0[1-9]|{ss}[1-9]\d)-(0[1-9]|1[0-2])-([0-2][1-9]|3[0-1]))<\/data>\n.+<nome>\w+.* (\w+)<\/nome>''',conteudo)
    nomesSec = set()
    apelidosSec = set()
    for elem in auxnomesSec:
        nomesSec.add(elem)
    for elem in auxapelidosSec:
        apelidosSec.add(elem)
    nomesOrdSec = dict()
    apelidosOrdSec = dict()
    for nome in nomesSec:
        if (nome[5] in nomesOrdSec):
            k = nomesOrdSec[nome[5]] + 1
            nomesOrdSec[nome[5]] = k
        else:
            nomesOrdSec[nome[5]] = 1

    for apelido in apelidosSec:
        if (apelido[5] in apelidosOrdSec):
            k = apelidosOrdSec[apelido[5]] + 1
            apelidosOrdSec[apelido[5]] = k
        else:
            apelidosOrdSec[apelido[5]] = 1

    nomesOrdSec = sorted(nomesOrdSec.items(),key=lambda x: x[1],reverse=True)
    print("Nomes século",s,":")
    i = 0
    while (i < 5):
        print(nomesOrdSec[i][0],":",nomesOrdSec[i][1],"vezes.")
        i = i+1
    print()
    apelidosOrdSec = sorted(apelidosOrdSec.items(),key=lambda x: x[1],reverse=True)
    print("Apelidos século",s,":")
    i = 0
    while (i < 5):
        print(apelidosOrdSec[i][0],":",apelidosOrdSec[i][1],"vezes.")
        i = i+1
    print("------------------------------")

    f.close()
    