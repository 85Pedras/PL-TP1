import sys
import re

def delete(lista,x):
    while (x in lista):
        lista.remove(x)

f = open ("processos.xml",encoding="utf8")
conteudo = f.read()

nomes = re.findall(r'<nome>(\w+).* \w+<\/nome>',conteudo)
apelidos = re.findall(r'<nome>\w+.* (\w+)<\/nome>',conteudo)

nomesOrd = dict()
apelidosOrd = dict()

for nome in nomes:
    if (nome in nomesOrd):
        nomesOrd[nome] += 1
    else:
        nomesOrd[nome] = 1


for apelido in apelidos:
    if (apelido in apelidosOrd):
        apelidosOrd[apelido] += 1
    else:
        apelidosOrd[apelido] = 1



#for elem in sorted(nomesOrd,key=nomesOrd.get,reverse=True):
#    print(elem,nomesOrd[elem])

#for elem in sorted(apelidosOrd,key=apelidosOrd.get,reverse=True):
#    print(elem,apelidosOrd[elem])


#Dic de anos
auxanos = re.findall(r'<data>(\d{4})-\d{2}-\d{2}<\/data>',conteudo)
anos = dict()
for elem in auxanos:
    if elem in anos:
        anos[elem] += 1
    else:
        anos[elem] = 1


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


for s in sorted(seculos):
    ss = int(s)-1
    nomesSec = re.findall(rf'''<data>((({s})00|{ss}0[1-9]|{ss}[1-9]\d)-(0[1-9]|1[0-2])-([0-2][1-9]|3[0-1]))<\/data>\n.+<nome>(\w+).* \w+<\/nome>''',conteudo)
    apelidosSec = re.findall(rf'''<data>((({s})00|{ss}0[1-9]|{ss}[1-9]\d)-(0[1-9]|1[0-2])-([0-2][1-9]|3[0-1]))<\/data>\n.+<nome>\w+.* (\w+)<\/nome>''',conteudo)
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
    print("Nomes século: ",s," ->",nomesOrdSec[:5])
    apelidosOrdSec = sorted(apelidosOrdSec.items(),key=lambda x: x[1],reverse=True)
    print("Apelidos século: ",s," ->",apelidosOrdSec[:5])
    print("\n")
    